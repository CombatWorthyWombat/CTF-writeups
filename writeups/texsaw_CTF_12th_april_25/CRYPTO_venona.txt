we are given the following:

a background to the challenge: "venona

You've been deployed on a classified reconnaissance mission deep in the jungles of Vietnam. After days of trekking through dense foliage, your team discovers an abandoned intelligence outpost that appears to have been hastily evacuated. As the team's cryptanalyst, you're tasked with investigating a small underground room containing what looks like a communication center. Among scattered papers and broken equipment, you find:

A peculiar reference table (see attached image) with alphabetic grid patterns Scattered papers with two plaintext messages and three encrypted messages.

Intelligence believes one of the three messages contains critical information about enemy operations.

flag format: texsaw{FLAG}"

and two files:

"MESSAGES.txt"
and
"DIANA.tiff"

the messages contains:

===== PLAINTEXT MESSAGES =====
-OPERATION BLUE EAGLE MOVING TO SECTOR FOUR STOP REQUEST EXTRACTION AT BLUE EAGLE
-AGENT SUNFLOWER COMPROMISED NEAR HANOI STOP ABORT MISSION COMPROMISED

===== ENCRYPTED MESSAGES =====
-RCPZURNPAQELEPJUJZEGAMVMXWVWCTBMHKNYEEAZVXQWVKGMRVWXDLCANHLGY
-FLPDBSBQIGBJECHMIOZGJMQONXJANFPQYQPWIIONYKNERKHIABLJTPTAOZMDGZUTAESK
-KDPRMZZKNBECTGTKMKQOWXKCHMVNDOPQXUWJJLECUCLBQKKVDXJNUEYFIDAGVIUG

the image is of some sort of encryption table

=================================================================

first impressions:

the picture looks a lot like an enigma settings sheet, but with out the plugboard or daily settings
its got the classic 5 character blocks in upper-case
DIANA.tiff could indicate an operation or a person, but unsure

VENONA i think was a WWII US decryption project of some sort -> check wikipedia
	- having looked it up, VENONA was a project to try and decrypt soviet OTP codes
	- a soviet company accidentally printed the same OPT codebooks 35k times (lmao)

the image could be a OTP then, given OTP is a substitution - there should be a 1->1 match between len(pt) and len(ct)
lets see which pts match to which cts from the MESSAGES.txt:

pt1: OPERATIONBLUEEAGLEMOVINGTOSECTORFOURSTOPREQUESTEXTRACTIONATBLUEEAGLE -> length of [68]
pt2: AGENTSUNFLOWERCOMPROMISEDNEARHANOISTOPABORTMISSIONCOMPROMISED        -> length of [61]

ct1: RCPZURNPAQELEPJUJZEGAMVMXWVWCTBMHKNYEEAZVXQWVKGMRVWXDLCANHLGY        -> length of [61]
ct2: FLPDBSBQIGBJECHMIOZGJMQONXJANFPQYQPWIIONYKNERKHIABLJTPTAOZMDGZUTAESK -> length of [68]
ct3: KDPRMZZKNBECTGTKMKQOWXKCHMVNDOPQXUWJJLECUCLBQKKVDXJNUEYFIDAGVIUG     -> length of [64]

assumption is ∴

pt1 -> ct2
pt2 -> ct1
flag pt -> ct3

======================================================================

the image is split into two sections:

one seems like the OTP, 5x19 5 char blocks
the other seems like a rotation reference
	- it seems like an atbash style reverse matching with offset

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Z Y X W V U T S R Q P O N M L K J I H G F E D C B A

simple script for working out the translation for a given atbash matching:

atbash_a_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
atbash_a_2 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"


