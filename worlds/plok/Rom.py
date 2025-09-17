import Utils
from Utils import read_snes_rom
from worlds.AutoWorld import World
from worlds.Files import APDeltaPatch
#from .Locations import lookup_id_to_name, all_locations
from .palette_data import *

USHASH = "478a2723ff6db38428d9b26cf0d504bf"
ROM_PLAYER_LIMIT = 65535

ROM_FREE_SPACE = 0xFCE60
DEATHLINK_ADR = ROM_FREE_SPACE + 2
QUEEN_ITM_ADR = ROM_FREE_SPACE + 3
FLEASAN_ADR = ROM_FREE_SPACE + 4
MUSIC_TABLE = 0x36D9E

import hashlib
import os
import math
import random


class LocalRom:

    def __init__(self, file, patch=True, vanillaRom=None, name=None, hash=None):
        self.name = name
        self.hash = hash
        self.orig_buffer = None

        with open(file, 'rb') as stream:
            self.buffer = read_snes_rom(stream)
        #if patch:
        #    self.patch_rom()
        #    self.orig_buffer = self.buffer.copy()
        #if vanillaRom:
        #    with open(vanillaRom, 'rb') as vanillaStream:
        #        self.orig_buffer = read_snes_rom(vanillaStream)
        
    def read_bit(self, address: int, bit_number: int) -> bool:
        bitflag = (1 << bit_number)
        return ((self.buffer[address] & bitflag) != 0)

    def read_byte(self, address: int) -> int:
        return self.buffer[address]

    def read_bytes(self, startaddress: int, length: int) -> bytearray:
        return self.buffer[startaddress:startaddress + length]

    def write_byte(self, address: int, value: int):
        self.buffer[address] = value

    def write_bytes(self, startaddress: int, values):
        self.buffer[startaddress:startaddress + len(values)] = values

    def write_to_file(self, file):
        with open(file, 'wb') as outfile:
            outfile.write(self.buffer)

    def read_from_file(self, file):
        with open(file, 'rb') as stream:
            self.buffer = bytearray(stream.read())



