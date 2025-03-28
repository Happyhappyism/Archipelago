item_flag_adr = {
    # Powerups
    0x6C42: [0x4A, 0x70], # Don't Gain Health (strb r2, [r1, #2])ca
    0x6C9A: [0x8A, 0x70], # Don't Gain Bombup (strb r2, [r1, #2])ca
    0x6CBA: [0xCA, 0x70], # Don't Gain Fireups (strb r2, [r1, #3])
    

    # Items
    0x46358: [0xD8], #Comic 1 Write
    0x2F5060: [0x60, 0x03], # Comic 1 Read
    0x463A4: [0xD9], #Comic 2
    0x2F5A5C: [0x64, 0x03], # Comic 2 Read
    0x2F50B4: [0x64, 0x03], # Comic 2 Read
    0x463F0: [0xDA], #Comic 3
    0x2F602C: [0x68, 0x03], # Comic 3 Read
    0x2F6140: [0x68, 0x03], # Comic 3 Read
    0x4643C: [0xDB], #Comic 4
    0x2F6AE8: [0x6C, 0x03], # Comic 4 Read
    0x2F6DD0: [0x6C, 0x03], # Comic 4 Read
    0x46488: [0xDC], #Comic 5
    0x2F71B4: [0x6C, 0x03], # Comic 5 Read
    0x21637B: [0x01,0xCE], # Ring Pickup
    0x215FDC: [0x00,0x2E], # Check for Ring in Invetory
    0x21646C: [0x01,0xCC], # Camera
    0x459FC: [0x2C,0x00], # Louie Checks for Camera
    0x216940: [0x21, 0xE0, 0x04, 0x01, 0x16, 0x20, 0x20, 0x20], # Reset Louie
    #0x2163B3: [0x01,0x71], # Skip Camera Dialog
    0x21A031: [0x01,0xD1], # Fish Hook -> $2A9[0]
    0x2169C1: [0x01,0xC4], # Sensor
    0x219AD2: [0x01,0xC1], # Raindrop
    0x2199C7: [0xE0, 0x01, 0x00, 0x31, 0x05, 0x17, 0xE0, 0x01, 0x01, 0x36, 0x05, 0x16, 
               0xE0, 0x01, 0x01, 0x36, 0x05, 0x16,], # Sempai
    0x21BF61: [0x01,0xC3], # Transistor
    0x21F499: [0x01,0xC0], # Balloon
    0x21C1BE: [0x01,0xC2], # Hammer Write?
    0x2F5180: [0x08,0x07], # Hammer Read
    0x48816: [0xE3], # Beef
    0x301188: [0xE3], # Beef Write
    #0x2F5180: [0x00, 0x07], # Comic 4 Read
    0x220690: [0x01,0xD5], # Ice Flower
    #0x21EB7A: [0x01,0xD2], # Flour
    #0x21EE4A: [0x01,0xD3], # Bread
    #0x21EE3A: [0x00,0x39], # Check for Flour
    0x21ED32: [0x01,0xD4], # Egg
    0x2212E6: [0x01,0xD8], # Step Counter
    0x4929A: [0x79], # Don't lose Beef from Morg
    0x223AC6: [0x03], # Don't lose Beef in heart trade
    0x2F5D20: [0xD0, 0x06], # Iceflower Reading Pteradon 0x00D0 Ice Flower
    #0x4C3A0: [0x00, 0xD0], # Pteradon Ice Flower BEQ $4
    


    # Medals
    0x218537: [0x01,0xC8], # Bravery
    0x21AE46: [0x01,0xC9], # Justice
    0x301954: [0xCA,0x01], # Love
    0x301B2A: [0xCB,0x01], # Friendship

    # Bosses
    0x211E52: [0xDD], # Magnet Bomber Defeat Read
    0x211E54: [0xE7], # Pretty Bomber Defeat Read
    0x211E56: [0xE8], # Plasma Bomber Defeat Read
    0x211E58: [0xE9], # Golem Bomber Defeat Read
    0x1F7D78: [0xDD], # Magmnet Bomber Defeat Write

    #Chests
    0x4BF76: [0x79], #Silver Boot Chest
    0x4BF87: [0x79], #Silver Armor Chest
    0x4BF92: [0x79], #Gold Armor Chest
    0x4BFA2: [0x79], #Gold Armor Chest
    0x4C02E: [0x79], #Magnet Crystal Chest
    0x4C03A: [0x79], #Pretty Crystal Chest
    0x4C046: [0x79], #Plasma Crystal Chest
    0x4C052: [0x79], #Golem Crystal Chest
    0x4C05E: [0x79], #Fantasy Crystal Chest
    0x4C06A: [0x79], #Radar Chest
    0x4C082: [0x79], #Disinfectent Chest

    # Karabon Fusion
    #0x4E01C: [0x00, 0x65, 0x3C, 0x08],

    #Karabons
    #0x4AB1E: [0x19, 0xE0], # Allow refusion
    0x21635F: [0x00], # Do not Set Pommy
    0x300942: [0xA8,0x81], # Pommy Read
    0x49E5C:  [0xA8,0x01], # Pommy Write
    0x300958: [0xA9,0x81], # Ceedrun Read
    0x2FFA5E: [0xA9,0x01], # Ceedrun Write
    0x45A48: [0xD5,0x20], # Eflian Read
    0x4A07E: [0xD5,0x20], # Eflian Read
    0x4A0FE: [0xD5,0x20], # Eflian Write
    0x45590: [0xD5], # Eflian Prisoner Always On
    0x45B38:  [0xAD, 0x1], # Th Ligar Read Spawn 
    0x2F5594: [0xB4,0x06], 0x2F55A0: [0xB4,0x06],  # Th Ligar Read Interact
    0x301222: [0xAD,0x01], # Th Ligar Write
    0x460B0: [0xAC, 0x01], # Sharkun Read Spawn
    0x30106A: [0xAC,0x01], # Sharkun Write
    0x45BA8: [0xAF, 0x01], # Kai-man Read Spawn
    0x489EC: [0xAF, 0x01], # Kai-man Read Interact
    0x21B2CB: [0x01, 0xAF], # Kai-man Dialog Read
    0x2195B3: [0x01, 0xAF], # Kai-man Dialog Read
    0x2197DE: [0x01, 0xAF], # Kai-man Dialog Write
    0x30124A: [0xAF, 0x01], # Kai-man Write
    0x2F54F8: [0xB8,0x06], 0x2F5504: [0xB8,0x06], 0x2F5510: [0xB8,0x06], 0x2F551C: [0xB8,0x06], # TwinDrag Read
    0x2F5528: [0xB8,0x06], 0x2F5534: [0xB8,0x06], 0x2F5540: [0xB8,0x06], 0x2F554C: [0xB8,0x06], 0x2F5558: [0xB8,0x06], 
    0x3012E0: [0xAE,0x01], # TwinDrag Write
    0x46910: [0xD7],       # TwinDrag Read Spawn
    0x46060: [0xB0, 0x01], # Nucklz Read Spawn
    0x2F5630: [0xC0, 0x06], 0x2F563C: [0xC0, 0x06], 0x2F5648: [0xC0, 0x06], # Nucklz Read >> 2
    0x2F5654: [0xC0, 0x06], 0x2F5660: [0xC0, 0x06], 0x2F566C: [0xC0, 0x06],
    0x301034: [0xB0, 0x01], # Nucklz Write
    0x45DD0: [0xD8, 0x20], # Nucklz Prisoner Always On
    0x45ACC: [0xC7, 0x01], # Firekong Read
    0x2F51A4: [0x1C, 0x07], 0x2F51B0: [0x1C, 0x07], 0x2F51BC: [0x1C, 0x07], # Firekong Read
    0x2F51C8: [0x1C, 0x07], 0x2F51D4: [0x1C, 0x07], 
    0x4A24C: [0xC7, 0x01], # Firekong Write
    0x46CEC: [0xB2, 0x01], # Toughguy Read Spawn
    0x46D30: [0xB2, 0x01], # Toughguy Read Spawn
    0x2F5CC0: [0xC8, 0x06], 0x2F5CCC: [0xC8, 0x06], # Toughguy Read Minigame Start
    0x301962: [0xB2, 0x01], # Toughguy Write
    #0x31B260: [0xB2, 0x01], # Toughguy Not sure what
    0x300970: [0xB9,0x81], # P Beast Hatched Read
    0x48D68: [0x33, 0x20, 0x00, 0x1C], # Check for Egg
    0x22007F: [0x01, 0xB3], # P Beast Write
    0x46DBC: [0xDA], # PTeradon read spawn
    0x3019F6: [0xB4, 0x01], # Pteradon
    #0x2F5D20: [], # Pteradon
    0x46C24:  [0xB5, 0x01], # Dorako Spawn
    0x48D50:  [0xB5, 0x01], # Dorako Interact
    0x45620:  [0xB5, 0x01], # Dorako Prisoner
    0x3018BC: [0xB5, 0x01], # Dorako Write
    0x46D50:  [0xDC], # Youno Read Spawn
    0x48F26:  [0xDC, 0x20], # Youno Read
    0x3019AE: [0xB8, 0x01], # Youno Write
    0x4781C:  [0xB7, 0x01], # Sibaloon Read Spawn
    0x49B88:  [0xB7, 0x01], # Sibaloon Read Interact
    0x22110C: [0x01, 0xB7], # Sibaloon Read Dialog
    0x22132C: [0x01, 0xB7], # Sibaloon Read Dialog 2
    0x301C90: [0xB7, 0x01], # Sibaloon Write
    0x46F0C:  [0xB9, 0x01], # P animal Read Spawn
    0x301A70: [0xB9, 0x01], # P animal Read Write
    0x47290:  [0xBA, 0x01], # Unagi Read Spawn
    0x2F51E0: [0xE8, 0x06], 0x2F51EC: [0xE8, 0x06], 0x2F51F8: [0xE8, 0x06], 
    0x2F5204: [0xE8, 0x06], 0x2F5210: [0xE8, 0x06], # Unagi Read Interact
    0x301ABE: [0xBA, 0x01], # Unagi Write
    0x8156:   [0xDC], # Elekong Oasis Read
    0x47750:  [0xDC], # Elekong Read Spawn
    0x2F54B0: [0xF0, 0x06], 0x2F54BC: [0xF0, 0x06], 0x2F54C8: [0xF0, 0x06], 
    0x2F54D4: [0xF0, 0x06], # Elekong Read Interact
    0x301C06: [0xBC, 0x01], # Elekong Write
    0x4730C:  [0xDB], #Youni Read Spawn
    0x4954A:  [0xDB], #Youni Read Interact
    0x45654:  [0xDB], #Youni Prisoner
    0x301B60: [0xB6, 0x01], # Youni Write
    0x2F64F4: [0xF8, 0x06], 0x2F6500: [0xF8, 0x06], # KameKing Read
    0x302A70: [0xBE, 0x01], # Kameking Write
    0x46844:  [0xBF, 0x01], # Marigon Read Spawn
    0x2F55B8: [0xFC, 0x06], # Marigon Read Interact
    0x3012A0: [0xBF, 0x01], # Marigon Write

    # Fusion
    0x4AB14:  [
        0x68, 0x88, # LDRH R0, [R5, #$02]
        0xCB, 0xF7, 0x35, 0xFE # BL proc_readflag
        ],
    0x4AB5E: [0xA8, 0x79], # LDRB R0, [R5, #$06]
    
    0x30204E: [0xAB,0x01], # P Fangs Read
    0x302056: [0xB1,0x01], # P Sea Read
    0x30205E: [0xBB,0x01], # P Dragon Read
    0x302066: [0xBD,0x01], # SeaWing Read

    0x302050: [0xAB,0x01], # P Fangs Write
    0x302058: [0xB1,0x01], # P Sea Write
    0x302060: [0xBB,0x01], # P Dragon Write
    0x302068: [0xBD,0x01], # SeaWing Write

    0x302052: [0x03], # P Fangs Graphic
    0x30205A: [0x09], # P Sea Graphic
    0x302062: [0x0E], # P Dragon Graphic
    0x30206A: [0x15], # SeaWing Graphic
    
    # Repoint fusion materials text
    0x30202C: [
        0x00, 0x2A, 0x3C, 0x08,
        0x10, 0x2A, 0x3C, 0x08,
        0x20, 0x2A, 0x3C, 0x08,
        0x30, 0x2A, 0x3C, 0x08,
        0x40, 0x2A, 0x3C, 0x08,
        0x50, 0x2A, 0x3C, 0x08,
        0x60, 0x2A, 0x3C, 0x08,
        0x70, 0x2A, 0x3C, 0x08,
        ],
    #Dialog fixes
    0x0216531: [0xE0, 0x0D, 0x01,0xFF], # Set Pommy on Arrival and skip opening dialog
    0x22135E: [0xE0,0x03,0x01,0x66], # <setflag 0x166> For step counter

    # Bomb Sythesis
    0x30291C: [0x03,0x03], #Hold Bomb
    0x302924: [0x04,0x03], # Aqua Bomb
    0x30292C: [0x05,0x03], # Power Bomb
    0x302934: [0x06,0x03], # RC Bomb
    0x30293C: [0x07,0x03], # Landmine

    # Arcade
    0x49A5D: [0x60], # B Valley STR R1, [R0, #$00]
    0x49A9D: [0x60], # S Forest
    0x49ADD: [0x60], # Upsilon
    0x49B1D: [0x60], # Desert
    0x21C260: [0x79],# Medicine Trophy

    # Do not unset karabons passives
    0x6D1C: [0x79], # Sharkun
    0x6D22: [0x79], # Doroko



    # Other
    0x4BAA0: [0xE3,0x01], # Theta Reroute
     # Warp fixes
    0x2FCE02: [0x1E,0x00], # Magnet Door Scene
    0x2FD080: [0x50,0x00,0x1F,0x00], # Pretty Boat Scene
     # SID Chest
    0x2FBC50: [0x25, 0x00, 0x31, 0x00, 0x94, 0x00, 0x21, 0x07], # Magbase
    0x2FBE04: [0x07, 0x00, 0x45, 0x00, 0x94, 0x00, 0x22, 0x07], # PrettyBase
    0x2FC216: [0x43, 0x00, 0x51, 0x00, 0x94, 0x00, 0x23, 0x07], # PlasmaBase
    0x2FC6A2: [0x34, 0x00, 0x3D, 0x00, 0x94, 0x00, 0x24, 0x07], # GolemBase
     # Beta House SID Warp
    0x2FD8D8: [0x25, 0x00, 0x24, 0x00, 0x00, 0x03, 0x01, 0x00], # Inside Beta House -> Inside SID Room
    0x2FD920: [0x23, 0x00, 0x07, 0x00, 0x02, 0x00, 0x00, 0x00], # Inside SID Room -> Outside Beta House
}

