alphabetList =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # character matching


specialChars = '[@_!#$%^&*()<>?/\|}{~:]' # for symbol matching 

userInput = input("Please enter your word/phrase: ") # ask for user input (word/phrase)

def encode(given, shiftNum ): # function to encod the text
  oridnals = [] # keep ordinal list
  result = ""
  for i in range(len(given)): # iterate over all elements in the given text
    currentIndex = given[i].lower() # convert to lower case to ignore upper case, step 3
    if currentIndex == " " and currentIndex in specialChars : # if space and characters are in string, skip
      i = i + 1
    for x in range(len(alphabetList)): # go over all elements in the alphabet list 
      if currentIndex == alphabetList[x]: # if match
          current = x + shiftNum
          if current > 25:
              current = (current - 26) # wrap around the list if the current index is more than 25 the last element
          result = result + alphabetList[current].upper() # convert to upper case 
          oridnals.append(hex(ord(alphabetList[current].upper()))) # append to the ordinals list as a hexadecimals
  print("Original Hexadecimal List", oridnals,  "\n") # print the original hexadecimals list 
  even = []
  odd = []
  for i in range(len(oridnals)): 
      if i % 2 == 0: # if position is even 
          even.append(oridnals[i]) # append to even list
      else:
          odd.append(oridnals[i]) # append to the odd list 
  combined = even + odd # combin in ocrrect order 
  
  print("Encoding: ", "\n")
  for i in range(len(combined)):
      counter = i + 1
      if counter % 5 == 0 and counter != 0: # if the position is divisible by 5 
          print(combined[i], "\n") # print and establish newline
      else:
          print(combined[i], end=" ") # print the hexadecimal 
          
  return result # return the result encoding


result = encode(userInput, 4)  # endcode and shift 4
print("\n", "Result after applying shift: ", result) # print result after cypher 

  
  
# symbol assistance, https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/

  
  