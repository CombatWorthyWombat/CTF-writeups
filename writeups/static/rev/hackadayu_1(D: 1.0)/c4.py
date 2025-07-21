# Author: CWW
# 09/07/2025
# python utf-8
# script to parse byte values for string

string = "hackaday-u"

def add_two(string):
    result = ""
    for char in string:
        x = ord(char)
        x = x + 2
        y = chr(x)
        result = result + y
    
    return result
        
if __name__ == "__main__":
    password = add_two(string)
    print(password)