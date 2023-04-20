import math

p = int("00fb2e8473c499d184d806e6b5df7f621b", 16)
alice = int("2ca50afea541f0d90f68e0efc85c2686", 16)
bob = int("6e146d3b2149f41450713e5c83d21e70", 16)
g = 2

# calculate A = g^a mod p and B = g^b mod p
A = pow(g, alice, p)
B = pow(g, bob, p)

# s = B^a mod p = A^b mod p
s1 = pow(B, alice, p)
s2 = pow(A, bob, p)

shared_key1 = hex(s1)[2:]  # Remove '0x' prefix from hex string
shared_key2 = hex(s2)[2:]  # Remove '0x' prefix from hex string

# get the bit count 
print("Bit count of p:", int(math.log2(p)))


print("Shared key A :", shared_key1)
print("Shared key B :", shared_key2)