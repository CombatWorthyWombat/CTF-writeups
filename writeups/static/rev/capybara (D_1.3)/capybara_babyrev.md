we get the following:

"You’ve just run across an old program, seemingly innocent at first. It asks for a password, and if you enter it correctly, you might think you've won. But there's more lurking beneath the surface. Something about this challenge doesn’t add up.

The program not only demands the correct password, but also a secret code—one that isn’t easily discovered. Is it hidden within the code? Or perhaps something you’ll have to figure out for yourself?

Resources
If it's your first reverse challenge, this website should be helpful https://dogbolt.org/ this website tries to decompile the program for you. Other popular tool is ghidra https://ghidra-sre.org/"

========================================================

lets run it and see what we get:

Welcome to baby rev challenge
Input the password:

100
Input the secret code now:

100
Wrong code!

========================================================

scanning the listing view you encounter "CTFlearn{\naughty naughty naughty using strings are..."

little easter egg :)

once the variable names are made more human-readable we get capybara_babyrev.png

it seems like only once you've put in both password/code will the check occur

the correct password seems to be a hardcoded string: ""Sup3rS3cr3tP455W0rd\n"
and the correct code seems to be: "0x539" which is 1337 in dec

when we put these two into the program when prompted, we are displayed the flag:
================
Correct!
Here is your flag

CTFlearn{W4s_1T_Th4T_H4rd?}
================

nice, we got there pretty quickly actually
CWW
