import Utils
import typing
import logging
from typing import Optional
from Utils import read_snes_rom
from worlds.AutoWorld import World
from worlds.Files import APDeltaPatch, APProcedurePatch, APTokenMixin, APTokenTypes, APPatchExtension
#from .Locations import lookup_id_to_name, all_locations
#from typing import TYPE_CHECKING
from pkgutil import get_data
#if TYPE_CHECKING:
#from . import ActraiserWorld

USHASH = "635d5d7dd2aad4768412fbae4a32fd6e"
ROM_PLAYER_LIMIT = 65535

ROM_FREE_SPACE = 0xF8000
DEATHLINK_ADR = ROM_FREE_SPACE + 2
DEBUG_ADR = ROM_FREE_SPACE + 4
DCRYSTAL_ADR = ROM_FREE_SPACE + 6
POPGOAL_ADR = ROM_FREE_SPACE + 8
TANZRA_ADR = ROM_FREE_SPACE + 10
POPGOAL_ADR_ENA = ROM_FREE_SPACE + 11
CRYGOAL_ADR_ENA = ROM_FREE_SPACE + 12

MUSIC_TABLE = 0x36D9E

import hashlib
import os
import math
#import random
#import struct

from .rom_routines import *
logger = logging.getLogger("Actraiser")

class ActraiserProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Actraiser"
    hash = [USHASH]
    patch_file_ending = ".apactr"
    procedure = [
        ("apply_tokens", ["token_data.bin"]),
    ]
    name: bytes

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()
    
    def write_byte(self, offset, value) -> None:
        self.write_token(APTokenTypes.WRITE, offset, value.to_bytes(1, "little"))

    def write_bytes(self, offset, value: typing.Iterable[int]) -> None:
        self.write_token(APTokenTypes.WRITE, offset, bytes(value))
    
    def copy_bytes(self, source, amount, destination) -> None:
        self.write_token(APTokenTypes.COPY, destination, (amount, source))


class LocalRom:

    # def __init__(self, file, patch=True, vanillaRom=None, name=None, hash=None):
    #     self.name = name
    #     self.hash = hash
    #     self.orig_buffer = None

    #     with open(file, 'rb') as stream:
    #         self.buffer = read_snes_rom(stream)
    def __init__(self, file: bytes, name: Optional[str] = None) -> None:
        self.file = bytearray(file)
        self.name = name
        
    def read_byte(self, offset: int) -> int:
        return self.file[offset]

    def read_bytes(self, offset: int, length: int) -> bytes:
        return self.file[offset:offset + length]

    def write_byte(self, offset: int, value: int) -> None:
        self.file[offset] = value

    def write_bytes(self, offset: int, values) -> None:
        self.file[offset:offset + len(values)] = values

    def get_bytes(self) -> bytes:
        return bytes(self.file)



