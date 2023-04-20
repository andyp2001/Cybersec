
# set the plaintext
plaintext = input("Please enter the plaintext: ") # ask for user input (word/phrase)
# set the cyphertext
key = input("Please enter the key: ") # ask for user input (word/phrase)


# The key is used to initialize a permutation of all possible bytes (0 to 255) in a 256-byte array called the state table.
def init(givenKey):
    
    S = []
    # initiate the s table from 0 to 255
    for i in range(256):
        S.append(i)
        
    j = 0
    #j variable is used to keep track of the index of the state table that is swapped with the current index i
    for i in range(256):
        j = (j + S[i] + ord(givenKey[i % len(givenKey)])) % 256 # assigning value, getting the current value of the key + the current on the state table 
        
        # swapping 
        temp = S[i]
        S[i] = S[j]
        S[j]= temp
    
    # return the state table,in other words defining a scheduling used to generate a pseudorandom keystream
    return S 

    
#generates a pseudo-random keystream by repeatedly shuffling the state table. Takes the scheduling    
def generateStream(S, plaintext):
    keystream = []
   
    i = 0
    j = 0
    
    # assign a keystream the same lenght as the plaintext 
    for i in range(len(plaintext)): 
        #i += 1
        # variables to shuffle the state table
        i = (i + 1) % 256 
        j = (j + S[i]) % 256
        
        # swapping 
        temp = S[i]
        S[i] = S[j]
        S[j]= temp
        #generating a keystream of the same length as the plaintext
        keystream.append(S[(S[i] + S[j]) % 256])
    return keystream
    
# Xoring to get the cypher text
def encrypt(keystream, plaintext):
    toOrd = [] 
    result = []
    
    # go over the plaintext and append each ordinal value to ordinals list 
    for char in plaintext:
        toOrd.append(ord(char))
    
    for i in range(len(toOrd)):
        # xoring with the next byte of the message to produce the next byte of the ciphertext 
        result.append((toOrd[i] ^ keystream[i]))
    return result

# Xoring to get the plain text
def decrypt(keystream, cypher):
    toOrd = [] 
    result = ''
    
    # go over the cypher and appends to ordinals list 
    for i in range(len(cypher)):
        toOrd.append(cypher[i])
    
    
    for i in range(len(toOrd)):
        # xoring with the next byte of the message to produce the next byte of the plaintext
        result = result + chr(cypher[i] ^ keystream[i])

    # represented as decimal values
    return result


# asks for key and the plaintext, implements the Rc4 functions 
def Rc4(key,  plaintext):
   
    #inititalize the key scheduling algorithm 
    scheduled  = init(key)
   
    # genreate the key stream 
    keystream = generateStream(scheduled, plaintext)
    
    #encrypt the plaintext
    cypher = encrypt(keystream, plaintext)
    
    #decrypt the cyphertext
    decrypted = decrypt(keystream, cypher)

    #return both the encrypted and decrypted outcome 
    return cypher, decrypted 
    
# print the rc4 outcome 
print("This the result before and after applying RC4 Encryption:" , Rc4(key, plaintext))

# Pseudo code and explanation from https://en.wikipedia.org/wiki/RC4
    