Karabon_skip_set = [
    0x217697, # Ceedrun
    0x216E7A, # Elifan
    0x21900F, # Sharkun
    0x21A75C, # Th Liger
    0x219956, # Kai-man
    0x21A1F6, # Twindrag
    0x21A56A, # P Knuckz
    0x21E226, # Toughguy
    0x220118, # P Beast
    0x2207C4, # Pteridon
    0x21FFCE, # Dorako
    0x21F9E5, # Youno
    0x221471, # Sibaloon
    0x2215A8, # P Animal
    0x221B96, # Unagi
    0x2239CA, # Elekong
    0x222678, # Youni
    0x21A987, # Marigon
    0x222886, # KameKing
    0x216F6F, # Firekong
]

location_replace_txt = {
    # Items
    "L Forest - Ring Pickup": [0x21637E, 0x21638E, 9],
    "Alpha - Return Ring": [0x2161A6,0x2161B6,15],
    "Alpha - Camera": [0x21646F, 0x21647F, 11],
    "Alpha - Turn in Louie Photo": [0x2169C4, 0x2169D3,9],
    "ToPlain - Sampei Raindrop": [0x219AB2, 0x219AC2,10],
    "ToPlain - Sampei Return Fishhook": [0x219BB0, 0x219BC0, 15],
    "Beluga - Fish hook": [0x21A057, 0x21A04B, 10],
    "Ita - Purchased Beef": [0x21BCAA,0x21BCBA, 14],
    "Theta - Hammer": [0x21CA4C, 0x21CA5E, 7],


    # Karabons
    "ShuraRd - Ceedrun": [0x21761C, 0x21763E, 14],
    "Magnet - Elifan": [0x216C1E, 0x216DAA,14],
    "Omega - Unagi": [0x221AC9, 0x221AD9, 5],
    "ToPlain - Sharkun": [0x218FBB, 0x218F92, 15],
    "HighMt - Kai-man": [0x21980C, 0x219848, 15],
    "HighMt - TwinDrag": [0x21A191, 0x21A106, 9],
    "ColdSea - Firekong": [0x216EF3, 0x216ED4, 15],
    "Pretty - P Nucklz": [0x21A484, 0x21A469, 9],
    "LiteCave - Th Liger": [0x21A703, 0x21A6A3,9],
    "Pretty - MarinGon": [0x21A8B1, 0x21A833, 9],

    # Chest
    "LiteCave - Disinfectant Chest": [0x21C973, 0x21C983, 13],
    "Magnet - Crystal Chest": [0x21C87F, 0x21C893, 15],
    "Magnet - Silver Shoe Chest": [0x21C790, 0x21C7A0, 13],
    "Pretty - Crystal Chest": [0x21C8A7, 0x21C8BB, 12],
    "Pretty - Silver Armor Chest": [0x21C7B2, 0x21C7C2, 13],
    "Plasma - Crystal Chest": [0x21C8CC, 0x21C8E0, 14],
    "Plasma - Gold Shoes Chest": [0x21C7D4, 0x21C7E4, 11],
    "Golem - Crystal Chest": [0x21C8F4, 0x21C907, 13],
    "Golem - Gold Armor Chest": [0x21C7F4, 0x21C804, 11],
    #"Fantasy Crystal Chest": [0x21C919, 0x21C92D, 15],

    #Bomb Synthesis
    "Bomb Synthesis - Hold Bomb": [0, 0x31B182, 9],
    "Bomb Synthesis - Aqua Bomb": [0, 0x31B18C, 9],
    "Bomb Synthesis - Power Bomb": [0, 0x31B196, 9],
    "Bomb Synthesis - RC Bomb": [0, 0x31B1A0, 9],
    "Bomb Synthesis - Landmine": [0, 0x31B1AA, 9],

    # Fusions 
    "Beta - Fuse Fangs": [0,0x21C45A, 15],
    "Beta - Fuse Sea": [0,0x21C475, 13],
    "Beta - Fuse Dragon": [0, 0x21C48E,16],
    "Beta - Fuse SeaWing": [0,0x21C4AA,15],

    # Medals
    "Magnet - Magnet Clear": [0x21853D, 0x21854F,16],
    "Pretty - Pretty Clear": [0x21853D, 0x21A452,17],

    # Other
    "Alpha - Kid Challenge": [0x21727A, 0x21728A, 11],
    "L Forest - Basement Heart": [0x2168AA, 0x2168BA, 16],
    "Beta - Ralph's Challenge": [0x217057, 0x2170A1,15],
    "Wetwood - Heart": [0x21AAf1, 0x21AB02, 8],
    "Colosseum Streak": [0x21BF38, 0x21BCFD, 13]

}

