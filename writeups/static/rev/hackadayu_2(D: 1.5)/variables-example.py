# Author: CWW
# 02/07/2025
# UTF-8
# Fixed script for reversing 'variables-examples' binary from HackadayU 2

XorMe = 0xDEADBEEFFACECAFE
globalVar = "KeYpress"

def extract_bytes_from_int(val, num_bytes=8):
    return [(val >> (i * 8)) & 0xFF for i in range(num_bytes)]

def gen_keypass(xor_int, global_str):
    keycode = ""
    xor_bytes = extract_bytes_from_int(xor_int)

    for i in range(8):
        xor_byte = xor_bytes[i]
        global_ord = ord(global_str[i])
        val = (xor_byte + global_ord + 1) & 0xFF
        keycode += chr(val)

    return keycode

keypass = gen_keypass(XorMe, globalVar)

print("Generated keypass:", keypass)

