we are given the following:

"This is a simple CrackMe for Linux x86\_64. 
The goal is to find the correct serial that allows access. 
No packers or anti-debug tricks are used. 
Compiled with GCC. 
Enjoy and good luck :)"

========================================================

taking a look at the program:

Enter your serial: 100
Access Denied! Invalid Serial.

looks like we need to find ourselves a valid serial

========================================================

in ghidra, the main function simply checks if the user submitted serial satisifes a "check\_serial" function

this is as seen in check\_serial.png (after renaming variables)

the serial needs to be of length 8

and is checked using a "transform" function, which mutates the user_serial_guess
local\_38 = [0x58, 0x6e, 0x60, 0x6b, 0x7b, 0x56, 0x66, 0x75]
if the user\_serial\_guess[x] == local\_38[x] - then return 0 and set uVar2 = 1 (which is our success condition bool)

the transform function, however, is as seen in transform.png

in our case, param\_1 is the user\_serial\_guess[x], and param\_2 is x
        return ((int)param_1 ^ param_2 + 7U) + 0xd & 0x7f;

say our counter = 0
our unknown is our serial[0]

local_38[0] = (serial[0] ^ 0 + 7U) + 0xd & 0x7f
/// 7U is an unsigned integer 7, 200U would be an unsigned integer 200

88 = (serial[0] ^ [0] + 7) + (13 bitwise\_and 127)
88 = (serial[0] ^ 7) + 13
75 = (serial[0] ^ 7)
75 ^ 7 = serial[0]
serial[0] = 76

so our serial would look like: serial[0x4c, ?, ?, ?, ?, ?, ?, ?]

the generalised formula is:
for 0 -> 7 as count:
local\_38[count] - 13) ^ (count + 7) = serial[count]

generalising this to a script - as seen in vulnix_easyjerk.py
gets us the result: LiZTeETf

========================================================

Enter your serial: LiZTeETf
Access Granted! Welcome!

nice - we got it!
CWW
