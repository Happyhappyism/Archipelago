import hashlib
import math
import os
import struct
import random

from .rom_data import *
from settings import get_settings
import Utils
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes
from .com_ap_methods import randomize_dict_items, split_into_xbit_chunks, ramdomize_table_with_exclude, ramdomize_table_with_exclude_list
from BaseClasses import Location

from worlds.AutoWorld import World

MD5Hash = "79aef9bbe1378adfbd688cd66e11a7be"



# def split_into_xbit_chunks(byte_array,size):
#    #Splits a byte array into chunks of 32 bits (4 bytes).

#     chunks = []
#     for i in range(0, len(byte_array), size):
#         chunk = byte_array[i:i + size]
#         # If the last chunk is less than 4 bytes, pad it with zeros
#         if len(chunk) < size:
#             chunk += b'\x00' * (size - len(chunk)) 
#         chunks.append(chunk)
#     return chunks

# def ramdomize_table_with_exclude(tbl,entrysize,excepts):
#     split_table = split_into_xbit_chunks(tbl,entrysize)
#     idxshuffle = []
#     new_table = []
#     for x in range(len(split_table)):
#         idxshuffle.append(x)
#         new_table.append(b'/x00/x00/x00/x00')
#     random.shuffle(idxshuffle)
#     for idx in range(len(split_table)):
#         if idx in excepts:
#             new_table[idx] = split_table[idx]
#             continue
#         randidx = idxshuffle.pop(0)
#         while randidx in excepts:
#             randidx = idxshuffle.pop(0)
#         new_table[idx] = split_table[randidx]
#     result = b''.join(new_table)
#     return result

# def ramdomize_table_with_exclude_list(tbl,entrysize,excepts,baseoffset):
#     # Same as the other function but returns a list of offsets and data to write,
#     # Useful when randomizing multiple sets of data to the same table
#     split_table = split_into_xbit_chunks(tbl,entrysize)
#     idxshuffle = []
#     new_table = []
#     out_dict = {}
#     offset = baseoffset
#     for x in range(len(split_table)):
#         idxshuffle.append(x)
#         new_table.append(b'/x00/x00/x00/x00')
#     random.shuffle(idxshuffle)
#     for idx in range(len(split_table)):
        
#         if idx in excepts:
#             new_table[idx] = split_table[idx]
#             continue
#         randidx = idxshuffle.pop(0)
#         while randidx in excepts:
#             randidx = idxshuffle.pop(0)
        
#         new_table[idx] = split_table[randidx]
#         if randidx not in excepts:
#             out_dict.update({offset:new_table[idx]})
#         offset += entrysize
#     #result = b''.join(new_table)
#     return out_dict

class BomberTProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Bomberman Tournament"
    hash = MD5Hash
    patch_file_ending = ".apbombt"
    result_file_ending = ".gba"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()
    
