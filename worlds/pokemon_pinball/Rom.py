import hashlib
import math
import os
import struct
import random

from settings import get_settings
import Utils
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from worlds.AutoWorld import World

from .Rom_routines import *
from .Palette_data import *
from .Rom_data import ENCOUNTER_DATA, slot_rewards, required_mon_data, RECIEVE_TABLE, EVO_COORDS

MD5Hash = "fbe20570c2e52c937a9395024069ba3c"

ROM_NAME_ADR = 0xF9F10
PLAYER_NAME_ADR = 0xF9F30
OPTION_ADR = 0xF9F00

class PokePinballProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Pokemon Pinball"
    hash = MD5Hash
    patch_file_ending = ".apkpinball"
    result_file_ending = ".gbc"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()
    
def write_tokens(world:World, patch:PokePinballProcedurePatch):
    for j, b in enumerate(world.romName):
        patch.write_token(APTokenTypes.WRITE, ROM_NAME_ADR + j, struct.pack("<B", b))
    for j, b in enumerate(world.playerName):
        patch.write_token(APTokenTypes.WRITE, PLAYER_NAME_ADR + j, struct.pack("<B", b))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x0, bytearray([world.options.dex_needed.value]))
    if world.options.death_link:
        patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x2, bytearray([0x01]))
    score_need = world.options.required_score.value
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x8, score_need.to_bytes(4, 'little'))

    if world.options.permanent_ball_saver:
        patch.write_token(APTokenTypes.WRITE, 0x146BB, bytearray([0x00])) # DEC -> NOP
    if world.options.strong_tilt:
        patch.write_token(APTokenTypes.WRITE, 0x372F, bytearray([0x01,0x74,0x01,0x64,0xFF,0xFF,0x01,0x6C,0x01,0x70]))

    # Catchem/Evo Map rotation requirements
    if world.options.evo_rotation.value != 0x02:
        patch.write_token(APTokenTypes.WRITE, 0x15F09, bytearray([world.options.catch_rotation.value])) # CP XX
        patch.write_token(APTokenTypes.WRITE, 0x1C930, bytearray([world.options.catch_rotation.value])) # CP XX
        patch.write_token(APTokenTypes.WRITE, 0x1D399, bytearray([world.options.catch_rotation.value])) # CP XX
    if world.options.evo_rotation.value != 0x03:
        # Red Field
        patch.write_token(APTokenTypes.WRITE, 0x107ED, bytearray([world.options.evo_rotation.value])) # CP XX
        patch.write_token(APTokenTypes.WRITE, 0x107F0, bytearray([0x38, 0x02])) # JR C, $47F4
        # Blue Field
        patch.write_token(APTokenTypes.WRITE, 0x1C8F5, bytearray([world.options.evo_rotation.value, 0x30, 0x04])) # CP XX
        patch.write_token(APTokenTypes.WRITE, 0x1C960, bytearray([world.options.evo_rotation.value, 0x38, 0x1C])) # CP XX
        patch.write_token(APTokenTypes.WRITE, 0x1D282, bytearray([world.options.evo_rotation.value, 0x38, 0x14])) # CP XX

    if world.options.less_tired:
        patch.write_token(APTokenTypes.WRITE, 0x21030, bytearray([0x00]))
        patch.write_token(APTokenTypes.WRITE, 0x20A29, bytearray([0x00]))
    patch.write_token(APTokenTypes.WRITE, 0x7C30, EVO_COORDS)
    patch.write_token(APTokenTypes.WRITE, 0x7D00, EVO_ITEM)

    # Base AP routines
    patch.write_token(APTokenTypes.WRITE, 0x3740, CALL_BANKSWITCH)
    patch.write_token(APTokenTypes.WRITE, 0xD946, bytearray([0xCD, 0x00, 0x7B])) # CALL $7B00
    patch.write_token(APTokenTypes.WRITE, 0xDB15, bytearray([0xCD, 0x40, 0x7C])) # CALL $7CC0
    patch.write_token(APTokenTypes.WRITE, 0xFB00, AP_BASE_ROUTINE)
    patch.write_token(APTokenTypes.WRITE, 0xFB80, AREA_SELECT)
    patch.write_token(APTokenTypes.WRITE, 0xFC00, CHECK_MOVE)
    patch.write_token(APTokenTypes.WRITE, 0xFC40, SWAP_TABLE)
    patch.write_token(APTokenTypes.WRITE, 0x83BA, bytearray([0xCD, 0x80, 0x4F])) # CALL $4F80
    patch.write_token(APTokenTypes.WRITE, 0x8F80, RESTORE_PARTY)
    patch.write_token(APTokenTypes.WRITE, 0xFC04, bytearray([world.options.map_btn.value])) # Map Button
    patch.write_token(APTokenTypes.WRITE, 0xFC80, RECIEVE_TABLE)
    #patch.write_token(APTokenTypes.WRITE, 0xFC44, bytearray([world.options.map_btn.value])) # Map Button

    # Ensure new mons
    patch.write_token(APTokenTypes.WRITE, 0x10089, bytearray([0xCD, 0x00, 0x78, 0x28, 0xDE, 0x00])) # CALL $7800 -> JR Z, $4074 -> NOP
    patch.write_token(APTokenTypes.WRITE, 0x13800, NEW_CATCHEM)

    # REstrict start stage table
    patch.write_token(APTokenTypes.WRITE, 0x16605, bytearray([0x00,0x00,0x00,0x00,0x00,0x00,0x00])) # Red Table Palette Town
    patch.write_token(APTokenTypes.WRITE, 0x1C8AF, bytearray([0x01,0x01,0x01,0x01,0x01,0x01,0x01])) # Blue Table Viridian City

    # Red Table Move area
    patch.write_token(APTokenTypes.WRITE, 0x312A1, RESTRICT_MAP_MOVE_R)
    #patch.write_token(APTokenTypes.WRITE, 0x312D5, bytearray([0xEA, 0xF1, 0xDA])) # LD ($DAF1), A
    # Blue Table Move Area
    #patch.write_token(APTokenTypes.WRITE, 0x3145F, bytearray([0xEA, 0xF2, 0xDA])) # LD ($DAF2), A
    patch.write_token(APTokenTypes.WRITE, 0x3142B, RESTRICT_MAP_MOVE_B)
    # Change Slots table
    for offset, data in slot_rewards.items():
        patch.write_token(APTokenTypes.WRITE, offset, bytearray([data]))

    
    if world.options.required_mons.value:
        from .Locations import pokemon_names
        
        for mon in world.options.required_mons.value:
            if mon in pokemon_names:
                required_mon_data[pokemon_names.index(mon)] = 0x00
    patch.write_token(APTokenTypes.WRITE, 0xDD400, bytearray(required_mon_data))
    

    if world.options.rebalance_encounters:
        for offset, data in ENCOUNTER_DATA.items():
            patch.write_token(APTokenTypes.WRITE, offset, bytearray(data))

    if world.options.mon_colors:
        for startoffset, endoffset in mon_pal_offsets.items():
            offset = startoffset
            while offset < endoffset:
                pal1 = world.random.randint(0, 0x7FFF),
                pal2 = world.random.randint(0, 0x7FFF),
                patch.write_token(APTokenTypes.WRITE, offset+2, pal1[0].to_bytes(2, "little"))
                patch.write_token(APTokenTypes.WRITE, offset+4, pal2[0].to_bytes(2, "little"))
                offset += 0x08
    if world.options.map_colors:
        invalid_offsets = [0x00,0x06,0x08,0x0E]
        for color, offsets in field_pal_data.items():
            clr = world.random.randint(0, 0x7FFF),
            for offset in offsets:
                if offset & 0xF not in invalid_offsets:
                    patch.write_token(APTokenTypes.WRITE, offset, clr[0].to_bytes(2, "little"))
        #offset = 0xDC880
        ##while offset < 0xdd140:
         #       pal1 = world.random.randint(0, 0x7FFF),
         #       pal2 = world.random.randint(0, 0x7FFF),
         #       patch.write_token(APTokenTypes.WRITE, offset+2, pal1[0].to_bytes(2, "little"))
         #       patch.write_token(APTokenTypes.WRITE, offset+4, pal2[0].to_bytes(2, "little"))
         #       offset += 0x08

    if world.options.double_timer:
        patch.write_token(APTokenTypes.WRITE, 0x867D, bytearray([0xCD, 0x06, 0x4F, 0x00,0x00,0x00,0x00,0x00])) # CALL $8F06
        patch.write_token(APTokenTypes.WRITE, 0x8F06, DOUBLE_TIME) # CALL $8F06

    patch.write_file("token_data.bin", patch.get_token_binary())

def get_base_rom_bytes(file_name: str ="") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        md5hash = basemd5.hexdigest()
        if MD5Hash !=md5hash:
            raise Exception("Supplied Rom does not match known MD5 for Pokemon Pinball")
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes

def get_base_rom_path(file_name: str="")-> str:
    if not file_name:
        file_name = get_settings().pokepinball_settings.rom_file
    if not os.path.exists(file_name):
        file_name= Utils.user_path(file_name)
    return file_name