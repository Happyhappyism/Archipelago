mon_pal_offsets = {
    0x5bf00: 0x5bff8,
    0x7bf00: 0x7bff8,
    0x8bf00: 0x8bff8,
    0xdba80: 0xdbb78,
    0xdc100: 0xdc5f8,
    0xdc700: 0xdc768,
    
    0xabf00: 0xabff8,
    0xdb780: 0xdba78,
    0xdbd80: 0xdbe68,
}


field_pal_data = {
0x3: [0xdc98e, 0xdca8e],
0x4: [0xdc9ce, 0xdc9fe],
0x10: [0xdc894, 0xdc914, 0xdca14, 0xdcb24, 0xdcba4, 0xdcc14, 0xdcc94, 0xdcf14],
0x15: [0xdc9cc, 0xdc9fc],
0x1b: [0xdca1c, 0xdca4c, 0xdcc5c],
0x1d: [0xdcae4, 0xdcbe4, 0xdcc0c, 0xdcc24, 0xdcc2a, 0xdcc6c, 0xdcc74],
0x1f: [0xdc892, 0xdc912, 0xdc98c, 0xdc99c, 0xdc9a4, 0xdc9ac, 0xdc9b4, 0xdc9bc, 0xdca12, 0xdca8c, 0xdca9c, 0xdcaa4, 0xdcb22, 0xdcb34, 0xdcba2, 0xdcc12, 0xdcc92, 0xdcd0a, 0xdcd3c, 0xdcd62, 0xdcdbc, 0xdcde2, 0xdce64, 0xdce94, 0xdce9c, 0xdcea4, 0xdcec6, 0xdcecc, 0xdced6, 0xdcefc, 0xdcf12, 0xdcf84, 0xdcf8c, 0xdcf94, 0xdcfcc, 0xdd0b4, 0xdd104, 0xdd112],
0x45: [0xdc9ee],
0x82: [0xdc97e],
0x8a: [0xdc9de],
0xc0: [0xdcfb8, 0xdcfba, 0xdcfbc, 0xdcfbe, 0xdcfd8, 0xdcfda, 0xdcfdc, 0xdcfde, 0xdcfe0, 0xdcfe2, 0xdcfe4, 0xdcfe6, 0xdcfe8, 0xdcfea, 0xdcfec, 0xdcfee, 0xdcff0, 0xdcff2, 0xdcff4, 0xdcff6, 0xdcff8, 0xdcffa, 0xdcffc, 0xdcffe],
0xca: [0xdcb56],
0xe0: [0xdc9e6],
0xef: [0xdcc8c],
0xf7: [0xdccdc],
0xfb: [0xdc88c],
0x10d: [0xdcf4c],
0x10f: [0xdc91c, 0xdcb1c, 0xdcb9c, 0xdcc1c],
0x11f: [0xdcd12, 0xdce0c, 0xdce44],
0x139: [0xdcccc],
0x156: [0xdce1c],
0x1a3: [0xdc97c],
0x21f: [0xdcc72, 0xdcc8a, 0xdcd1a],
0x25a: [0xdce14],
0x25d: [0xdcd3a, 0xdcd4c, 0xdcdba, 0xdcdcc],
0x265: [0xdc9e4],
0x278: [0xdcf4a],
0x29f: [0xdc9ea, 0xdd102],
0x2b6: [0xdce04],
0x2bb: [0xdcacc, 0xdcbcc],
0x2c0: [0xdce84, 0xdce8c],
0x2df: [0xdc9dc],
0x2fa: [0xdce54],
0x31f: [0xdcd22],
0x320: [0xdd114],
0x35f: [0xdcb54],
0x39f: [0xdcae2, 0xdcbe2, 0xdcc02, 0xdcc0a],
0x3bf: [0xdc91a, 0xdcb1a, 0xdcb9a, 0xdcc1a, 0xdce0a, 0xdce12, 0xdce1a, 0xdce42, 0xdce4c, 0xdce9a, 0xdceca, 0xdced4, 0xdcf82, 0xdcf9a, 0xdcfc4],
0x3f8: [0xdc98a, 0xdc9a8, 0xdca8a],
0x3ff: [0xdcc52, 0xdccda, 0xdcd2a],
0x47a: [0xdcabc],
0x602: [0xdcab4],
0x804: [0xdc96e],
0x80d: [0xdc95e],
0x97b: [0xdcc54],
0xb53: [0xdc97a],
0xe77: [0xdcafe, 0xdcbfe],
0x104d: [0xdc96c],
0x109f: [0xdc884, 0xdc984, 0xdca04, 0xdca84, 0xdcb04, 0xdcb84, 0xdcc84, 0xdcf04, 0xdd084],
0x10bf: [0xdc8c4, 0xdc9c4, 0xdca44, 0xdcac4, 0xdcb44, 0xdcbc4, 0xdccc4, 0xdcf44, 0xdd0c4],
0x11a0: [0xdc90c, 0xdcb14, 0xdcb94],
0x131e: [0xdc88a],
0x13bf: [0xdcd38, 0xdcd4a, 0xdcdb8, 0xdcdca],
0x13fc: [0xdd088],
0x14a5: [0xdcd06, 0xdcd3e, 0xdcd56, 0xdcd86, 0xdcdbe, 0xdcdd6],
0x14f8: [0xdcbbc],
0x1897: [0xdcb4c],
0x18df: [0xdcd8c, 0xdcd94, 0xdcd9c, 0xdcda4, 0xdcdac, 0xdcdc4],
0x2004: [0xdc94e],
0x2108: [0xdc89c, 0xdc8a4, 0xdc8ac, 0xdc8b4, 0xdc8bc, 0xdc8e4, 0xdc8ec, 0xdc8f4, 0xdc8fc, 0xdc924, 0xdc92c, 0xdc934, 0xdc93c, 0xdc944, 0xdc954, 0xdc964, 0xdc974, 0xdca24, 0xdca2c, 0xdca34, 0xdca3c, 0xdca5c, 0xdca64, 0xdca6c, 0xdca74, 0xdca7c, 0xdcaac, 0xdcadc, 0xdcaec, 0xdcb2c, 0xdcb3c, 0xdcb64, 0xdcb6c, 0xdcb7c, 0xdcbac, 0xdcbdc, 0xdcbec, 0xdcc7c, 0xdcc9c, 0xdcca4, 0xdccac, 0xdccb4, 0xdccbc, 0xdcce4, 0xdccec, 0xdccf4, 0xdccfc, 0xdcf1c, 0xdcf24, 0xdcf2c, 0xdcf34, 0xdcf3c, 0xdcf5c, 0xdcf6c, 0xdcf74, 0xdcf7c, 0xdd094, 0xdd09c, 0xdd0a4, 0xdd0ac, 0xdd0bc, 0xdd0cc, 0xdd0dc, 0xdd0ec, 0xdd0f4, 0xdd0fc],
0x225f: [0xdca1a, 0xdca4a, 0xdcc5a],
0x231b: [0xdcafc, 0xdcbfc],
0x255f: [0xdc96a],
0x27df: [0xdce02],
0x294a: [0xdd140],
0x297f: [0xdc8cc, 0xdcc64],
0x29a5: [0xdca0c],
0x2a9b: [0xdcab2, 0xdcbba],
0x2cc6: [0xdcf0c],
0x2cf7: [0xdc95c],
0x2d6b: [0xdce5c, 0xdceac, 0xdd004, 0xdd04c],
0x2fff: [0xdce52],
0x340b: [0xdcc34],
0x35bf: [0xdc99a, 0xdc9ba, 0xdca9a],
0x35ff: [0xdc9fa],
0x36e4: [0xdc90a, 0xdcb12, 0xdcb92, 0xdcc22],
0x394c: [0xdcb5c],
0x39ce: [0xdcd04, 0xdcd54, 0xdcd84, 0xdcdd4],
0x3a40: [0xdc9f4, 0xdcaf4, 0xdcb74, 0xdcbf4],
0x3c1f: [0xdcc32],
0x3ca4: [0xdd08c],
0x3dbf: [0xdcb4a],
0x3def: [0xdc904],
0x4088: [0xdc94c],
0x41ff: [0xdc9ec],
0x435f: [0xdccca],
0x43df: [0xdcafa, 0xdcbfa],
0x4bf2: [0xdc9e2],
0x4def: [0xdcc42],
0x4e7f: [0xdce92, 0xdcec4, 0xdcefa],
0x516b: [0xdc8dc],
0x5294: [0xdc89a, 0xdc8a2, 0xdc8aa, 0xdc8b2, 0xdc8ba, 0xdc8c0, 0xdc8d0, 0xdc8e0, 0xdc8ea, 0xdc8f0, 0xdc8fa, 0xdc922, 0xdc92a, 0xdc932, 0xdc93a, 0xdc940, 0xdc950, 0xdc960, 0xdc970, 0xdc9d0, 0xdc9e0, 0xdc9f0, 0xdca22, 0xdca2a, 0xdca32, 0xdca3a, 0xdca40, 0xdca50, 0xdca5a, 0xdca60, 0xdca62, 0xdca6a, 0xdca70, 0xdca72, 0xdca7a, 0xdcaaa, 0xdcaf0, 0xdcb2a, 0xdcb3a, 0xdcbaa, 0xdcc7a, 0xdcc9a, 0xdcca2, 0xdccaa, 0xdccb2, 0xdccba, 0xdccc0, 0xdccd0, 0xdcce0, 0xdcce2, 0xdccea, 0xdccf0, 0xdccf2, 0xdccfa, 0xdcd50, 0xdcdd0, 0xdcf1a, 0xdcf22, 0xdcf2a, 0xdcf32, 0xdcf3a, 0xdcf40, 0xdcf50, 0xdcf5a, 0xdcf60, 0xdcf6a, 0xdcf70, 0xdcf72, 0xdcf7a, 0xdcfc0, 0xdcfd0, 0xdd092, 0xdd09a, 0xdd0a2, 0xdd0aa, 0xdd0ba, 0xdd0c0, 0xdd0ca, 0xdd0d0, 0xdd0da, 0xdd0e0, 0xdd0ea, 0xdd0f0, 0xdd0fa],
0x530a: [0xdca0a],
0x5567: [0xdcbb4],
0x55ef: [0xdcf0a],
0x56b5: [0xdc9c0, 0xdcac0, 0xdcaca, 0xdcad0, 0xdcae0, 0xdcb40, 0xdcb50, 0xdcb60, 0xdcb70, 0xdcbc0, 0xdcbca, 0xdcbd0, 0xdcbe0, 0xdcbf0, 0xdceaa, 0xdd144],
0x5800: [0xdcc2c],
0x5a7f: [0xdc9ca],
0x5ad6: [0xdce5a, 0xdd002, 0xdd044],
0x5ef7: [0xdcd02, 0xdcd82],
0x63f7: [0xdcf92, 0xdcfaa, 0xdcfb4],
0x66bf: [0xdc95a],
0x67bf: [0xdc918],
0x67e0: [0xdc9f2, 0xdcaf2, 0xdcb72, 0xdcbf2],
0x6980: [0xdcf8a, 0xdcf9c, 0xdcfa4, 0xdcfac],
0x6a94: [0xdc8ca, 0xdc8da, 0xdcc62],
0x6ad8: [0xdcb5a],
0x6bfa: [0xdc908],
0x6d29: [0xdcd0c, 0xdcd14, 0xdcd1c, 0xdcd24, 0xdcd2c, 0xdcd44],
0x6eb5: [0xdc8d4, 0xdca54, 0xdcad4, 0xdcbd4, 0xdccd4, 0xdcf54, 0xdd0d4],
0x6ef7: [0xdce62, 0xdcfd4],
0x6f67: [0xdce82, 0xdce8a],
0x777f: [0xdc900, 0xdc920, 0xdc928],
0x7c00: [0xdcd8a, 0xdd10c],
0x7c1d: [0xdd0e4],
0x7c1f: [0xdc9a2, 0xdc9aa, 0xdc9d4, 0xdcaa2, 0xdcc44, 0xdcc4c, 0xdcf64, 0xdd118, 0xdd11a, 0xdd11c, 0xdd11e, 0xdd120, 0xdd122, 0xdd124, 0xdd126, 0xdd128, 0xdd12a, 0xdd12c, 0xdd12e, 0xdd130, 0xdd132, 0xdd134, 0xdd136, 0xdd138, 0xdd13a, 0xdd13c, 0xdd13e],
0x7d00: [0xdcd92],
0x7d60: [0xdc994, 0xdca94, 0xdcb0c, 0xdcb8c, 0xdcc04, 0xdcc3c, 0xdcc6a],
0x7d90: [0xdc94a],
0x7dad: [0xdc9b2, 0xdcb32, 0xdd0b2],
0x7dc8: [0xdd08a],
0x7e00: [0xdcd9a],
0x7e25: [0xdcaba],
0x7e8d: [0xdc882, 0xdc982, 0xdca02, 0xdca82, 0xdcb02, 0xdcb82, 0xdcc82, 0xdcf02, 0xdd082],
0x7e8f: [0xdcbb2],
0x7e94: [0xdcfa2, 0xdcfb2],
0x7ec0: [0xdd10a],
0x7ef7: [0xdcea2],
0x7f00: [0xdcda2],
0x7f2b: [0xdc992, 0xdca92, 0xdcb0a, 0xdcb8a, 0xdcc3a],
0x7f3f: [0xdcc4a, 0xdcf62],
0x7fb9: [0xdc910],
0x7fdd: [0xdcab0, 0xdcab8],
0x7fe0: [0xdcdaa],
 }