def comicHints(world:World):
    from .Items import kara_hints
    comic_offsets = [0x21D8F2,0x21DA13,0x21DB4B,0x21DC5F,0x21DD79]

    def gethintitem(comic_id):
        match comic_id:
            case 0: # Comic 1
                world.random.shuffle(kara_hints)
                return kara_hints.pop(0)
            case 1:
                from .Items import bomb_hints
                world.random.shuffle(bomb_hints)
                return bomb_hints.pop(0)
            case 2:
                from .Items import item_hints
                world.random.shuffle(item_hints)
                return item_hints.pop(0)
            case 3:
                if world.options.zone_navigation.value != 2:
                    if world.options.zone_navigation.value == 1:
                        from .Items import key_hints
                        world.random.shuffle(key_hints)
                        return key_hints.pop(0)
                    else:
                        return "Zone Key"
                else:
                    world.random.shuffle(kara_hints)
                    return kara_hints.pop(0)
            case 4:
                if world.options.pool_medals:
                    from .Items import medal_hints
                    world.random.shuffle(medal_hints)
                    return medal_hints.pop(0)
                else:
                    world.random.shuffle(kara_hints)
                    return kara_hints.pop(0)
            case _:
                world.random.shuffle(kara_hints)
                return kara_hints.pop(0)
            
    def writeComicHint(hintitem, loc_name, player_name, comic_id):
        basetext = ""
        itemcode =  hintitem.encode('ascii')
        playercode = player_name.encode('ascii')
        loccode = loc_name.encode('ascii')
        #itemtext.encode('ascii')
        match comic_id:
            case 0:
                basetext = b'Our Hero '+ itemcode + b' \xFA is fighting evil in \xFB '+ playercode +b's \xFA '+ loccode + b'\xFF'
            case 1:
                basetext = b'Our Hero finds the peculiar\xFA '+ itemcode + b' hidden deep  '+ playercode +b's \xFA '+ loccode + b'\xFF'
            case 2:
                basetext = b'Continueing their search\xFA our hero finds the elusive\xFB'+ itemcode + b' awaiting them in \xFA '+ playercode +b's \xFB '+ loccode + b'\xFF'
            case 3:
                if world.options.zone_navigation.value != 2:
                    basetext = b'Our Hero finds the\xFA'+ itemcode + b' in\xFB '+ playercode +b's \xFA '+ loccode + b'\xFF'
                else:
                    basetext = b'Our Hero meets up with\xFA'+ itemcode + b' in their \xFB search in  '+ playercode +b's \xFA '+ loccode + b'\xFF'
            case 4:
                if world.options.pool_medals:
                    basetext = b'After defeating the evil \xFA '+ playercode + b' \xFB Our Hero finally recieves \xFA '+ itemcode +b's \xFB from '+ loccode + b'\xFF'
                else:
                    basetext = b'After defeating the evil \xFA '+ playercode + b' \xFB Our Hero frees \xFA '+ itemcode +b's \xFB from '+ loccode + b'\xFF'
                pass
        
        return basetext
    
    token_list = []
    for x in range(5):
        hintitem = gethintitem(x)
        hint_location = world.multiworld.find_item(hintitem, world.player)
        hint_player_name = world.multiworld.get_player_name(hint_location.player)
        hint_loc_name = hint_location.name
        token_list.append(APTokenTypes.WRITE,comic_offsets[x], writeComicHint(hintitem, hint_loc_name, hint_player_name, x))
    return token_list