def patch_rom(world: World, rom: LocalRom):
    rom.write_byte(0xE8000, 0x00)

    #Write Level Clear Checks
    rom.write_bytes(0xF36, bytearray([
        0x08,               #PHP
        0xE2, 0x30,         #SEP $30
        0xAD, 0x48, 0x08,   #LDA $0848
        0xA2, 0x00,         #LDX $00

        0x29, 0xF8,         #AND $F8
        0xF0, 0x06,         #BEQ
        0xE8,               #INX
        0x38,               #SEC
        0xE9, 0x08,         #SBC $08
        0x80, 0xF6,         #BRA -

        0xAD, 0x48, 0x08,   #LDA Stage
        0x29, 0x07,         #AND $07
        0xA8,               #TAY
        0xA9, 0x01,         #LDA $01
        0xC0, 0x00,         #CPY $00
        0xF0, 0x04,         #BEQ +

        0x0A,               #ASL
        0x88,               #DEY
        0xD0, 0xFC,         #BNE -

        0x8D, 0x7E, 0x07,   #STA 
        0xBD, 0x80, 0x07,   #LDA 
        0x0D, 0x7E, 0x07,   #ORA 
        0x9D, 0x80, 0x07,   #STA 
        0x28,               #PLP
        0x60                #RTS
    ]))

    #Jump to AP setup Rotuine
    rom.write_bytes(0x7E,  bytearray([0x20, 0x68, 0x8F])) #JSR $8F68
    #AP setup Rotuine
    rom.write_bytes(0xF68,  bytearray([
        0x08,               #PHP
        0X22, 0X00, 0XD4, 0x1F, # JSL $1FD400
        0xE2, 0x20,         #SEP $20
        0xEA, 0xEA,         #NOP NOP
        0xEA, 0xEA,         #NOP NOP
        0xEA, 0xEA, 0xEA,   #NOP NOP NOP
        0x28,               #PLP
        0x60                #RTS
    ]))
    rom.write_bytes(0xFD400, bytearray([
        0x9C, 0x4E, 0x08, 	#	  STZ $084E
        0x9C, 0x22, 0x07, 	#	  STZ $0722
        0x9C, 0xB6, 0x07, 	#	  STZ $07B6
        0x9C, 0xB8, 0x07, 	#	  STZ $07B8
        0x9C, 0xBA, 0x07, 	#	  STZ $07BA
        0x9C, 0xC0, 0x07, 	#	  STZ $07C0
        0x9C, 0xC2, 0x07, 	#	  STZ $07C2
        0x9C, 0xC4, 0x07, 	#	  STZ $07C4
        0x9C, 0xC6, 0x07, 	#	  STZ $07C6
        0x9C, 0xC8, 0x07, 	#	  STZ $07C8
        0xA9, 0x30, 0x00, 	#	  LDA #$0030
        0x8D, 0xB0, 0x07, 	#	  STA $07B0
        0xA9, 0x10, 0x00, 	#	  LDA #$0010
        0x8D, 0xB2, 0x07, 	#	  STA $07B2
        0xA9, 0x1C, 0x00, 	#	  LDA #$001C
        0x8D, 0xC8, 0x07,	#	  STA $07C8
        0x6B	#	  RTL
        ]))

    #Spin Jump check
    rom.write_bytes(0x36DD,  bytearray([0x2D, 0xB4, 0x07])) #AND $07B4 (check for $12)

    # Amulet Check
    rom.write_bytes(0x5825,  bytearray([0xCD, 0xB6, 0x07 ,0xB0, 0xF5])) #   CMP $07B6 -> BCS $00D81F
    # Allow Amulet in bosses
    rom.write_bytes(0x582A, bytearray([0x80, 0x0D, 0xEA])) # BRA $00D839

    #Max Health Setup LDA $07B0
    #rom.write_bytes(0x757,  bytearray([0xAD, 0xB0, 0x07]))
    #rom.write_bytes(0x148E, bytearray([0xAD, 0xB0, 0x07]))
    rom.write_bytes(0x3227, bytearray([0xAD, 0xB0, 0x07]))
    rom.write_bytes(0x3532, bytearray([0xAD, 0xB0, 0x07]))
    rom.write_bytes(0x7028, bytearray([0xAD, 0xB0, 0x07]))
    rom.write_bytes(0x14532, bytearray([0xCD, 0xB0, 0x07]))
    rom.write_bytes(0x14537, bytearray([0xAD, 0xB0, 0x07]))

    #Max Shell Setup
    rom.write_bytes(0x3D13, bytearray([
        0xCD, 0xB2, 0x07,   #CMP $07B2
        0x90, 0x07,         #BCC (RTL)
        0xAD, 0xB2, 0x07,   #LDA $07B2
        0x8D, 0xF2, 0x08,   #STA $08F2
        0xEA                #NOP
    ]))

    STAGE_SEL = bytearray([
        0x9C, 0x7A, 0x07, #   STZ $077A
        0xAD, 0x06, 0x09, 	#	    LDA $0906
        0xD0, 0x02, 	#	  BNE $1FD10A
        0xAD, 0x8C, 0x06, 	#	  LDA $068C
        0xF0, 0x27, 	#	  BEQ exit
        0xC9, 0x01, 0x00, 	#	  CMP #$0001
        0xD0, 0x06, 	#	  BNE continue
        0xA9, 0x02, 0x00, 	#	  LDA #$0002
        0x8D, 0xBC, 0x0D, 	#	  STA $0DBC
            #	  continue:
        0xC9, 0x00, 0x02, 	#	  CMP #$0200
        0xF0, 0x02, 	#	  BEQ left
        0x80, 0x05, 	#	  BRA checkright
            #	  left:
        0x20, 0x40, 0xD1, 	#	  JSR $D140
        0x80, 0x10, 	#	  BRA exit
            #	  checkright:
        0xC9, 0x00, 0x01, 	#	  CMP #$0100
        0xF0, 0x02, 	#	  BEQ right
        0x80, 0x09, 	#	  BRA exit
            #	  right:
        0x20, 0x00, 0xD2, 	#	  JSR $D200
        0x80, 0x04, 	#	  BRA exit
        0x22, 0x25, 0x81, 0x00, 	#	  JSL $008125
            #	  exit:
        0x6B, 	#	  RTL
    ])
    STAGE_INC = bytearray([
        0xDA, 	#	  PHX
        0xAD, 0x48, 0x08, 	#	  LDA $0848
        0x1A, 	#	  INC
        0xAA, 	#	  TAX
        0xC9, 0x08, 0x00, 	#	  CMP #$0008
        0xD0, 0x07, 	#	  BNE stg0A
        0xAD, 0xC0, 0x07, 	#	  LDA $07C0
        0xF0, 0x52, 	#	  BEQ exit
        0x80, 0x43, 	#	  BRA changestage
            #	  
            #	  stg0A:
        0xC9, 0x0A, 0x00, 	#	  CMP #$000A
        0xD0, 0x0E, 	#	  BNE stg17
        0xAD, 0xC2, 0x07, 	#	  LDA $07C2
        0xD0, 0x04, 	#	  BNE noskiplegacy
        0xA9, 0x12, 0x00, 	#	  LDA #$0012
        0xAA, 	#	  TAX
            #	  noskiplegacy:
        0x8A, 	#	  TXA
        0x1A, 	#	  INC
        0xAA, 	#	  TAX
        0x80, 0x30, 	#	  BRA changestage
            #	  
            #	  stg17:
        0xC9, 0x17, 0x00, 	#	  CMP #$0017
        0xD0, 0x0B, 	#	  BNE stg1D
        0xAD, 0xCA, 0x07, 	#	  LDA $07C4
        0xF0, 0x33, 	#	  BEQ exit
        0xA9, 0x17, 0x00, 	#	  LDA #$0017
        0xAA, 	#	  TAX
        0x80, 0x20, 	#	  BRA changestage
            #	  
            #	  stg1D:
        0xC9, 0x1D, 0x00, 	#	  CMP #$001D
        0xD0, 0x0B, 	#	  BNE stg27
        0xAD, 0xC4, 0x07, 	#	  LDA $07C4
        0xF0, 0x23, 	#	  BEQ exit
        0xA9, 0x20, 0x00, 	#	  LDA #$0020
        0xAA, 	#	  TAX
        0x80, 0x10, 	#	  BRA changestage
            #	  
            #	  stg27:
        0xC9, 0x27, 0x00, 	#	  CMP #$0027
        0x90, 0x0B, 	#	  BCC changestage
        0xAD, 0xC6, 0x07, 	#	  LDA $07C6
        0xF0, 0x13, 	#	  BEQ exit
        0xA9, 0x27, 0x00, 	#	  LDA #$0027
        0xAA, 	#	  TAX
        0x80, 0x0F, 	#	  BRA fleaqueenextended
            #	  
            #	  
            #	  changestage:
        0x8A, 	#	  TXA
        0x8D, 0x48, 0x08, 	#	  STA $0848
        0xFA, 	#	  PLX
        0xA9, 0xFF, 0x01, 	#	  LDA #$01FF
        0x1B, 	#	  TCS
        0x22, 0x25, 0x81, 0x00,  	#	  JSL $008125
            #	  
            #	  exit:
        0xFA, 	#	  PLX
        0x60,	#	  RTS
        # fleaqueenextended:
        0xAD, 0x48, 0x08, # LDA $0848
        0xC9, 0x27, 0x00, # CMP #$0027
        0xF0, 0xF6, # BEQ exit
        0x80, 0xE7, # BRA changestage

    ])
    STAGE_DEC = bytearray([
        0xDA, 	#	  PHX
        0xAD, 0x48, 0x08, 	#	  LDA $0848
        0xF0, 0x33, 	#	  BEQ exit
        0x3A, 	#	  DEC
        0xAA, 	#	  TAX
        0xC9, 0x1F, 0x00, 	#	  CMP #$001F
        0xD0, 0x06, 	#	  BNE stg12
        0xA9, 0x1C, 0x00, 	#	  LDA #$001C
        0xAA, 	#	  TAX
        0x80, 0x19, 	#	  BRA changestage
            #	  
            #	  stg12:
        0xC9, 0x12, 0x00, 	#	  CMP #$0012
        0xD0, 0x0B, 	#	  BNE stg0A
        0xAD, 0xC2, 0x07, 	#	  LDA $07C2
        0xD0, 0x0F, 	#	  BNE changestage
        0xA9, 0x09, 0x00, 	#	  LDA #$0009
        0xAA, 	#	  TAX
        0x80, 0x09, 	#	  BRA changestage
            #	  
            #	  stg0A:
        0xC9, 0x0A, 0x00, 	#	  CMP #$000A
        0xD0, 0x04, 	#	  BNE changestage
        0x3A, 	#	  DEC
        0xAA, 	#	  TAX
        0x80, 0x00, 	#	  BRA changestage
            #	  
            #	  changestage:
        0x8A, 	#	  TXA
        0x8D, 0x48, 0x08, 	#	  STA $0848
        0xFA, 	#	  PLX
        0xA9, 0xFF, 0x01, 	#	  LDA #$01FF
        0x1B, 	#	  TCS
        0x22, 0x25, 0x81, 0x00, 	#	  JSL $008125
            #	  
            #	  exit:
        0xFA, 	#	  PLX
        0x60, 	#	  RTS

    ])

    # Write Stage Select Rotuine
    rom.write_bytes(0x6BE1,  bytearray([0x20, 0x0A, 0xEE])) # JSR $EE0A
    rom.write_bytes(0x6DF8,  bytearray([0xF0, 0x0F])) # BEQ $00EE09
    rom.write_bytes(0x8E4,  bytearray([0x80, 0x1A])) # BRA $008890
    rom.write_bytes(0x6E0A,  bytearray([
        0x22, 0x00, 0xD1, 0x1F, 	#	  JSL $1FD100
        0xAD, 0x8C, 0x06, 	#	  LDA $068C
        0x29, 0xC0, 0xD0, 	#	  AND #$3000
        0xF0, 0x04, # BEQ $00EE1A
        0x22, 0xC0, 0xD1, 0x1F,  # JSL $1FD1C0
        0x60,	#	  RTS
    ]))
    rom.write_bytes(0xFD100,  STAGE_SEL)
    rom.write_bytes(0xFD140,  STAGE_DEC)
    rom.write_bytes(0xFD200,  STAGE_INC)
    
    # Exit Stage
    rom.write_bytes(0x6332, bytearray([
        0x22, 0x00, 0xD3, 0x1F, # JSL $1FD300
        0xEA, # NOP
        0xEA, # NOP
    ]))
    rom.write_bytes(0xFD300, bytearray([
        0xAD, 0x19, 0x42, 	#	  LDA $4219
        0x29, 0x20, 0x00, 	#	  AND #$0020
        0xF0, 0x11, 	#	  BEQ $1FD310
        0x9C, 0xF4, 0x07,   #  STZ $077A
        0x9C, 0x1E, 0x08,   #  STZ $077A
        0x9C, 0x7A, 0x07,   #  STZ $077A
        0xA9, 0xFF, 0x01, 	#	  LDA #$01FF
        0x1B, 	#	  TCS
        0x22, 0xCB, 0x88, 0x00, 	#	  JSL $0088CB
        0xAD, 0x19, 0x42, 	#	  LDA $4219
        0x29, 0x10, 0x00, 	#	  AND #$0010
        0x6B,	#	  RTL
    ]))

    # Start Stage
    rom.write_bytes(0xFD1C0, bytearray([
        0xE2, 0x20, 	#	   SEP #$20
        0xA9, 0x7F, 	#	  LDA #$7F
        0x48, 	#	  PHA
        0xAB, 	#	  PLB
        0xC2, 0x20, 	#	  REP #$20
        0xA2, 0x00, 0x01, 	#	  LDX #$0100
            #	  loop:
        0x9E, 0x00, 0x00, 	#	  STZ $0000, X
        0xCA, 	#	  DEX
        0xCA, 	#	  DEX
        0x10, 0xF9, 	#	  BPL loop
        0xE2, 0x20, 	#	  SEP #$20
        0xA9, 0x01, 	#	  LDA #$01
        0x48, 	#	  PHA
        0xAB, 	#	  PLB
        0xC2, 0x20, 	#	  REP #$20
        #0x22, 0x25, 0x81, 0x00, 	#	  JSL $008125
        0x6B, 	#	  RTL
    ]))

    # Add in level flag
    rom.write_bytes(0x336, bytearray([0x9C, 0x7A, 0x07, 0xEA, ])) #   STZ $077A
    rom.write_bytes(0x10558, bytearray([0x22, 0x40, 0xD4, 0x1F ])) # JSL $1FD440
    rom.write_bytes(0xFD440, bytearray([0xA9, 0x01, 0x00, 	#	  LDA #$0001
        0x8D, 0x7A, 0x07, 	#	  STA $077A
        0xAD, 0x48, 0x08, 	#	  LDA $0848
        0x0A, 	#	  ASL
        0x6B, 	#	  RTL
        ]))
    
    # Setup Limb States
    LIMBREAD = bytearray([0xAD, 0xC8, 0x07]) # LDA $07C8
    rom.write_bytes(0x3221,bytearray([
        0x9C, 0xF4, 0x07,       #   STZ $07F4
        0x22, 0xA0, 0xD4, 0x1F, # JSL $1FD4A0
        0xEA, 0xEA, 0xEA, 0xEA ,0xEA])) 

    #rom.write_bytes(0xF92,LIMBREAD)
    rom.write_bytes(0x138A,LIMBREAD)
    rom.write_bytes(0x1990,LIMBREAD)
    #rom.write_bytes(0x3221,LIMBREAD)
    rom.write_bytes(0x520E,LIMBREAD)
    rom.write_bytes(0x53AB,LIMBREAD)

    # On Level Load
    rom.write_bytes(0xFD4A0, bytearray([
        0xAD, 0xF4, 0x07, 	#	  LDA $07F4
        0xD0, 0x0C, 	#	  BNE normalimb
        0xAD, 0x1E, 0x08, 	#	  LDA $081E
        0xD0, 0x07, 	#	  BNE normalimb
        0xAD, 0x7A, 0x07, 	#	  LDA $077A
        0xF0, 0x02, 	#	  BEQ normalimb
        0x80, 0x05, 	#	  BRA aplimb
            #	
            #	  normalimb:
        0xA9, 0x3F, 0x00, 	#	  LDA #$003F
        0x80, 0x03, 	#	  BRA exit
            #	  aplimb:
        0xAD, 0xC8, 0x07, 	#	  LDA $07C8
            #	  exit:
        0x8D, 0x22, 0x08, 	#	  STA $0822
        0xAD,0xB0,0x07, #   LDA $07B0
        0x8D,0x06,0x08, # STA $0806
        #0xAD,0x7A,0x07, # LDA $077A
        #0xF0,0x03, # BEQ $1FD4CA
        #0x20,0xD0,0xD4, # JSR $D4D0
        0x6B, 	#	  RTL
    ]))
