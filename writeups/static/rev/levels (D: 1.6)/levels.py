# Author: CWW
# 02/07/2025
# python utf-8
# script to try and reverse levels rev challenge

lv1_string = "34111"

def gen_lv2_string(string):
    result_1 = []
    result_2 = ""
    for char in string:
        x = (ord(char) - 48) * 2
        x = x + 48
        result_1.append(x)
    for i in result_1:
        c = chr(i)
        result_2 = result_2 + c
        
    return result_2


print(gen_lv2_string(lv1_string))