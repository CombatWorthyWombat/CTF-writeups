turn the binary to an executable: chmod +x minruaf_linux

prompted to enter some digits,
when you do that - it prompts you to enter some more digits

unless you enter the correct digits, the program restarts from the beginning

when decompiled and variables renamed, as in the png - the operation becomes a little more transparent
when you enter the first number, it has the following operation done to it:

        * 0x14 + 4

so the number is times by 20, then has 4 added

so for 10:

10
204

this combination lets us in
crackme solved :)
CWW
