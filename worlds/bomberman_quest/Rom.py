import hashlib
import math
import os
import struct
import random
import logging

from settings import get_settings
import Utils
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from worlds.AutoWorld import World

from .rom_routines import *
from .com_ap_methods import  ramdomize_table, split_into_xbit_chunks, ramdomize_table_with_exclude


logger = logging.getLogger("Bomberman Quest")

MD5Hash = "ad358f284c3303db01212016ed3944d5" # Gameboy Color cartridge


ROM_DATA_FREESPACE = 0x63900
ROM_NAME_ADR = ROM_DATA_FREESPACE + 0x10
PLAYER_NAME_ADR = ROM_DATA_FREESPACE + 0x30
OPTION_ADR = ROM_DATA_FREESPACE

class BombQuestProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Bomberman Quest"
    hash = MD5Hash
    patch_file_ending = ".apbombquest"
    result_file_ending = ".gbc"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()
    
def write_tokens(world:World, patch:BombQuestProcedurePatch):
    from .rom_data import AP_ICON, sound_sfx_table, music_table, extra_music_table,sound_excludes
    
    from .Items import item_index, item_sythesis_index
    from .Locations import rom_location_map, sythesis_rom_map

    for j, b in enumerate(world.romName):
        patch.write_token(APTokenTypes.WRITE, ROM_NAME_ADR + j, struct.pack("<B", b))
    for j, b in enumerate(world.playerName):
        patch.write_token(APTokenTypes.WRITE, PLAYER_NAME_ADR + j, struct.pack("<B", b))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x0, bytearray([world.options.game_goal.value]))
    patch.write_token(APTokenTypes.WRITE, OPTION_ADR + 0x1, bytearray([world.options.death_link.value]))
    
    if world.options.save_heal:
        patch.write_token(APTokenTypes.WRITE, 0xB85, bytearray([0xCD, 0x50, 0x32]))
        patch.write_token(APTokenTypes.WRITE, 0x3250, HEAL_SAVE)

    # Write local items
    for loc_name, rom_offset in rom_location_map.items():
        item = world.multiworld.get_location(loc_name,world.player).item
        item_name = item.name
        if item.player == world.player:
            patch.write_token(APTokenTypes.WRITE, rom_offset,bytearray(item_index[item_name]))
            pass
        else:
            patch.write_token(APTokenTypes.WRITE, rom_offset, bytearray([0x01, 0x15]))

    for loc_name, rom_offset in sythesis_rom_map.items():
        item = world.multiworld.get_location(loc_name,world.player).item
        item_name = item.name
        if item.player == world.player:
            item_index = item_sythesis_index[item_name]
            patch.write_token(APTokenTypes.WRITE, rom_offset, bytearray([item_index, item_index]))
        else:
            patch.write_token(APTokenTypes.WRITE, rom_offset, bytearray([0x00, 0x00]))
    
    # Remove statues
    if world.options.open_regions:
        patch.write_token(APTokenTypes.WRITE, 0x442CF, bytearray([0x00])) # NOP
        patch.write_token(APTokenTypes.WRITE, 0x44375, bytearray([0x00,0x00])) # NOP
    
    # Don't use bomb core
    patch.write_token(APTokenTypes.WRITE, 0x44907, bytearray([0x00,0x00,0x00]))
    patch.write_token(APTokenTypes.WRITE, 0x4491E, bytearray([0x00,0x00,0x00]))

    # Write Synthesis checks
    patch.write_token(APTokenTypes.WRITE, 0x448BD, bytearray([0xCD,0x00,0x70]))
    patch.write_token(APTokenTypes.WRITE, 0x47000, SYNTHESIS_CHECK)

    # Starting Items
    starting_health = world.options.health_start.value * 0x10
    patch.write_token(APTokenTypes.WRITE, 0xF8240, bytearray([starting_health,starting_health]))
    if world.options.sneakers_start:
        patch.write_token(APTokenTypes.WRITE, 0xF8305, bytearray([0x10]))
    if world.options.fire_start:
        patch.write_token(APTokenTypes.WRITE, 0xF8318, bytearray([0x11]))

    if world.options.sound_shuffle:
        patch.write_token(APTokenTypes.WRITE, 0x888E, ramdomize_table_with_exclude(sound_sfx_table,2,sound_excludes))
    if world.options.music_shuffle:
        patch.write_token(APTokenTypes.WRITE, 0x487A, ramdomize_table(music_table,2))
        patch.write_token(APTokenTypes.WRITE, 0x108B2, ramdomize_table(extra_music_table,2))
    if world.options.palette_random:
        from .palette_colors import single_color
        from .palette_data import single_pal_sources
        for offset in range(0x483F8, 0x484D8, 0x02):
            patch.write_token(APTokenTypes.WRITE, offset, bytearray(world.random.choice(single_color)) )
            for offset in single_pal_sources:
                patch.write_token(APTokenTypes.WRITE, offset, bytearray(world.random.choice(single_color))  )
        pass
    # Write Card Trade Check
    from .Items import item_card_index
    from .rom_data import txt_tbl

    card_item = world.multiworld.get_location(loc_name,world.player).item
    card_item_name = card_item.name
    if card_item.player == world.player:
        patch.write_token(APTokenTypes.WRITE, 0x444C8, bytearray([item_card_index[card_item_name]]))
    else:
        patch.write_token(APTokenTypes.WRITE, 0x444C8, bytearray([0xB0]))
    text_list = []
    for char in card_item_name:
        if char in txt_tbl:
            text_list.append(txt_tbl[char])
        else:
            text_list.append(0x1)
    if len(text_list) > 10:
        text_list = text_list[:10]
    elif len(text_list) < 10:
        text_list.extend([0x01] * (10 - len(text_list)))
    # 
    patch.write_token(APTokenTypes.WRITE, 0x8F518, bytearray(text_list))
    #AP Icon
    # Use item 0x0115 for these items
    patch.write_token(APTokenTypes.WRITE, 0x2A9F1, bytearray([0x13,0x14,0x15,0x16]))
    patch.write_token(APTokenTypes.WRITE, 0x71130, AP_ICON)

    patch.write_file("token_data.bin", patch.get_token_binary())

def get_base_rom_bytes(file_name: str ="") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        md5hash = basemd5.hexdigest()
        if MD5Hash != md5hash:
            raise Exception("Supplied Rom does not match known MD5 for Bomberman Quest")
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes

def get_base_rom_path(file_name: str="")-> str:
    if not file_name:
        file_name = get_settings().bombquest_settings.rom_file
    if not os.path.exists(file_name):
        file_name= Utils.user_path(file_name)
    return file_name