dialog_skip = [
    0x0216531, #Intro
]

zone_lock = {
    0x4A582: [0x20], # Magnet Door
    0x4A7C4: [0xE1,0x01], # Water Gate
    0x4B46C: [0xE2,0x01], # Desert Gate
}


common_replace_txt = {
    0x21C768: "APItem", # BombUp!
    0x21C784: "APItem", # FireUp!
    0x21C82C: "APItem", # Heart!
    0x21C847: "AP Item       ",# Small Medicine!
    0x21C86B: "AP Item       ",# Large Medicine!
    

}

text_tbl = {
    " ":0x20,
    "!":0x21,
    "“":0x22,
    "#":0x23,
    "$":0x24,
    "%":0x25,
    "&":0x26,
    "'":0x27,
    "(":0x28,
    ")":0x29,
    "*":0x2A,
    "+":0x2B,
    ",":0x2C,
    "-":0x2D,
    ".":0x2E,
    "/":0x2F,
    "0":0x30,
    "1":0x31,
    "2":0x32,
    "3":0x33,
    "4":0x34,
    "5":0x35,
    "6":0x36,
    "7":0x37,
    "8":0x38,
    "9":0x39,
    ":":0x3A,
    ";":0x3B,
    "<":0x3C,
    ">":0x3E,
    "?":0x3F,
    "@":0x40,
    "A":0x41,
    "B":0x42,
    "C":0x43,
    "D":0x44,
    "E":0x45,
    "F":0x46,
    "G":0x47,
    "H":0x48,
    "I":0x49,
    "J":0x4A,
    "K":0x4B,
    "L":0x4C,
    "M":0x4D,
    "N":0x4E,
    "O":0x4F,
    "P":0x50,
    "Q":0x51,
    "R":0x52,
    "S":0x53,
    "T":0x54,
    "U":0x55,
    "V":0x56,
    "W":0x57,
    "X":0x58,
    "Y":0x59,
    "Z":0x5A,
    "[":0x5B,
    "]":0x5D,
    "^":0x5E,
    "_":0x5F,
    "`":0x60,
    "a":0x61,
    "b":0x62,
    "c":0x63,
    "d":0x64,
    "e":0x65,
    "f":0x66,
    "g":0x67,
    "h":0x68,
    "i":0x69,
    "j":0x6A,
    "k":0x6B,
    "l":0x6C,
    "m":0x6D,
    "n":0x6E,
    "o":0x6F,
    "p":0x70,
    "q":0x71,
    "r":0x72,
    "s":0x73,
    "t":0x74,
    "u":0x75,
    "v":0x76,
    "w":0x77,
    "x":0x78,
    "y":0x79,
    "z":0x7A,
    "{":0x7B,
    "|":0x7C,
    "}":0x7D,
    "~":0x7E,
}

