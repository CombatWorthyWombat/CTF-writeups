from sympy import gcd
from Crypto.Util.number import long_to_bytes, inverse

# Given parameters
n = 30392456691103520456566703629789883376981975074658985351907533566054217142999128759248328829870869523368987496991637114688552687369186479700671810414151842146871044878391976165906497019158806633675101
e = 65537
ciphertext = int("0x3939dad4ba6dfe1d4c203e9c2acfde66493cac762d80114c7f740af92268725b7b16afd060594dd0153b26d7651be7e50061a4149d718e5b51305925dfb237844ee231d418e005aaa0701297c79e9a5e144ab0", 16)

# Observed decryption outputs
correct_decryption = int("0x33dae9999b9e9b19b88572c7075c49bcb7577f8eee2b2a1d02d29f00bc9a7161bc676a7c3abbd105eb002791e49ede11c79cb678f72fd3926a0fab04bb9aac31bcebcb4f9a4f7e79a6627aeeda597311bf5b4d", 16)
faulty_decryptions = [
    int("0x10db635c8df8f5fcef00a410ce669256dcbac7a350d2830b87d6ceaaf20c9ea5d4237c8939a34dbf3b34c6ccc50217d13fcf0489465cb96b19bdb502b59411824574d280f62c17c0e27212dd18a8cd69d7633c", 16),
    int("0x296cc73617575eae7c3931cb6df65bc9919321ea09a63f6af7efd3897ddf3fb0336ab2c7d10162e02a7d0b20b0f6dd7f2514773b626df0a4269e75feff15cf9382987fe78fcda2315369acd676525582f2fcd6", 16)
]

def bellcore_attack(n, correct_dec, faulty_dec):
    diff = abs(correct_dec - faulty_dec)
    p = gcd(n, diff)
    if p != 1 and p != n:
        q = n // p
        return p, q
    return None, None

p, q = None, None
for faulty_dec in faulty_decryptions:
    p, q = bellcore_attack(n, correct_decryption, faulty_dec)
    if p and q:
        print(f"Factors found: p = {p}, q = {q}")
        break

if not p or not q:
    raise ValueError("Attack failed to find valid factors for n")

phi = (p - 1) * (q - 1)
d = inverse(int(e), int(phi))

m = pow(ciphertext, d, n)

decrypted_message = hex(m)[2:]
print(bytes.fromhex(decrypted_message).decode('utf-8'))