def write_tokens(world:World, patch:BomberTProcedurePatch, fuse_dict):
    # Skip Intro dialog
    #patch.write_token(APTokenTypes.WRITE, 0x0216531, bytearray([0xFF]))
    # Do not gain items from dialog
    enemy_rando = world.options.random_enemy.value
    if enemy_rando:
        if enemy_rando == 1: # Shuffle
            shuffle_pool = {}
            for x in range(len(enemy_rando_types)): # Create a dict of enetype: enetype
                shuffle_pool.update({enemy_rando_types[x]:enemy_rando_types[x]})
            shuffled_enepool = randomize_dict_items(shuffle_pool) # Then shuffle the items
        elif enemy_rando == 2: # Chatoic random
            patch.write_token(APTokenTypes.WRITE, 0x2E564, bytearray([0x80])) # Adjust Object Sprite Start Address
        for base_offset, objlist in object_rando_bytes.items():
            if enemy_rando == 2: # Chatoic random
                enemy_pool = enemy_rando_types
                world.random.shuffle(enemy_pool)
                region_enemy_pool = []
                for x in range(7):
                    region_enemy_pool.append(enemy_pool[x])
            for objnum in range(len(objlist)):
                objoffset = (base_offset + (objnum * 0x08)) + 4
                if objlist[objnum] in enemy_rando_types:
                    if enemy_rando == 1: # Shuffle
                        randenemy = shuffled_enepool[objlist[objnum]]
                    elif enemy_rando == 2:# Chatoic random
                        randenemy = world.random.choice(region_enemy_pool)
                    patch.write_token(APTokenTypes.WRITE, objoffset, bytearray([randenemy]))
    
    # SID Fusion
    
    baseoffset = 0x30204C
    #fuse_results = [0x03, 0x09, 0x0E, 0x15]

    for x in range(4):
        karaval1 = kara_list.index(fuse_dict[fuse_items[x]][0])
        karaval2 = kara_list.index(fuse_dict[fuse_items[x]][1])
        fuse_token = bytearray([karaval1, karaval2]) #fuse_results[x],0x00, x+ 0x2C, 0x01])
        patch.write_token(APTokenTypes.WRITE, baseoffset + (x << 3), fuse_token)
        materialtextoffset = 0x3C2A00 + (x * 0x20)
        patch.write_token(APTokenTypes.WRITE, materialtextoffset, kara_list[karaval1].encode('ascii') + b'\xFF')
        patch.write_token(APTokenTypes.WRITE, materialtextoffset + 0x10, kara_list[karaval2].encode('ascii')+ b'\xFF')

    for offset, val in item_flag_adr.items():
        patch.write_token(APTokenTypes.WRITE, offset, bytearray(val))
    # Prevent Karaboms for setting themselves
    for offset in Karabon_skip_set:
        patch.write_token(APTokenTypes.WRITE, offset, bytearray([0xFF]) )
    # Skip certain dialog
    #for offset in dialog_skip:
    #    patch.write_token(APTokenTypes.WRITE, offset, bytearray([0xFF]) )
    # Softlock Fixes
    for offset, val in softlock_fixes.items():
        patch.write_token(APTokenTypes.WRITE, offset, bytearray(val) )
    # Remove zone keys
    if world.options.zone_navigation == 1:
        for offset, val in zone_lock.items():
            patch.write_token(APTokenTypes.WRITE, offset, bytearray(val) )
    # Write Rom name
    if world.options.bomber_color:
        if world.options.bomber_color.value != 16:
            patch.write_token(APTokenTypes.WRITE, 0x6DC08, bytearray(bomber_colors[world.options.bomber_color.value]) )
        else:
            patch.write_token(APTokenTypes.WRITE, 0x6DC0C, bytearray(bomber_color_primaries[world.options.bomber_body_color.value][0]) )
            patch.write_token(APTokenTypes.WRITE, 0x6DC1C, bytearray(bomber_color_primaries[world.options.bomber_body_color.value][1]) )

            patch.write_token(APTokenTypes.WRITE, 0x6DC16, bytearray(bomber_color_secondaries[world.options.bomber_limb_color.value]) )
            patch.write_token(APTokenTypes.WRITE, 0x6DC24, bytearray(bomber_color_secondaries[world.options.bomber_antenna_color.value]) )
            patch.write_token(APTokenTypes.WRITE, 0x6DC20, bytearray(bomber_color_secondaries[world.options.bomber_arm_color.value]) )
    for j, b in enumerate(world.romName):
        patch.write_token(APTokenTypes.WRITE, 0x10 + j, struct.pack("<B", b))
    for j, b in enumerate(world.playerName):
        patch.write_token(APTokenTypes.WRITE, 0x30 + j, struct.pack("<B", b))

    # Write Movement Speed
    speed = world.options.move_speed.value
    patch.write_token(APTokenTypes.WRITE, 0x6CE6, bytearray([speed]) )
    patch.write_token(APTokenTypes.WRITE, 0x6CEC, bytearray([speed + 2]) )
    patch.write_token(APTokenTypes.WRITE, 0x6CDC, bytearray([speed + 4]) ) 

    # Write Karabon Multiplier
    kara_multiplier = world.options.kara_multiply.value
    patch.write_token(APTokenTypes.WRITE, 0x711E, bytearray([kara_multiplier]) ) # Attack
    patch.write_token(APTokenTypes.WRITE, 0x713A, bytearray([kara_multiplier]) ) # Defense
    patch.write_token(APTokenTypes.WRITE, 0x714E, bytearray([kara_multiplier]) ) # Special
    
    # Write Game Options
    if world.options.death_link:
        patch.write_token(APTokenTypes.WRITE, 0x3C2800, bytearray([0x01]) )
    # Add Karabon check table
    patch.write_token(APTokenTypes.WRITE, 0x3C6500, bytearray(KARA_FLAG_CHECK) )
    if world.options.random_sound or world.options.random_music:
        audio_random_table = SOUND_TBL
        if world.options.random_sound:
            audio_random_table =  ramdomize_table_with_exclude(audio_random_table,0x8,sound_exclude)
        if world.options.random_music: # 
            audio_random_table =  ramdomize_table_with_exclude(audio_random_table,0x8,music_exclude)
        patch.write_token(APTokenTypes.WRITE, 0x31C890, audio_random_table)

    # Randomize NPC sprites, Very unstable
    if world.options.random_npc:
        for x in range(139):
            adr = 0x30046C + (x * 8)
            patch.write_token(APTokenTypes.WRITE,adr, bytearray([world.random.randint(0x00, 0x70)]))
    if world.options.autosave:
        autosavebytes = bytearray([0x00, 0xB5, # PUSH {LR}
            0x00, 0x20, # MOV R0, #00
            0x46, 0xF4, 0x5A, 0xF9, # BL 0x800633C (Save routine)
            0x04, 0xBC, # POP {R2}
            0x00, 0x00, # NOP
            0x00, 0x00, # NOP
            0x00, 0x00, # NOP
            0x01, 0x49, # LDR R1, [PC, #01]
            0x00, 0x20, # MOV R0, #00
            0x08, 0x60, # STR R0, $02035268
            0x10, 0x47, # BX R2
            0x68, 0x52, 0x03, 0x02  # db $02035268
        ])
        patch.write_token(APTokenTypes.WRITE,0x9178, bytearray([0xB6,0xF3,0x82,0xFF])) # BL $083C0080
        patch.write_token(APTokenTypes.WRITE,0x3C0080, autosavebytes)
    # Write basic text changes
    for offset, text in common_replace_txt.items():
        patch.write_token(APTokenTypes.WRITE,offset, text.encode('ascii'))

    # Write item and player text
    for loc_name, val in location_replace_txt.items():
        item = world.multiworld.get_location(loc_name,world.player).item
        item_name = item.name
        player_str = world.multiworld.get_player_name(item.player)
        if val[0]:
            i= 0
            text_array = []
            if len(player_str) > 9:
                player_str = player_str.replace(" ","")
            for c in player_str:
                if c in text_tbl:
                    text_array.append(text_tbl[c])
                    i += 1
                    if i >= 9:
                        break
            while len(text_array) < 9:
                text_array.append(0x20)
            patch.write_token(APTokenTypes.WRITE,val[0], bytearray(text_array))
        if val[1]:
            i= 0
            text_array = []
            if len(item_name) > val[2]:
                item_name = item_name.replace(" ","").replace("Progressive","")
            for c in item_name:
                if c in text_tbl:
                    text_array.append(text_tbl[c])
                    i += 1
                    if i >= val[2]:
                        break
            while len(text_array) < val[2]:
                text_array.append(0x20)
            patch.write_token(APTokenTypes.WRITE,val[1], bytearray(text_array))

    # Write Comic Hints
    
    #Testing string replacement
    #test_replace = world.multiworld.get_location("Camera",world.player).item.name
    #camera_string = []
    #for c in test_replace:
    #    if c in text_tbl:
    #        camera_string.append(text_tbl[c])
    #patch.write_token(APTokenTypes.WRITE,0x216483, bytearray(camera_string))
    
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
            raise Exception("Supplied Rom does not match knwon MD5 for Bobmerman Tournament")
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes




def get_base_rom_path(file_name: str="")-> str:
    if not file_name:
        file_name = get_settings().bombermantournament_settings.rom_file
    if not os.path.exists(file_name):
        file_name= Utils.user_path(file_name)
    return file_name