KARA_FLAG_CHECK = [
    0xA8,0x01,0xA9,0x01,0xAA,0x01,0xAB,0x01,0xAC,0x01,0xAD,0x01,0xAF,0x01,0xAE,0x01,
    0xB0,0x01,0xB1,0x01,0xB2,0x01,0xB3,0x01,0xB4,0x01,0xB5,0x01,0xBB,0x01,0xB8,0x01,
    0xB7,0x01,0xB9,0x01,0xBA,0x01,0xBC,0x01,0xB6,0x01,0xBD,0x01,0xBE,0x01,0xBF,0x01,
    0xC7,0x01
]

SOUND_TBL = bytearray([
    0xB0, 0xCB, 0x31, 0x08, 0x00, 0x00, 0x00, 0x00, 0x9C, 0x7D, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xB8, 0x7D, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0xD8, 0x7D, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xF4, 0x7D, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x20, 0x7E, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xB0, 0x7E, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x0C, 0x7F, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x5C, 0x7F, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x80, 0x7F, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xA0, 0x7F, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0xBC, 0x7F, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x14, 0x80, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x30, 0x80, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x54, 0x80, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x70, 0x80, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x90, 0x80, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0xBC, 0x80, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x6C, 0x81, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0xFC, 0x81, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x78, 0x84, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x34, 0x86, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x18, 0x9C, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0xE0, 0x9C, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x48, 0x9E, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x40, 0xA2, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0xF0, 0xA9, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0xF0, 0xAA, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x20, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x34, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x3C, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x44, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x4C, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x54, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x5C, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x64, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x6C, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x74, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x7C, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x84, 0xAC, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0xC0, 0xAC, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0xE4, 0xAC, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x04, 0xAD, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x54, 0xAD, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x70, 0xAD, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x8C, 0xAD, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x20, 0xAE, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x40, 0xAE, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xFC, 0xAE, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x7C, 0xAF, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x9C, 0xAF, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0xBC, 0xAF, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xDC, 0xAF, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0xFC, 0xAF, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x40, 0xB0, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x5C, 0xB0, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x78, 0xB0, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x9C, 0xB0, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xB8, 0xB0, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x10, 0xB1, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xA4, 0xB1, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0xC8, 0xB1, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xE8, 0xB1, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x04, 0xB2, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x24, 0xB2, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x40, 0xB2, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x6C, 0xB2, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0xB0, 0xB2, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xD8, 0xB3, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x28, 0xB4, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x58, 0xB4, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x8C, 0xB4, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xFC, 0xB4, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x1C, 0xB5, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xD8, 0xB5, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0xFC, 0xB5, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0x24, 0xB6, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00, 0x44, 0xB6, 0x37, 0x08, 0x01, 0x00, 0x01, 0x00,
    0xB4, 0xCD, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0xC4, 0xCF, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x9C, 0xD4, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x8C, 0xE1, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x98, 0xEB, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x50, 0xF7, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00,
    0xB8, 0xFF, 0x37, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x94, 0x12, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00, 0x28, 0x1E, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x88, 0x23, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00, 0x4C, 0x2D, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00,
    0xD8, 0x35, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00, 0x3C, 0x36, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00,
    0xC8, 0x3F, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00, 0x18, 0x41, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00,
    0xA4, 0x42, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00, 0xE8, 0x4C, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x24, 0x52, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00, 0xA8, 0x55, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00,
    0xC0, 0x56, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00, 0xAC, 0x57, 0x38, 0x08, 0x00, 0x00, 0x00, 0x00,
])