#    rom.write_bytes(0xFD4D0, bytearray([
#
    #]))
    # Custom Level Graphics

    # Warp Checks
    rom.write_bytes(0x1754, bytearray([0x1A, 0x8D, 0x86, 0x07, 0xEA, 0xEA,0xEA, 0xEA])) # INC -> STA $0786

    # Fruit Checks
    rom.write_bytes(0x14520, bytearray([0x22, 0x20, 0xD3, 0x1F, 0xEA, ])) # JSL $1FD320
    rom.write_bytes(0xFD320, bytearray([
        0xAD, 0x48, 0x08, 	#	  LDA $0848
        0x1A, 	#	  INC
        0x8D, 0x88, 0x07, 	#	STA $0788
        0xB5, 0x00, 	#	LDA $00, X
        0x8D, 0x8A, 0x07, 	#	STA $078A
        0xB5, 0x02, 	#	LDA $02, X
        0x8D, 0x8C, 0x07, 	#	STA $078C
        0xA9, 0xFF, 0xFF, 	#	LDA #$FFFF
        0x95, 0x00, 	#	STA $00,X
        0x6B,	#	RTL
    ]))

    # Present Transformation Changes
    rom.write_bytes(0x1443E, bytearray([
        0x80, 0x06, 	#	  BRA $82C446
        0x22, 0x40, 0xD3, 0x9F, 	#	  JSL procAP_transform
        0x80, 0x08, 	#	  BRA $82C44E
        0x22, 0xB0, 0xD3, 0x9F, 	#	  JSL procAP_vechicleFP
        0xEA, 	#	  NOP
        0xEA, 	#	  NOP
        0xEA, 	#	  NOP
        0xEA, 	#	  NOP
    ])) 
    rom.write_bytes(0x52D7, bytearray([0xEA, 0xEA, 0xEA])) # JSR $CA34 -> NOP
    rom.write_bytes(0xFD340, bytearray([
        0xDA, 	#	  PHX
        0x85, 0xDE, 	#	  STA $DE
        0xAA, 	#	  TAX
        0xA9, 0x01, 0x00, 	#	  LDA #$0001
            #	  loop:
        0x0A, 	#	  ASL
        0xCA, 	#	  DEX
        0xE0, 0x00, 0x00, 	#	  CPX #$0000
        0xD0, 0xF9, 	#	  BNE loop
        0x2D, 0xBA, 0x07, 	#	  AND $07BA
        0xF0, 0x0B, 	#	  BEQ notransform
        0xA5, 0xDE, 	#	  LDA $DE
        0x8D, 0xF4, 0x07, 	#	  STA $07F4
        0xB9, 0xC8, 0x09, 	#	  LDA $09C8,Y
        0x8D, 0xF6, 0x07, 	#	  STA $07F6
            #	  notransform:
        0xFA, 	#	  PLX
        0xAD, 0x48, 0x08, 	#	  LDA $0848
        0x8D, 0x8E, 0x07, 	#	  STA $078E
        0xB5, 0x00, 	#	  LDA $00, X
        0x8D, 0x90, 0x07, 	#	  STA $0790
        0xB5, 0x02, 	#	  LDA $02, X
        0x8D, 0x92, 0x07, 	#	  STA $0792
        0xA9, 0xFF, 0xFF, 	#	  LDA #$FFFF
        0x95, 0x00, 	#	  STA $00,X
        0x6B, 	#	  RTL
    ]))

    # Flea Pit Presents
    rom.write_bytes(0x906, bytearray([0x1D])),# Prevent softlock
    rom.write_bytes(0xFD3B0,bytearray([
        0xDA, 	#	  PHX
        0x9C, 0x1E, 0x08, 	#	  STZ $081E
        0x85, 0xDE, 	#	  STA $DE
        0xAA, 	#	  TAX
        0xA9, 0x01, 0x00, 	#	  LDA #$0001
            #	  loop:
        0x0A, 	#	  ASL
        0xCA, 	#	  DEX
        0xE0, 0x00, 0x00, 	#	  CPX #$0000
        0xD0, 0xF9, 	#	  BNE loop
        0x2D, 0xB8, 0x07, 	#	  AND $07B8
        0xF0, 0x07, 	#	  BEQ notransform
            #	  
        0xA5, 0xDE, 	#	  LDA $DE
        0x8D, 0x1E, 0x08, 	#	  STA $081E
        0x80, 0x08, 	#	  BRA transform
            #	  notransform:
            #	  
        0xA9, 0xFF, 0x01, 	#	  LDA #$01FF
        0x1B, 	#	  TCS
        0x22, 0xCB, 0x88, 0x00, 	#	  JSL $0088CB
            #	  
            #	  transform:
        0xFA, 	#	  PLX
        0xAD, 0x4E, 0x08, 	#	  LDA $084E
        0x8D, 0x8E, 0x07, 	#	  STA $078E
        0xB5, 0x00, 	#	  LDA $00, X
        0x8D, 0x90, 0x07, 	#	  STA $0790
        0xB5, 0x02, 	#	  LDA $02, X
        0x8D, 0x92, 0x07, 	#	  STA $0792
        0xA9, 0xFF, 0xFF, 	#	  LDA #$FFFF
        0x95, 0x00, 	#	  STA $00,X
        0x6B, 	#	  RTL
    ]))

    # Letter checks
    rom.write_bytes(0x1445E,bytearray([0x22, 0x80, 0xD4, 0x1F, 0xEA, 0xEA])) # JSL $1FD480 -> NOP NOP
    rom.write_bytes(0xFD480,bytearray([0xAD, 0x48, 0x08, 	#	  LDA $0848
        0x8D, 0x94, 0x07, 	#	  STA $0794
        0xB5, 0x00, 	#	  LDA $00,X
        0x8D, 0x96, 0x07, 	#	  STA $0796
        0xB5, 0x02, 	#	  LDA $02,X
        0x8D, 0x98, 0x07, 	#	  STA $0798
        0xA9, 0xFF, 0xFF, 	#	  LDA #$FFFF
        0x95, 0x00, 	#	  STA $00,X
        0xA9, 0x00, 0x00, 	#	  LDA #$0000
        0x99, 0xA8, 0x09, 	#	  STA $09A8,Y
        0x6B, 	#	  RTL
    ]))
    # Bonus Stage Changes
    rom.write_bytes(0x13165, bytearray([0x22, 0x80, 0xD3, 0x1F])),# JSL $1FD380

    rom.write_bytes(0xFD380,bytearray([0xDA, 	#	  PHX
        0xAD, 0x48, 0x08, 	#	  LDA $0848
        0x0A, 	#	  ASL
        0xAA, 	#	  TAX
        0xBD, 0x95, 0xEE, 	#	  LDA $EE95,X
        0xAA, 	#	  TAX
        0xA9, 0x01, 0x00, 	#	  LDA #$0001
        0xCA, 	#	  DEX
        0x30, 0x03, 	#	  BMI $1FD393
        0x0A, 	#	  ASL
        0x80, 0xFA, 	#	  BRA $1FD38D
        0x2D, 0xB8, 0x07, 	#	  AND $07B8
        0xF0, 0x06, 	#	  BEQ $1FD39E
        0xA9, 0x01, 0x00, 	#	  LDA #$0001
        0x8D, 0x10, 0x0A, 	#	  STA $0A10
        0xFA, 	#	  PLX
        0x6B, 	#	  RTL
        ]))

    if world.options.random_color:
        for palname, vals in palette_offsets.items():
            offset = vals[0]
            clrcount = vals[1]
            palmode = vals[0]
            match clrcount:
                case 3:
                    writeary = world.random.choice(list(threecolor.values()))
                case 4:
                    writeary = world.random.choice(list(fourcolor.values()))
                case 5:
                    writeary = world.random.choice(list(fivecolor.values()))
                case 6:
                    writeary = world.random.choice(list(sixcolor.values()))
                case 7:
                    writeary = world.random.choice(list(sevencolor.values()))
            match palmode:
                case 1: # Insert a 0x00 byte at positon 6
                    writeary.insert(6, 0x00)
                case 2:
                    writeary.insert(0xC, 0xE2)
                    writeary.insert(0xC, 0x00)
                    writeary.insert(0xC, 0x04)
                case _:
                    pass
            rom.write_bytes(offset, bytearray(writeary))

    # Do not ADvance levels
    rom.write_bytes(0x8B2, bytearray([0xEA])) # NOP

    # Starting Lives
    rom.write_byte(0xE6, world.options.start_lives.value)


    if world.options.random_music:
        for offset in range(41):
            music = (world.random.randint(0x2,0x14) * 2)
            rom.write_byte(MUSIC_TABLE + (offset *2), music)

    if world.options.random_limbsfx:
        rom.write_byte(0x3868, world.random.randint(0x1,0x4B)) #Shoot
        rom.write_byte(0x3BBC, world.random.randint(0x1,0x4B)) #Return

    from Utils import __version__
    rom.name = bytearray(f'PK{__version__.replace(".", "")[0:3]}_{world.player}_{world.multiworld.seed:11}\0', 'utf8')[:21]
    rom.name.extend([0] * (21 - len(rom.name)))
    rom.write_bytes(0x7FC0, rom.name)
    if world.options.death_link:
        rom.write_byte(DEATHLINK_ADR, 0x01)
    else:
        rom.write_byte(DEATHLINK_ADR, 0x00)
    rom.write_byte(QUEEN_ITM_ADR, world.options.queen_items.value)
    rom.write_byte(FLEASAN_ADR, world.options.fleasanity.value)



class PlokDeltaPatch(APDeltaPatch):
    hash = USHASH
    game = "Plok"
    patch_file_ending = ".aplok"

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
        file_name = options["plok_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name