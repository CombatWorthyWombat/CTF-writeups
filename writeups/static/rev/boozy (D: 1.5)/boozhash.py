# Author: CWW
# 01/07/2025
# python utf-8
# script to recreate the boozhash function

user_input = "username"

def boozhash(string):
    x = 0
    for char in string:
        x = (x + ord(char)) * 1025
        x = x ^ (x >> 6)
    
    hash_value = (x * 9) ^ ((x * 9) >> 11)
    return hash_value

print(boozhash(user_input))