sound_exclude = [0x00,0x14,0x15,0x16,0x17,0x18,0x19,0x1A,0x1B,0x1C,0x1D,0x1E,0x1F,0x20,0x21,0x22,
                 0x23,0x24,0x25,0x26,0x27,0x4E,0x4F,0x50,0x51,0x52,0x53,0x54,0x55,0x56,0x57,0x58,
                 0x59,0x5A,0x5B,0x5C,0x5D,0x5E,0x5F,0x60,0x61,0x62,0x63,]

music_exclude = [0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F,
                 0x10,0x11,0x12,0x13,0x28,0x29,0x2A,0x2B,0x2C,0x2D,0x2E,0x2F,0x30,0x31,0x32,0x33,
                 0x34,0x35,0x36,0x37,0x38,0x39,0x3A,0x3B,0x3C,0x3D,0x3E,0x3F,0x40,0x41,0x42,0x43,
                 0x44,0x45,0x46,0x47,0x48,0x49,0x4A,0x4B,0x4C,0x4D]

softlock_fixes = {
    0x6D422: [0x00,0x00],
}

object_rando_bytes = {
    0x2FB30C: [# Field Zone
        0x03, 0x01, 0x03, 0x03, 0x01, 0x01, 0x01, 0x02, 0xC2, 0x02, 0x02, 0x01, 0x03, 0x02, 0x02, 0x81, 0x01, 0xC1, 0x04, 0x81, 0x04, 0x04, 0x04, 0x04, 0xC1, 0x02, 0xC1, 0x81, 0x04, 0xC1, 
        0xC1, 0x04, 0x81, 0x01, 0x04, 0xC1, 0xC1, 0xC1, 0x04, 0x02, 0x02, 0x81, 0x02, 0x01, 0x02, 0x04, 0x02, 0x01, 0x04, 0x02, 0x02, 0x01, 0x02, 0x01, 0x01, 0x02, 0x01, 0x81, 0x04, 0x81,],
    0x2FB4EE: [# Beach Zone
        0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x09, 0x0B, 0x0B, 0x0A, 0x0A, 0x09, 0x0B, 0x09, 0xC3, 0x09, 0x09, 0x09, 0x09, 0xC3, 0xC3, 0x09, 0xC3, 0xC3, 0x09, 0x0B, 0xC3, 0x09, 0x0B, 0x09, 0x09,
        0xC3, 0x82, 0x0B, 0x09, 0x09, 0x0A, 0x09, 0x0B, 0xC3, 0xC3, 0x0B, 0x09, 0x09, 0xC3, 0x0A, 0x09, 0x09, 0xC3, 0xC3, 0x0B, 0x82, 0x0A, 0x0A, 0x0B, 0x09, 0x0B,],
    0x2FB6BA: [# BigOcean
        0x0C, 0x0D, 0x0D, 0x0C, 0x0D, 0x0D, 0x0D, 0x0D, 0x83, 0x83, 0x0D, 0x83, 0x0C, 0x83, 0x0D, 0x83, 0x83, 0x0D, 0x0D, 0x0C, 0x0C, 0x0D, 0x0D, 0x0C, 0x0D, 0x0D, 0x83, 0x0C, 0x0C, 0x83, 
        0x0D, 0x0D, 0x0C, 0x0D, 0x0C],
    0x2FB7D4: [# Snow Zone
        0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x8C, 0x16, 0x8B, 0x13, 0x13, 0x13, 0x16, 0x16, 0x16, 0x89, 0x13, 
        0x16, 0x16, 0x13, 0x13, 0x13, 0x13, 0x16, 0x16, 0x13, 0x89, 0x16, 0x13, 0x89, 0x89, 0x13, 0x12, 0x12, 0x12, 0x89, 0x12, 0x12,],
    0x2FB96E: [0x8B, 0x15, 0x14, 0x15, 0x15, 0x15, 0x15, 0x14, 0x15, 0x14, 0x15, 0x15, 0x15, 0x15, 0x89, ], # Frozen Palace
    0x2FB98E: [# Desert Zone
        0x1B, 0x1E, 0x1E, 0x1E, 0x1B, 0x1B, 0x1B, 0x1C, 0x1E, 0x1C, 0x1C, 0x1B, 0x8F, 0x1F, 0x1B, 0x1C, 0x1B, 0x8F, 0x8F, 0x1C, 0x8F, 0x1C, 0x1F, 0x1F, 0xC4, 0x8F, 0x8F, 0x1B, 0x1F, 0x1C, 
        0x1F, 0x1F, 0x1B, 0x1F, 0x8F, 0x1B, 0xC4, 0xC4, 0x1F, 0x1D, 0x1F, 0x1D, 0x1F, 0xC4, 0x1D, 0xC4, 0x1F, 0xC4, 0x8E, 0x1D, 0x1F, 0x1D, 0x1D, 0xC4, 0x8E, 0x1D, 0x1D, 0x1D,],
    0x2FBBD0: [#Magbase
        0x2C, 0x05, 0x08, 0x94, 0x08, 0x80, 0x05, 0x94, 0x07, 0x80, 0x80, 0x80, 0x07, 0x80, 0x80, 0x80, 0x80, 0x80, 0x05, 0x05, 0x05, 0x05, 0x07, 0x80, 0x80, 0xC0, 0x80, 0x07, 0x06, 0x07, 
        0x06, 0x06, 0x07, 0x80, 0x06, 0xC0, 0xC0, 0x94, 0x08, 0x80, 0x08, 0x80, 0x94, 0x08, 0x80, 0x07, 0x08, 0x07, 0x07, 0x08, 0x08, 0x07,],
    0x2FBDAC: [# Pretty Base
        0x85, 0x11, 0x88, 0x85, 0x11, 0x88, 0x94, 0x85, 0x88, 0x11, 0x85, 0x11, 0x88, 0x88, 0x86, 0x86, 0x86, 0x86, 0x86, 0x86, 0x86, 0x86, 0x86, 0x85, 0x86, 0x86, 0x86, 0x86, 0x94, 0x07, 
        0x87, 0x2D, 0x85, 0x87, 0x87, 0x87, 0x87, 0x85, 0x87, 0x87, 0x07, 0x85, 0x85, 0x11, 0x86, 0x85, 0x86, 0x0F, 0x86, 0x85, 0x85, 0x85, 0x0F, 0x07, 0x86, 0x86, 0x86, 0x86, 0x86, 0x85, 
        0x87, 0x85, 0x11, 0x86, 0x85, 0x85, 0x87, 0x0F, 0x0F, 0x86, 0x94, 0x94, 0x0E, 0x07, 0x07, 0x10, 0x86, 0x86, 0x86, 0x86, 0x86, 0x0E, 0x88, 0x88, 0x10, 0x0E, 0x07, 0x88, 0x10, 0x88, 
        0x86, 0x10, 0x10, 0x86, 0x86, 0x0E, 0x0E, 0x07, 0x07, 0x0E, 0x07, 0x86, 0x07, 0x07, 0x0E, 0x07, 0x0E, 0x86,],
    0x2FC10E: [#Plasma Base
        0x94, 0x8A, 0x8A, 0x17, 0x8A, 0x17, 0x17, 0x94, 0x8A, 0x8A, 0x18, 0x18, 0x18, 0x1A, 0x1A, 0x1A, 0x19, 0x8A, 0x8A, 0x19, 0x8A, 0x19, 0x8A, 0x8A, 0x19, 0x8A, 0x8A, 0x8A, 0x8A, 0x8A, 
        0x8A, 0x8A, 0x8A, 0x8A, 0x8A, 0x94, 0x8A, 0x8A, 0x17, 0x17, 0x8A, 0x2E, 0x8A, 0x18, 0x8A, 0x8A, 0x17, 0x18, 0x94, 0x1A, 0x19, 0x8A, 0x8A, 0x8A, 0x8A, 0x8A, 0x19, 0x1A, 0x8A,
        ],
    0x2FC324: [0x07, 0x07, 0x07, 0x90, 0x90,],# Oldbase
    0x2FC352: [# Golem Base
        0x94, 0x07, 0x93, 0x93, 0x93, 0x93, 0x93, 0x93, 0x93, 0x91, 0x91, 0x92, 0x91, 0x92, 0x92, 0x94, 0x93, 0x92, 0x91, 0x92, 0x92, 0x92, 0x92, 0x91, 0x91, 0x92, 0x92, 0x91, 0x91, 0x91, 
        0x91, 0x93, 0x93, 0x22, 0x93, 0x93, 0x22, 0x93, 0x93, 0x93, 0x22, 0x93, 0x93, 0x22, 0x93, 0x93, 0x22, 0x92, 0x91, 0xC5, 0x22, 0x93, 0x92, 0x91, 0x91, 0x92, 0x23, 0x93, 0xC5, 0x93, 
        0x93, 0x93, 0x94, 0x93, 0x22, 0x93, 0x92, 0x92, 0x93, 0x22, 0x92, 0x91, 0x91, 0xC5, 0xC5, 0x07, 0xC5, 0x94, 0xC5, 0x20, 0xC5, 0xC5, 0xC5, 0x21, 0xC4, 0x07, 0xC5, 0xC4, 0x21, 0x20, 
        0xC5, 0xC4, 0xC5, 0xC5, 0x20, 0xC4, 0xC5, 0x91, 0x91, 0xC5, 0xC5, 0x2F, 0x91, 0x91, 0x21, 0xC4, 0x91, 0x92, 0x21, 0xC5, 0x91, 0x91, 0xC5, 0x91, 0x91, 0x94, 0x94, 0x92, 0x07, 0xC4, 
        0x92, 0x92, 0x92, 0xC4, 0x92, 0x86, 0x86, 0x86, 0x86, 0xC5, 0xC5, 0xC5, 0xC4, 0x92, 0xC5, 0x91, 0x23, 0x91, 0x91, 0xC4, 0x91, 0x91, 0x91, 0x23, 0x91, 0x91, 0x23, 0x91, 0x91, 0x92, 
        0x92, 0x91, 0x91, 0xC4, 0xC5, 0x91, 0xC5, 0xC5, 0xC4, 0x91, 0xC4, 0x20, 0x20, 0xC5, 0xC5, 0x94, 0x91, 0x91, 0x20, 0x20, 0xC5, 0xC4, 0x91, 0xC4, 0xC5, 0xC5, 0xC5
        ],
    0x2FC8DC: [# Fantasy
        0x97, 0x98, 0x98, 0x97, 0x97, 0x97, 0x94, 0x98, 0x97, 0x98, 0x98, 0xC7, 0xC6, 0x85, 0x97, 0x85, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x97, 0xC6, 0x97, 0x24, 0x27, 0x25, 0x24, 0x94, 
        0x27, 0xC6, 0x24, 0x97, 0x27, 0xC6, 0xC7, 0x2B, 0x27, 0xC7, 0x94, 0x91, 0x91, 0x94, 0xC7, 0x85, 0x97, 0xC6, 0xC7, 0x97, 0x97, 0xC7, 0xC7, 0xC7, 0x97, 0x97, 0xC7, 0xC7, 0xC8, 0xC6, 
        0x91, 0x91, 0xC6, 0x97, 0x2A, 0x29, 0x29, 0xC7, 0xC7, 0xC6, 0x2A, 0xC6, 0xC6, 0xC8, 0xC8, 0x91, 0x85, 0x2A, 0x2A, 0x29, 0x85, 0x94, 0x91, 0xC7, 0xC7, 0x29, 0x29, 0x94, 0xC7, 0x96, 
        0xC6, 0x91, 0xC7, 0xC7, 0x91, 0xC7, 0x2B, 0x2B, 0xC6, 0x96, 0x91, 0xC7, 0x27, 0x2B, 0x91, 0x91, 0xC7, 0xC7, 0x2B, 0xC7, 0x96, 0x96, 0x25, 0x28, 0xC6, 0xC6, 0x28, 0x2A, 0x25, 0xC7, 
        0xC7, 0xC6, 0xC6, 0x28, 0x85, 0x94, 0x85
        ]
}

