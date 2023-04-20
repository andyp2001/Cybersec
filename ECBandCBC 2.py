def expand(x: int) -> int:
    table = [1, 2, 4, 3, 4, 3, 5, 6]

    positions = {
        1: (x & 0b100000) >> 5,
        2: (x & 0b10000) >> 4,
        3: (x & 0b1000) >> 3,
        4: (x & 0b100) >> 2,
        5: (x & 0b10) >> 1,
        6: (x & 0b1),
    }
    result = 0

    for i in range(len(table)):
        result |= positions[table[i]] << (7-i)

    return result
    

  
def s1(x: int) -> int:
     
    assert x>=0 and x<=0b11111, "Invalid input to sbox 1"
	
    sbox1 = (
		(0b101, 0b010, 0b001, 0b110, 0b011, 0b100, 0b111, 0b000), 
		(0b001, 0b100, 0b110, 0b010, 0b000, 0b111, 0b101, 0b011)
	) 
  
    position = (x >> 3)

    if position == 1:
     x1 = 1  
    else:
        x1 = 0  

    x2 = x & 0b111
	
    return sbox1[x1][x2]


	
def s2(x: int) -> int:

  assert x>=0 and x<=0b11111, "Invalid input to sbox 2"
  sbox2 = (
  		(0b100, 0b000, 0b110, 0b101, 0b111, 0b001, 0b011, 0b010), 
  		(0b101, 0b011, 0b000, 0b111, 0b110, 0b010, 0b001, 0b100)
  	) 

  position = (x >> 3)

  if position == 1:
    x1 = 1  
  else:
    x1 = 0  


  x2 = x & 0b111
  return sbox2[x1][x2]
  
def f(x: int, key: bytearray) -> int:
    
    expanded = expand(x) ^ key
    leftBlock = expanded >> 4
    rightBlock = expanded & 0b1111
    
    
    result = s1(leftBlock) << 3 | s2(rightBlock)
    return (result)
    



def subkey(key: int, rnd: int) -> int:
    

    if rnd == 1:
        subkey = key >> 1
    elif rnd == 2:
        subkey =  key & 0b11111111
    elif rnd == 3:
        subkey =  (((key & 0b1111111) << 1) | (key >> 8))
    elif rnd == 4:
        subkey = ((key & 0b111111) << 2) | (key >> 7)
    elif rnd == 5:
        subkey =  ((key & 0b11111) << 3) | (key >> 6)

    return subkey


	
def round(x: int, key: int, rnd: int) -> int:

	l0 = x >> 6
	r0 = x & 0b111111

	r1 = f(r0, subkey(key, rnd)) ^ l0
	l1 = r0
	return l1 << 6 | r1

def encrypt(x: int, key: int) -> int:

	assert x >= 0 and x<=0b111111111111, "Invalid plaintext"
	assert key >= 0 and key<=0b111111111, "Invalid key"
	y=x
	for r in range(5):
		y=round(y, key, r+1)
	return y

def ecb(x: str, key: int) -> str:

    toHex = x.encode('utf-8').hex()

    blocks = []

    for i in range(0, len(toHex), 3):
      blocks.append(toHex[i:i+3])

    hexString = '0x'
    for i in range(len(blocks)):
        encrypted = (encrypt(int(blocks[i], 16), key))
        hexString = hexString + hex(encrypted)[2:]

    return "ECB: " + hexString
    
    
    
def cbc(x: str, key: int, iv: int) -> str:

    toHex = x.encode('utf-8').hex()

    blocks = []

    for i in range(0, len(toHex), 3):
      blocks.append(toHex[i:i+3])

    encrypted = 0 
    hexString = ''

    for i in range(len(blocks)):
        if i == 0:
          newblock = int(blocks[i], 16) ^ iv
          encrypted = encrypt(newblock, key)
          hexString = hex(encrypted)[2:]
        elif i >= 1:
          newblock = int(blocks[i], 16) ^ encrypted
          encrypted = encrypt(newblock, key)
          hexString += hex(encrypted)[2:]

    return 'CBC: 0x' + hexString 


# driver function with test cases
if __name__=="__main__":

    assert expand(0b110011) == 0b11000011, "Expander failed"
    assert subkey(0b101100101, 4) == 0b10010110, "Subkey function failed"
    assert s1(0b1001) == 0b100, "S1 failed"
    assert s2(0b1001) == 0b011, "S2 failed"
    assert encrypt(0x726, 0x99) == 0x3f8, "Encryption failed"
    print(ecb("World!", 421))
    print(cbc("World!", 421, 124))
    print("Everything is Ok")