def patch_rom(world: World, rom: ActraiserProcedurePatch):
    def import_binary_bytes(file_name: str):
        with open(file_name, "rb") as f:
                data = f.read()
        return bytearray(data)
    
    def randomize_music():
        from .rom_data import music_offsets, music_pointers
        #rom.write_bytes
        for offset in music_offsets:
            randtrack = world.random.choice(music_pointers)
            rom.write_bytes(offset, randtrack)

    def randomize_lairs():
        
        from .rom_data import custom_lair_images, lair_images,monsters
        # Write custom lair image 
        picked_lair_img = world.random.choice(list(custom_lair_images.keys()))
        rom.write_bytes(0x639C0, bytearray(custom_lair_images[picked_lair_img][0]))
        rom.write_bytes(0x63BC0, bytearray(custom_lair_images[picked_lair_img][1]))
        
        # Replace Diamond image with random custom image

        for x in range(24):
            lairoff = 0x1B825 + (x * 9)
            montype = world.random.choices(monsters, [0.4,0.25,0.2,0.15])[0]
            rom.write_byte(lairoff + 2, world.random.choice(lair_images)) # Lair Image
            rom.write_byte(lairoff + 3, montype) # Monster Type
            rom.write_byte(lairoff + 4, world.random.randint(0x1E, 0xC8)) # Action Delay
            if montype == 0x15:
                rom.write_byte(lairoff + 5, world.random.randint(0x64, 0x8D)) #Respawn Delay
            else:
                rom.write_byte(lairoff + 5, 0x01)

    def randomize_objects():
        #local_rom = LocalRom(rom)
        # valid_objects[obj_tbl_offsets.index(table_base)]
        from .rom_data import obj_tbl_offsets
        for table_base, data in obj_tbl_offsets.items():
            offset = 0
            obj_idx = 0
            valid_objs = data[0]
            enabled_objs = data[1]
            obj_list = data[2]
            for obj_id in obj_list:
                if obj_id in valid_objs and world.options.random_object:
                    rom.write_byte(table_base+ offset + 3, world.random.choices(valid_objs,enabled_objs)[0])
                elif obj_id == 0x80 and world.options.random_orb:
                    rom.write_byte(table_base+ offset + 2, world.random.randint(0x00, 0x07))
                offset += 4
                obj_idx += 1
            
            # while local_rom.read_byte(table_base+ entry) != 00 and  local_rom.read_byte(table_base+ entry) != 0xFE and local_rom.read_byte(table_base+ entry) != 0xFF:
            #     obj_id = local_rom.read_byte(table_base+ entry + 3)
            #     if obj_id in obj_tbl_offsets[table_base][0] and world.options.random_object:
            #         rom.write_byte(table_base+ entry + 3, random.choices(obj_tbl_offsets[table_base][0],obj_tbl_offsets[table_base][1])[0])
            #     elif obj_id == 0x80 and world.options.random_orb:
            #         rom.write_byte(table_base+ entry + 2, random.randint(0x00, 0x07))
            #     entry = entry + 4
            #     i = i + 1
        
    def randomize_palettes():
        from .palette_data import colorsets, pal_sources, single_color

        for object in pal_sources:
            rand_colorset = world.random.choice(list(colorsets[pal_sources[object][0]].keys()))
            i = 0
            for clrinx in pal_sources[object][1]:
                if clrinx == 18:
                    color = world.random.choice(single_color)
                    rom.write_bytes(object+i,bytearray(color))
                elif clrinx == 16:
                    i = i+2
                    continue
                elif clrinx == 17:
                    rom.write_bytes(object+i,bytearray([0x00,0x00]))
                else:
                    color = colorsets[pal_sources[object][0]][rand_colorset][clrinx]
                    rom.write_bytes(object+i,bytearray(color))
                i=i+2
            
    def text2bytes(text):
        from .rom_data import txt_table
        raw_bytes = []
        for char in text:
            if char in txt_table:
                raw_bytes.append(txt_table[char])
            else:
                raw_bytes.append(0x20) # space
        return bytearray(raw_bytes)
                    
    
    # Randomized Options
    if world.options.random_lair:
        randomize_lairs()
    if world.options.random_music:
        randomize_music()
    if world.options.random_object or world.options.random_orb:
        randomize_objects()
    if world.options.random_color:
        randomize_palettes()

    # instant default message speed
    rom.write_byte(0x13E5B, 0x00)

    # Free up AP RAM space
    rom.write_bytes(0x12E0,  bytearray([0xE0, 0x60, 0x13])) #CPX #$1360
    #This will stop the game from clearing the last 160 bytes in the enemy table in platformer segements
    #To make room for AP stuff at 0x1A00-0x1A9F

    #Jump to AP ram setup routine
    rom.write_bytes(0x37, bytearray([0x22, 0x00, 0x88, 0x1F]))  #JSL $1F8800
    
    #Jump to Item handling routine
    rom.write_bytes(0x12C69, bytearray([0x22, 0x10, 0x80, 0x1F]))  #JSL $1F8010 (from civ segments)
    rom.write_bytes(0xDB, bytearray([0x22, 0x60, 0x80, 0x1F]))  #JSL $1F8060 (from action stages)

    #Allow item handling in action stages
    #Also allows exiting stage
    rom.write_bytes(0xF8060, STAGE_EXIT) #JSL proc_decrementStageTimer -> BRA $8014

    #Jump to item check routines
    rom.write_bytes(0x892D, bytearray([0x20, 0xEA, 0x90 ])) #JSR $90EA

    #for levelup routine
    rom.write_bytes(0x1B3BD, bytearray([0xAF, 0x40, 0x1A, 0x7E ])) #LDA $1A40

    #levelup checks
    rom.write_bytes(0x1B3D4, LEVELUP_CHECKS )

    #Item handleing routine
    rom.write_bytes(0xF8010, ITEM_HANDLE)

    #Recieve Item Text Rotuine
    rom.write_bytes(0xF8A60, ITEM_TEXT_HANDLE)
    #Clear Recieve Item Text
    rom.write_bytes(0xF8AA0, CLEAR_TEXT)

    #Death Link
    rom.write_bytes(0xF8090, DEATH_LINK)

    #Jump to send death
    rom.write_bytes(0x1CE8, bytearray([0x22, 0xC0, 0x80, 0x1F, 0xEA, 0xEA]))

    #Send Death
    rom.write_bytes(0xF80C0, SEND_DEATH_LINK)

    #Individual Item Routines
    rom.write_bytes(0xF8100, ITEM_ROUTINES)

    #Recieve Magic Spell
    rom.write_bytes(0xF8230, GET_MAGIC_SPELL)

    #Recieve Offering
    rom.write_bytes(0xF8260, GET_OFFERING)
    rom.write_bytes(0x8D00, bytearray([0x22, 0x42, 0x83, 0x1F])) #JSL $1F8342
    # Backup Inventory Shift Rotuine 
    rom.write_bytes(0xF8342,BACKUP_INVENTORY)
    #Recieve Civ Level up
    rom.write_bytes(0xF8198, GET_CIVLEVEL)

    #Recieve Flame Sword
    rom.write_bytes(0xF8141, GET_FLAMESWORD)

    #Flame Sword Usage
    rom.write_bytes(0xF82B0, USE_FLAMESWORD)

    #Recieve Progressive Arrow
    rom.write_bytes(0xF8112, GET_ARROW) 

    #Recieve Death Crystal
    rom.write_bytes(0xF81B0, GET_CRYSTAL) # INC $1A48 -> RTS

    #Recieve 1UP
    rom.write_bytes(0xF8223,GET_1UP)
    #Recieve MP
    rom.write_bytes(0xF8218,GET_MP) # INC $2C -> RTS

    #Recieve 1000 points
    rom.write_bytes(0xF81D4, GET_POINTS)

    # Recieve Smite, same the bomb item routine.
    rom.write_bytes(0xF8A00, GET_SMITE)
    # Custom Population Boom Item
    rom.write_bytes(0x9CB4, bytearray([0xBF, 0xFF]))
    rom.write_bytes(0xF0AE, bytearray([0xC5, 0xFF]))
    rom.write_bytes(0xFFC0, FERT_ITEM_1)
    rom.write_bytes(0xF82C0, FERT_ITEM_2)
    rom.write_bytes(0xF82E0, FERT_ITEM_3)


    #Recieve Population Boom
    rom.write_bytes(0xF8290, GET_BOOM)

    #Recieve Skull Trap, does nothing in action stages
    rom.write_bytes(0xF8A30, GET_SKULLTRAP)

    # Redirection Trap
    rom.write_bytes(0xF8980, GET_REDIRECT)

    #Lightning
    rom.write_bytes(0x829C, GET_LIGHTNING)

    #Rain
    rom.write_bytes(0x8307, GET_RAIN)

    #Sun
    rom.write_bytes(0x8372, GET_SUN)

    #Wind
    rom.write_bytes(0x843D, GET_WIND)

    #Earthquake
    rom.write_bytes(0x83DD, GET_QUAKE)

    #Check if Miracle can be used
    rom.write_bytes(0xF8600, CHECK_MIRACLE)

    # SP Cost Text table
    rom.write_bytes(0xF85F0, SP_COST)

    #Jump to check if item is permanent routine
    rom.write_bytes(0x922B, bytearray([0x22, 0x40, 0x86, 0x1F, 0xEA])) # JSL $1F8640

    #Permanent Item (Wheat)
    rom.write_bytes(0xF8640, WHEAT)

    #Check if flame sword is collected on slash, UNTESTED
    if world.options.fire_sword:
        #rom.write_bytes(0x8CA, bytearray([0xEA, 0xAD, 0x4A, 0x1A])) #LDA $1A4A
        rom.write_bytes(0x8CA, bytearray([0x22, 0xB0, 0x82, 0x1F])) # JSL 1F82B0

    #Jump to arrow power routine
    rom.write_bytes(0xB361, bytearray([0x22, 0x58, 0x87, 0x1F, 0xEA ]))

    rom.write_bytes(0xF8758, bytearray([
        0xAD, 0x45, 0x1A, #LDA $1A45
        0x9D, 0x16, 0x00, 
        0x6B #RTL
    ]))

    #Jump to magic check routine
    rom.write_bytes(0x90E5, bytearray([0x22, 0x80, 0x87, 0x1F, 0x60])) # JSL $1F8780 -> RTS

    #jump to source of life check routine
    rom.write_bytes(0x9CBD, bytearray([0x22, 0x6E, 0x87, 0x1F, 0x80, 0x03, 0xEA, 0xEA, 0xEA,  ]))# JSL $1F876E (5 NOPS for padding)

    #Source of Magic checks
    rom.write_bytes(0x9CD6,MAGIC_LOCS)

    

    #check if item is a key item (excluding compass)
    rom.write_bytes(0x90EA, KEY_ITEM_CHECK)
    
    #key item check
    rom.write_bytes(0xF8700, KEY_ITEM_CHECK2)
        
    #Normal offerings checks
    rom.write_bytes(0xF8730, OFFERING_LOCS)
    
    #Source of Life checks
    rom.write_bytes(0xF876E, LIFE_LOCS)

    #Magic Check routine
    rom.write_bytes(0xF8780, MAGIC_ITEM_LOCS)

    #Jump to text handling routine
    #It's broken right now
    #rom.write_bytes(0x181B8, bytearray([0x20, 0x8E, 0x80 ])) #JSR $B701

    #Do not gain civ levels
    rom.write_bytes(0x1808C, bytearray([0x80, 0x05, 0x22, 0x9A, 0xFF, 0x01, 0x60,]))
    rom.write_bytes(0x1B6FC, bytearray([
        0x22, 0xA0, 0x87, 0x1F, 
        0xAE, 0xFB, 0x7B, 
        0x80, 0x2C,
        0xEA, 0xEA, 0xEA, 0xEA, 0xEA
        ]))
    
    #Civ level up checks
    rom.write_bytes(0xF87A0, CIV_LEVEL_LOCS)

    # Jump to action stage item check routine
    rom.write_bytes(0x16DF, bytearray([0x22, 0xE0, 0x87, 0x1F ])) # JSL $1F87E0

    # Action Stage check routine
    rom.write_bytes(0xF87E0, ACTION_STAGE_LOCS)

    #Setup AP Data on Load
    rom.write_bytes(0xF8800, AP_INIT)
    
    #This is to call the textbox routine from bank $1F where we have all our AP code
    #Not currently used
    rom.write_bytes(0xFF9A, bytearray([0x20, 0x29, 0x8E, 0x6B])) #JSR $8E29 -> RTL 


    #Text code
    #'Master, you do not \n have this yet.'
    rom.write_bytes(0xF283, bytearray([0x8A, 0x80, 0xFB, 0xC9, 0x0D, 0x89, 0x87, 0x79, 0x65, 0x74, 0x2E, 0x00]))

    #'AW $1A45'
    rom.write_bytes(0xF4A2, bytearray([0x41, 0x57, 0x40, 0x09, 0x02, 0x45, 0x1A, 0x20]))
    #'Crystal $1A48'
    rom.write_bytes(0xF4BF, bytearray([0x43, 0x72, 0x79, 0x73, 0x74, 0x61, 0x6C, 0x20, 0x09, 0x02, 0x48, 0x1A]))
    # Level Select Text
    rom.write_bytes(0xF783, LEVEL_TEXT)

    #Recieve Item Text
    rom.write_bytes(0xF9A00, bytearray([0x53, 0x69, 0x72, 0x2C, 0x40, 0x57, 0x65, 0x40, 0x00])) #Sir, We 
    rom.write_bytes(0xF9000, ITEM_TEXT)

    #Data Tables
    #Miracle SP and item check
    #These are used for the routine that checks if you have the miracle item
    rom.write_bytes(0xF85E0, bytearray([
        0x0A, 0x00, # lightning
        0x14, 0x00, # Rain
        0x1E, 0x00, # Sun
        0x50, 0x00, # Wind
        0xA0, 0x00, # Earthquake
        0x01, 0x02, 0x04, 0x08, 0x10, 0x20 #Bit masks
        ]))

    #item Recieve routine pointer table
    rom.write_bytes(0xF8500, ITEM_POINTERS)
    

    #This is all handled automatically now
    # Max Town Population Requirements
    #max_populations = [world.options.fillmore_max.value, world.options.bloodpool_max.value, world.options.kasandora_max.value, 
                       #world.options.aitos_max.value, world.options.marahna_max.value, world.options.northwall_max.value]
    #rom.write_bytes(0xF85D0, max_populations[0].to_bytes(2, 'little'))
    #rom.write_bytes(0xF85D2, max_populations[1].to_bytes(2, 'little'))
    #rom.write_bytes(0xF85D4, max_populations[2].to_bytes(2, 'little'))
    #rom.write_bytes(0xF85D6, max_populations[3].to_bytes(2, 'little'))
    #rom.write_bytes(0xF85D8, max_populations[4].to_bytes(2, 'little'))
    #rom.write_bytes(0xF85DA, max_populations[5].to_bytes(2, 'little'))

    # Jump to Max population check routine
    rom.write_bytes(0x1C025, bytearray([0x22, 0xA0, 0x86, 0x1F ])) # JSL $1F86A0

    # Max Town Population Checks
    rom.write_bytes(0xF86A0, MAX_POP_LOCS)

    # Pyramid Check Fix???
    rom.write_bytes(0x1FBEA, bytearray([0xA0, 0x60, 0xFE])) #LDY #$FE60
    rom.write_bytes(0x1FE60, bytearray([0x40, 0x92]))

    # Bridge Food Increase
    rom.write_bytes(0x1C0E5, bytearray([0x30])) # LDY #$30

    # Randomized level entry requirements
    act_levels = world.act_levels
    for x in range(6):
        rom.write_bytes(0x8773 + (x*2), bytearray([act_levels[x] + 1]))
        if act_levels[x] >= 9:
            textlevel = bytearray([0x31, ((act_levels[x]-9) + 0x30)])
        else:
            textlevel = bytearray([(act_levels[x] + 0x31)])
        rom.write_bytes(0xEFF4 + (x*2), textlevel)
        

    #Graphics
    # Catraiser
    
    #AP Ofering Icons
    rom.write_bytes(0xF0AC, bytearray([0xA0, 0xFF])) # Use Bag Icon Pointer
    rom.write_bytes(0xFFA0, bytearray([0x45, 0x05])) # Use Bag Icon For Item 10
    #AP Icon Top Tiles
    rom.write_bytes(0x6BC80, APICON_TOP)
    #AP Icon Bottom Tiles
    rom.write_bytes(0x6BE80, APICON_BOT)
    # Fertility icon top tiles
    rom.write_bytes(0x6BC40, FERTICON_TOP)
    # Fertility icon bottom tiles
    rom.write_bytes(0x6BE40, FERTICON_BOT)
    rom.write_bytes(0xB63E, bytearray([0x22, 0x30, 0x83, 0x1F ])) #JSL $1F8330
    #Always use item icon #10
    rom.write_bytes(0xF8330, ICON_FIX)

    #Expand SRAM
    rom.write_byte(0x7FD8, 0x04)

    #Jump to Save AP items
    rom.write_bytes(0x4F6, bytearray([0x22, 0xA0, 0x83, 0x1F ])) #JSL $1F83A0
    rom.write_bytes(0x1AA10, bytearray([0x22, 0x20, 0x84, 0x1F ])) #JSL $1F8420

    #Ap save item routine
    rom.write_bytes(0xF83A0, SAVE_ITEM)

    #Load AP items
    rom.write_bytes(0xF8420, LOAD_ITEM)

    # Make stages replayable
    rom.write_bytes(0x86D4, STAGE_REPLAY)
    rom.write_bytes(0x0104D4, STAGE_REPLAY2)
    # Stage Start Code
    rom.write_bytes(0xF89D0, STAGE_START)

    rom.write_bytes(0x22A4, bytearray([0x22, 0x80, 0x86, 0x1F, 0xEA])) #JSL 1F8680

    #Check high score and write action score checks
    rom.write_bytes(0xF8680, SCORE_LOCS)

    #Free space
    rom.write_bytes(0x86E5, bytearray([0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA]))

    #Called when clearing a level, free to JSL with 3 free extra bytes above it
    rom.write_bytes(0x2731, bytearray([0xEA, 0xEA, 0xEA, 0xEA]))

    # Goal routines
    rom.write_bytes(0x75A9, bytearray([0x20, 0x23, 0xFF])) #JSR $FF20
    rom.write_bytes(0x2357, bytearray([0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA,0xEA, 0xEA, 0xEA])) # Do not open Death heim

    # Goal type check
    rom.write_bytes(0xF83C0, GOAL_TYPE_CHECK)

    #Clear Death Heim
    rom.write_bytes(0x7F23, DHEIM_CLEAR)


    rom.write_bytes(0x18E2B, bytearray([0x22, 0x00, 0x83, 0x1F ])) #JSL $1F8300

    #Reach Population Goal Routine
    rom.write_bytes(0xF8300, POP_GOAL)

    #Faster Construction Time
    if world.options.fast_construct:
        rom.write_bytes(0x181E0, bytearray([0xC9, 0x80, 0x01])) #change Construction Wait Timer

    #DEBUG CODE
    #if world.options.debug_mode:
    #    rom.write_byte(DEBUG_ADR, 0x01)
    #    rom.write_bytes(0x181E0, bytearray([0xC9, 0x30, 0x00])) #change Construction Wait Timer
    #else:
    rom.write_byte(DEBUG_ADR, 0x00)


    if world.options.catraiser:
        
        import os
        #logger.warning("Meow")
        cat_bytes = get_data(__name__, "catraiser.bin")
        #logger.warning(f"{cat_bytes}")
        rom.write_bytes(0x68000, cat_bytes)
        rom.write_bytes(0x2E27F, BIGCATRAISER)
        rom.write_bytes(0x6B840, FISH_TOP)
        rom.write_bytes(0x6BA40, FISH_BOT)
        catraiser_text_dict = {
            "FILLMEOW":     [0x2851,0xF1CB,0x2000E,0x2177E,0x217FA,0x21D19,0x222EC,0x24D93,0x24E2F,0x25A7F],
            "BLOODPURR":    [0x285E,0xF1D4,0xF60A,0x20017,0x207D8,0x207F8,0x22068,0x22167,0x22351,0x24F70,0x25D1F],
            "MEWSNDORA":    [0x2870,0xF1DE,0xF621,0x20021,0x22BFA,0x23135,0x249C9,0x250F9,0x25C8F],
            "CATOS":        [0x2882,0xF1E8,0x2002B,0x232D3,0x233CB,0x236E8,0x23811,0x2529D,0x25B93],
            "NYANHNA":      [0x2890,0xF1EE,0x20031,0x23B0F,0x23B3B,0x23E35,0x23FDB,0x25AD3],
            "NORTHPAWS":    [0x28A0,0xF1F6,0xF659,0x20039,0x24174,0x241C6,0x24210,0x24307,0x24514,0x25514,0x25D43],
            "PAWS!":        [0x28EF],
            "Tabby":        [0x209C3,0x20A05,0x22012,0x2208D,0x223A6,0x22431,0x22469,0x2256E,0x227AA,0x229AD,0x2484E,0x24FD4,0x250D8],
            "mew":          [0xF80D,0xF82A,0xFE15,0x20255,0x20FE0,0x210C6,0x21C1E,0x22452,0x225FB,0x22B22,0x22FD0,0x23E64,0x24318,0x245A0,0x245DC,0x24743,0x24784,0x25020,0x250AA,0x2576B,0x258F3,0x25953,0x25977],
            "fur":          [0xF907,0xFC57,0xFC83,0x200D2,0x206CA,0x21094,0x216A2,0x2172F,0x219FB,0x21A66,0x21C19,0x21FE6,0x22D47,0x23468,0x235B3,0x2401C,0x24648,0x249F1,0x24A61,0x24B21,0x24BBF,0x24EA4,0x25321,0x25360,0x257D6,0x25836,0x258A0,0x25B33],
            "pawer":        [0x20ED1,0x20FA4,0x20FB9,0x21387,0x21978,0x21B3C,0x22B8B,0x22DA3,0x23028,0x23845,0x23909,0x247FE,0x2481B,0x24A14,0x2517B,0x25E4B,],
            "fresh fishy":  [0x2241E, 0x22486, 0x24835],
            "fishy":        [0x20A1F, 0x22442,]
        }
        for text, addresses in catraiser_text_dict.items():
            text_bytes = text2bytes(text)
            for address in addresses:
                rom.write_bytes(address, text_bytes)




    #set population goal
    if world.options.population_goal:
        popgoal = world.options.pop_goal_count.value
        rom.write_bytes(POPGOAL_ADR, popgoal.to_bytes(2, 'little'))
        rom.write_byte(POPGOAL_ADR_ENA, 0x02)
    else:
        rom.write_bytes(POPGOAL_ADR, bytearray([0x7F, 0x7F])) #Unachieveable
        rom.write_byte(POPGOAL_ADR_ENA, 0x00)

    #Required Death Hiem crystals
    rom.write_byte(DCRYSTAL_ADR + 0x1, 0x00)
    if world.options.crystal_goal:
        rom.write_byte(DCRYSTAL_ADR, world.options.crystal_count.value)
        rom.write_byte(CRYGOAL_ADR_ENA, 0x01)
    else:
        rom.write_byte(DCRYSTAL_ADR, 0x7F) #Unachievable
        rom.write_byte(CRYGOAL_ADR_ENA, 0x00)

    if world.options.tanzra_require:
        rom.write_byte(TANZRA_ADR, 0x01)
    else:
        rom.write_byte(TANZRA_ADR, 0x00)

    from Utils import __version__
    rom_name = bytearray(f'AR{__version__.replace(".", "")[0:3]}_{world.player}_{world.multiworld.seed:11}\0', 'utf8')[:21]
    rom_name.extend([0] * (21 - len(rom_name)))
    rom.name = bytes(rom_name)
    rom.write_bytes(0x7FC0, rom.name)
    if world.options.death_link:
        rom.write_byte(DEATHLINK_ADR, 0x01)
    else:
        rom.write_byte(DEATHLINK_ADR, 0x00)

    rom.write_file("token_data.bin", rom.get_token_binary())


class ActraiserDeltaPatch(APDeltaPatch):
    hash = USHASH
    game = "Actraiser"
    patch_file_ending = ".apactr"
    
    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()


def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        if USHASH != basemd5.hexdigest():
            raise Exception('Supplied Base Rom does not match known MD5 for US(1.0) release. '
                            'Get the correct game and version, then dump it')
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes

def get_base_rom_path(file_name: str = "") -> str:
    options = Utils.get_options()
    if not file_name:
        file_name = options["actraiser_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name