enemy_rando_types = [
    0x1, #Slime
    0x2, #Tree Enemy
    0x3, #Flower Trio
    0x4, #Balloon
    0x5, #Hedgehog
    0x6, #Zombie
    0x7, #Higehige
    0x8, #Snake
    0x9, #Red Slime
    #0x0A, #Invalid?? Causes lag spike
    0x0B, #Frog
    0x0C, #Crab
    0x0D, #Merman
    0x0E, #Lampslime
    0x0F, #Skeleton
    0x10, #Jellyfish
    0x11, #Drill Squid
    0x12, #Yellow Slime
    0x13, #Yeti
    0x14, #Icicle Monster
    0x15, #Seel
    0x16, #Ninja
    0x17, #Shade
    0x18, #Bow Armor
    0x19, #Spade Card
    0x1A, #Flying Devil
    0x1B, #Green Slime
    0x1C, #Living Rock
    0x1D, #Quicksand Worm ; Takes up too much sprite space
    0x1E, #Fire Tribesman
    0x1F, #Purple Devil
    0x20, #Mummy
    0x21, #Cloud
    0x22, #Mudhand
    0x23, #Spider
    0x24, #Sickle Wizard
    0x25, #Hige Gunman
    0x26, #Spikey Monster
    0x27, #Robot
    0x28, #Catapillar
    0x29, #Living Bomb
    0x2A, #Skullrock
    0x2B, #Blockbot
    #0x2C, #Magnet Bomber
    #0x2D, #Pretty Bomber
    #0x2E, #Plasma Bomber
    #0x2F, #Golem Bomber
    #0x30, #Brain bomber
]

