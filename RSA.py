import math

#https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python

toAlphabet = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y',
    26: 'Z'
}

def factorize(x):
    factors = []
    while x % 2 == 0:
        factors.append(2)
        x //= 2
    f = 3
    while f <= math.sqrt(x):
        if x % f == 0:
            factors.append(f)
            x //= f
        else:
            f += 2
    if x > 1:
        factors.append(x)
    return factors

def dValue(p, q, e):
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return d

n = 712446816787
e = 6551
ciphertext = 273095689186

#factor the given n value with the factorize algorithm
factors = factorize(n)
#print(factors)

#compute the d value
d = dValue(factors[0], factors[1], e)

#determine the public key with given formula
public = pow(ciphertext, d, n)

separatedNumbers = []
plaintext = ''
toString = str(public)

#separate the overall number into number values of two digits given the coding scheme A =01, B= 02 etc, [15, 14, 05]
#add to the list
for i in range(0, len(str(public)), 2):
    separatedNumbers.append(int(toString[i:i+2]))

#print(separatedNumbers)

#compare each of the digits in the list to the dictionary, there is no way to put 01 as an integer in dictionary
#add it to the string variable
for d in separatedNumbers:
    plaintext = plaintext + toAlphabet[d]

print("The plaintext is: ", plaintext)






