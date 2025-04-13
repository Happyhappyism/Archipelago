# Used to write routines into the game ROM


AP_BASE_ROUTINE = bytearray([
    0xE5,	#	  PUSH HL
    0xF5,	#	  PUSH AF
    0xC5,	#	  PUSH BC
    0xD5,	#	  PUSH DE
    0xFA,0x99,0xFF,	#	  LD A, ($FF99)
    0xE6,0x10,	#	  AND $10
    0x28,0x08,	#	  JR Z, checkslot
    0xFA,0x4B,0xD5,	#	  LD A, ($D54B)
    0x28,0x03,	#	  JR Z, checkslot
    0xCD,0x80,0x7B,	#	  CALL $7B80
        #	  
        #	  checkslot:
    0xFA,0xF0,0xDA,	#	  LD A, ($DAF0)
    0xE6,0x01,	#	  AND $01
    0x28,0x08,	#	  JR Z, exit
    0xCD,0x49,0x5C,	#	  CALL $5C49
    0x3E,0x00,	#	  LD A, $00
    0xEA,0xF0,0xDA,	#	  LD ($DAF0), A
        #	  exit:
    0xD1,	#	  POP DE
    0xC1,	#	  POP BC
    0xF1,	#	  POP AF
    0xE1,	#	  POP HL
    0xCD,0x4C,0x0B,	#	  CALL $0B4C
    0xC9,	#	  RET
])

AREA_SELECT = bytearray([
    0xE5,	#	  PUSH HL
    0xFA,0xAC,0xD4,	#	  LD A, ($D4AC)
    0xE6,0x04,	#	  AND $04
    0x28,0x09,	#	  JR Z, redtbl
    0x06,0x01,	#	  LD B, $01
    0x21,0xD0,0xDA,	#	  LD HL, $DAD0
    0x4D,	#	  LD C, L
    0xC3,0x97,0x7B,	#	  JP areas
        #	  redtbl:
    0x06,0x00,	#	  LD B, $00
    0x21,0xB0,0xDA,	#	  LD HL, $DAB0
    0x4D,	#	  LD C, L
        #	  areas:
        #	  
    0xFA,0x4A,0xD5,	#	  LD A, ($D54A)
    0x57,	#	  LD D, A
        #	  nextarea:
    0x7A,	#	  LD A, D
    0x69,	#	  LD L, C
    0x3C,	#	  INC A
    0x57,	#	  LD D, A
    0xFE,0x12,	#	  CP $12
    0x20,0x04,	#	  JR NZ, checkstage
    0x78,	#	  LD A, B
    0xC3,0xB1,0x7B,	#	  JP setbasestage
        #	  
        #	  checkstage:
    0x57,	#	  LD D, A
    0x4D,	#	  LD C, L
    0x85,	#	  ADD A, L
    0x6F,	#	  LD L, A
    0x7E,	#	  LD A, (HL)
    0xE6,0xFF,	#	  AND $FF
    0x28,0xEB,	#	  JR Z, nextarea
        #	
        #	  setstage:
    0x7A,	#	  LD A, D
        #	  setbasestage:
    0xEA,0x4A,0xD5,	#	  LD ($D54A), A
    0xE6,0xFF,	#	  AND $FF
    0xCE,0x29,	#	  ADC A, $29
    0xCD,0x78,0x71,	#	  CALL $7178
        #	  exit:
    0xE1,	#	  POP HL
    0xC9,	#	  RET

])