print(len("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def translate(letter):
    if len(letter) > 1:
        print("one letter at a time pls")
    else:
        position = ord(letter) - ord("A")
        pt_letter = (atbash_a_1[(position):(position + 1)])
        ct_letter = (atbash_a_2[(position):(position + 1)])
        if pt_letter == letter:
            print(pt_letter,  "->", ct_letter, sep="")
        
translate("Z")

=========================================

the encryption process probably goes something like:

get your plaintext: "WE STRIKE AT DAWN"
split into 5 char chunks: "WESTR IKEAT DAWN"
match it to the OTP:

W E S T R │ I K E A T │ D A W N   -> pt
L F H H Y │ Z A H ? ? │ J R N X K -> OTP (i cant read two chars)

either [A]:
	- the pt char denotes an atbash lookup
	- the OTP char denotes which char to translate to
	
or [B]:
	- the OTP char denotes an atbash lookup
	- the pt char denotes which char to translate to

to try ->
for [A]:
	- the pt char is W
	- the OTP char is L
	- lookup table for W ->
	
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
D C B A Z Y X W V U T S R Q P O N M L K J I H G F E

so our ct char is -> S

for [B]:
	- the pt char is W
	- the OTP char is L
	- lookup table for L ->
	
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
O N M L K J I H G F E D C B A Z Y X W V U T S R Q P

so our ct char is -> S

ahh i feel dumb now, its a pairing where each letter is rotated in reverse from each end
and as 26/2 mod(2)≅0, if X -> Y, Y -> X

=========================================

lets test this with a ct/pt pair we have already:

p1 -> OTP -> ct2
first 5 blocks:

O P E R A │ T I O N B │ L U E E A │ G L E M O │ V I N G T <- pt1
L F F H Y │ Z A H ? ? │ J R N X K │ ? Y N F V │ K O Z A T <- OTP chars

O P E R A │ T I O N B │ L U E E A │ G L E M O │ V I N G T <- pt1
↓ ↓ ↓ ↓ ↓ │ ↓ ↓ ↓ ↓ ↓ │ ↓ ↓ ↓ ↓ ↓ │ ↓ ↓ ↓ ↓ ↓ │ ↓ ↓ ↓ ↓ ↓
A F P B B │ H R E ? ? │ F O I Y P │ ? Q I I Q │ U D N T N <- text passed through tables

should match:

F L P D B │ S B Q I G │ B J E C H │ M I O Z G │ J M Q O N <- ct2

which it doesn't... hmm

=====================================

maybe the OTP procedure was actaully followed, ie the first ciphertext used the first [x] chars on the OTP
then the next one started off from there onwards

the first ciphertext was:

RCPZURNPAQELEPJUJZEGAMVMXWVWCTBMHKNYEEAZVXQWVKGMRVWXDLCANHLGY
this corresponds to:
AGENTSUNFLOWERCOMPROMISEDNEARHANOISTOPABORTMISSIONCOMPROMISED

A G E N T │
L F F H Y │
↓ ↓ ↓ ↓ ↓ │
Z O Q F I │

ZOQFI != RCPZU - so thats not it either

=========================================

found the image online, the description says:
A format of one-time pad used by the U.S. National Security Agency, code named DIANA.
The table on the right is an aid for converting between plaintext and ciphertext using the characters at left as the key.

so lets ignore the atbash lookup tables for the moment, and just do regular modular addition for the OTP:

O P E R A │ T I O N B │ L U E E A │ G L E M O │ V I N G T <- pt1

L F F H Y │ Z A H ? ? │ J R N X K │ ? Y N F V │ K O Z A T <- OTP chars

this doesn't work either...

=============================================

lets try a different approach, lets revers the OTP from the pt/ct pairs we have to double check they are using the same OTP:

# created on Sat Apr 12 22:11:17 2025
# python 3
# utf-8
# @author: CombatWorthyWombat

# OTP generator from chosen pt/ct pair

def pos(letter):
    return ord(letter) - ord('A')

def from_pos(pos):
    return chr(pos + ord('A'))

def find_otp(pt, ct):
    otp_chars = []
    for p_char, c_char in zip(pt, ct):
        pt_val = pos(p_char)
        ct_val = pos(c_char)
        otp_val = (ct_val - pt_val) % 26
        otp_chars.append(from_pos(otp_val))
    return ''.join(otp_chars)

pt_1 = "AGENTSUNFLOWERCOMPROMISEDNEARHANOISTOPABORTMISSIONCOMPROMISED"
ct_1 = "RCPZURNPAQELEPJUJZEGAMVMXWVWCTBMHKNYEEAZVXQWVKGMRVWXDLCANHLGY"

pt_2 = "OPERATIONBLUEEAGLEMOVINGTOSECTORFOURSTOPREQUESTEXTRACTIONATBLUEEAGLE"
ct_2 = "FLPDBSBQIGBJECHMIOZGJMQONXJANFPQYQPWIIONYKNERKHIABLJTPTAOZMDGZUTAESK"

OTP_1 = "RWLMBZTCVFQPAYHGXKNSOEDIUJRWLMBZTCVFQPAYHGXKNSOEDIUJRWLMBZTCVFQPAYHG"

otp = find_otp(pt_1, ct_1)
print("OTP for 1st pair:", otp)
otp = find_otp(pt_2, ct_2)
print("OTP for 2nd pair:", otp)

====================================

this outputs:
OTP for 1st pair: RWLMBZTCVFQPAYHGXKNSOEDIUJRWLMBZTCVFQPAYHGXKNSOEDIUJRWLMBZTCV
OTP for 2nd pair: RWLMBZTCVFQPAYHGXKNSOEDIUJRWLMBZTCVFQPAYHGXKNSOEDIUJRWLMBZTCVFQPAYHG

so the OTP is not the one in the picture... what a red herring

well, given for each char in pt, ct:
	(pt + OTP) % 26 = ct
	(ct - OTP) % 26 = pt
	
modifying our OTP finder script we get a decrypt function:

def decrypt_ct(ct, otp):
    pt_chars = []
    for c_char, o_char in zip(ct, otp):
        ct_val = pos(c_char)
        otp_val = pos(o_char)
        pt_val = (ct_val - otp_val) % 26
        pt_chars.append(from_pos(pt_val))
    return ''.join(pt_chars)

ct_3 = "KDPRMZZKNBECTGTKMKQOWXKCHMVNDOPQXUWJJLECUCLBQKKVDXJNUEYFIDAGVIUG"
OTP = "RWLMBZTCVFQPAYHGXKNSOEDIUJRWLMBZTCVFQPAYHGXKNSOEDIUJRWLMBZTCVFQP"

print("pt_3: ", (decrypt_ct(ct_3, OTP)))

as len(pt_3) = 64
and len(otp we recovered) = 68

we need to trim the otp to meet a 64 char limit

when we do that we get:
THEFLAGISWONTIMEPADWITHUNDERSCORESBETWEENWORDSWRAPPEDINTHEHEADER (finally xD)

====================================

okay, wrapping the flag as it comes above doesnt work
	- THE FLAG IS WON TIME PAD WITH UNDER SCORES BETWEEN WORDS WRAPPED IN THE HEADER
	- try texsaw{WON_TIME_PAD}
	
eyy that worked - took me longer than it should have...
	