fuse_items = ["Beta - Fuse Fangs", "Beta - Fuse Sea", "Beta - Fuse Dragon", "Beta - Fuse SeaWing"]
kara_list = [
    "Pommy",
    "Ceedrun",
    "Elifan",
    "P Fangs",
    "Sharkun",
    "Th Liger",
    "Kai-man",
    "TwinDrag",
    "P Nucklz",
    "P Sea",
    "ToughGuy",
    "P Beast",
    "Pteradon",
    "Dorako",
    "P Dragon",
    "Youno",
    "Sibaloon",
    "P Animal",
    "Unagi",
    "Elekong",
    "Youni",
    "SeaWing",
    "KameKing",
    "MarinGon",
    "Firekong",
    ]

bomber_colors = [
    # White
    [0x0E, 0x43, 0x00, 0x00, 0xCE, 0x39, 0xF7, 0x5E, 0xFF, 0x7F, 0x93, 0x19, 0xDC, 0x3E, 0x7A, 0x18, 0x7F, 0x52, 0x7C, 0x13, 0x86, 0x79, 0xB1, 0x7E, 0xB5, 0x56, 0xFF, 0x7F, 0x7A, 0x18, 0x7F, 0x52],
    # Black
    [0x0E, 0x43, 0x00, 0x00, 0x84, 0x10, 0x08, 0x21, 0xAD, 0x35, 0xB4, 0x21, 0xFD, 0x42, 0x7A, 0x18, 0x7F, 0x52, 0x7C, 0x13, 0x08, 0x21, 0x8C, 0x31, 0xB4, 0x21, 0xFD, 0x42, 0x7A, 0x18, 0x7F, 0x52],
    # Red
    [0x0E, 0x43, 0x00, 0x00, 0x4E, 0x0C, 0x74, 0x0C, 0xBE, 0x18, 0x93, 0x19, 0xDC, 0x3E, 0x28, 0x22, 0x4D, 0x37, 0x7C, 0x13, 0x96, 0x14, 0xBD, 0x18, 0x93, 0x19, 0xDC, 0x3E, 0x1E, 0x49, 0xFF, 0x6A],
    # Blue
    [0x0E, 0x43, 0x00, 0x00, 0xE5, 0x54, 0xA8, 0x69, 0x6B, 0x7E, 0x93, 0x19, 0xDC, 0x3E, 0xBA, 0x20, 0x7F, 0x52, 0x7C, 0x13, 0xA8, 0x69, 0x4A, 0x7E, 0x93, 0x19, 0xDC, 0x3E, 0xBA, 0x20, 0x7F, 0x52],
    # Magnet
    [0x0E, 0x43, 0x00, 0x00, 0x61, 0x34, 0xE3, 0x50, 0xA5, 0x61, 0xF7, 0x5E, 0xFF, 0x7F, 0xBC, 0x1A, 0x9F, 0x17, 0xBC, 0x1A, 0xE3, 0x50, 0xA5, 0x61, 0xCE, 0x39, 0xF7, 0x5E, 0xBC, 0x1A, 0x9F, 0x17],
    # Pretty
    [0x2D, 0x32, 0x00, 0x00, 0x35, 0x30, 0x5C, 0x55, 0x7F, 0x6A, 0x9D, 0x3E, 0x5F, 0x5F, 0x05, 0x0E, 0xE9, 0x32, 0xFF, 0x7F, 0x5C, 0x55, 0x7F, 0x6A, 0x9D, 0x3E, 0x5F, 0x5F, 0xBC, 0x1A, 0x9F, 0x17],
    # Plasma
    [0x11, 0x21, 0x00, 0x00, 0xA0, 0x01, 0x83, 0x02, 0x4A, 0x07, 0x93, 0x19, 0xDC, 0x3E, 0xE3, 0x50, 0x9F, 0x17, 0xBC, 0x1A, 0x83, 0x02, 0x4A, 0x07, 0xF7, 0x5E, 0xFF, 0x7F, 0x51, 0x04, 0xB8, 0x04],
    # Golem
    [0x2D, 0x32, 0x00, 0x00, 0xD7, 0x00, 0xBF, 0x01, 0xBF, 0x12, 0xC9, 0x5D, 0xB0, 0x6E, 0x40, 0x1A, 0x40, 0x1F, 0x9F, 0x17, 0xBF, 0x01, 0xBF, 0x12, 0xBF, 0x01, 0xBF, 0x12, 0xBF, 0x12, 0x9F, 0x17],
    # MAX
    [0x0E, 0x66, 0x00, 0x00, 0x84, 0x10, 0x08, 0x21, 0x6B, 0x2D, 0x93, 0x19, 0xDC, 0x3E, 0x54, 0x14, 0x19, 0x29, 0xBF, 0x02, 0x08, 0x21, 0x6B, 0x2D, 0x73, 0x4E, 0x18, 0x63, 0x47, 0x55, 0xB0, 0x6A],
    # Purple
    [0x0E, 0x43, 0x00, 0x00, 0x4B, 0x4C, 0xAF, 0x64, 0x12, 0x71, 0x93, 0x19, 0xDC, 0x3E, 0xBA, 0x20, 0x7F, 0x52, 0x7C, 0x13, 0xD0, 0x64, 0xF2, 0x70, 0x93, 0x19, 0xDC, 0x3E, 0xBA, 0x20, 0x7F, 0x52],
]
bomber_color_primaries = [
    # Classic
    [[0xCE,0x39, 0xF7,0x5E, 0xFF,0x7F],[0x86,0x79, 0xB1,0x7E]],
    # Black
    [[0x84,0x10, 0x08,0x21, 0xAD,0x35],[0x08,0x21, 0x8C,0x31]],
    # Magnet
    [[0x61, 0x34, 0xE3, 0x50, 0xA5, 0x61,],[0xE3, 0x50, 0xA5, 0x61,]],
    # Pretty
    [[0x35, 0x30, 0x5C, 0x55, 0x7F, 0x6A,],[0x5C, 0x55, 0x7F, 0x6A,]],
    # Plasma
    [[0xA0, 0x01, 0x83, 0x02, 0x4A, 0x07,],[0x83, 0x02, 0x4A, 0x07,]],
    # Golem
    [[0xD7, 0x00, 0xBF, 0x01, 0xBF, 0x12,],[0xBF, 0x01, 0xBF, 0x12,]],
    # MAX
    [[0x84, 0x10, 0x08, 0x21, 0x6B, 0x2D,],[0x08, 0x21, 0x6B, 0x2D,]],
    # Red
    [[0x4E, 0x0C, 0x74, 0x0C, 0xBE, 0x18,],[0x96, 0x14, 0xBD, 0x18,]],
    # Orange
    [[0x33, 0x09, 0xB9, 0x15, 0xFD, 0x15,],[0xB7, 0x15, 0x1D, 0x1E,]],
    # Yellow
    [[0x13, 0x0A, 0xD9, 0x1E, 0x7E, 0x27,],[0x97, 0x1E, 0x7E, 0x27,]],
    # Green
    [[0x00, 0x02, 0x81, 0x06, 0x21, 0x07,],[0x82, 0x0A, 0x23, 0x0F,]],
    # Mint
    [[0x8C, 0x32, 0x2F, 0x3F, 0xD2, 0x4B,],[0xEE, 0x3A, 0x91, 0x47,]],
    # Cyan
    [[0x65, 0x4E, 0xE7, 0x5E, 0xA8, 0x77,],[0xE7, 0x5E, 0x68, 0x6F,]],
    # Blue
    [[0xE5, 0x54, 0xA8, 0x69, 0x6B, 0x7E,],[0xA8, 0x69, 0x4A, 0x7E,]],
    # Purple
    [[0x4B, 0x4C, 0xAF, 0x64, 0x12, 0x71,],[0xD0, 0x64, 0xF2, 0x70,]],
    # Magenta
    [[0x73, 0x4C, 0x97, 0x5C, 0xBC, 0x70,],[0x76, 0x58, 0x9B, 0x6C,]],
    # Pink
    [[0x54, 0x3D, 0x99, 0x4D, 0xFE, 0x5D,],[0x77, 0x49, 0xDD, 0x59,]],
    # White
    [[0xCE, 0x39, 0xF7, 0x5E, 0xFF, 0x7F,],[0xD6, 0x5A, 0x9C, 0x73,]],
    # Brown
    [[0xA9, 0x04, 0xEC, 0x08, 0x30, 0x0D,],[0xEC, 0x08, 0x30, 0x0D]],
]

bomber_color_secondaries = [
    # Classic
    [0x7A,0x18,0x7F,0x52],
    # Green
    [0x28,0x22,0x4D,0x37],
    # Blue
    [0xA8,0x69,0x4A,0x7E],
    # Red
    [0x54,0x14,0x19,0x29],
    # Gold
    [0xBC,0x1A,0x9F,0x17],
    # Orange
    [0xB7,0x15,0x1D,0x1E],
    # Yellow
    [0x97,0x1E,0x7E,0x27],
    # Purple
    [0xAF,0x64,0x12,0x71],
    # Beige
    [0xB4,0x21,0xFD,0x42],
    # Brown
    [0xEC,0x08,0x30,0x0D],
    # White
    [0x73,0x4E,0x9C,0x73],
    # Black
    [0xC6,0x18,0x29,0x25],
    # Pink
    [0x99,0x4D,0xFE,0x5D],
]