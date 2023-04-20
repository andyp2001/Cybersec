alphabetList =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # used to match the decoded hexadecimals


userInput = [] # store all lines of hexadecimal values


# while loop to get multiple lines of code to meet the input criteria
while True:
    try:
        multiline = input("Please enter your lines hexadecimal number (control + D to enter all lines) :") # ask the user for a line of hexadecimal values
        if multiline:
         split = multiline.split(" ") # split after every blank space
         userInput.append(split)
    except EOFError:
        break
    
    
print("User entered: ", userInput)# display inital input 

def decodeString(given): # function to decode the lines of hexadecimal values
  result = "" 
  mixedList = [] # create initial list to store the mixed values
  for sublist in userInput:
    mixedList.extend(sublist) # since we used split, lines/sublist of hexadecimal input would need to be merged into one list 
  print("List while it is still mixed: ", mixedList)
  
  # creating new list of values in the right order
  organizedList = []
  for i in range(len(mixedList)):
      if (i + 5) < len(mixedList): # since the previous output was seprated by 5 hexadecimals, organize according to the output
        organizedList.append(mixedList[i]) # # append the current hexadecimal
        organizedList.append(mixedList[i + 5]) # then add current index + 5, knowing the output from the encode was separaeted into five in a line
  print("Hexadecimal List after organizing: ", organizedList)
    
  # shifting the poisitions to the left 
  finalList = []
  for i in range(len(organizedList)):
    formatted = organizedList[i].replace('0x', '') # format to get the only two last digits
    currentLetter = bytes.fromhex(formatted).decode("utf-8").lower() # decode the current letter to shift
    for x in range(len(alphabetList)): # go over all elements in the alphabet list 
      if str(currentLetter) == alphabetList[x]:
          current = x - 4 # shifting 4 to the left
          if current < 0:
              current = (26 + current) 
          finalList.append(hex(ord(alphabetList[current].upper()))) # appending the hexadecimals to a new list after shifting 
    
    
  for i in range(len(finalList)):
      formatted = finalList[i].replace('0x', '')# format to get the only two last digits
      bystesFromHex = bytes.fromhex(formatted)
      character = bystesFromHex.decode("utf-8") # Converting back to characters using UTF-8 encoding
      result = result + character # attach to the resulting string 
      
  print("Hexadecimal List after shifting: ", finalList) # printing the final shifted and organized list
  return result # return the result after shift 


result = decodeString(userInput) 
print("\n", "Result of string after decoding: ", result) # print result after decode 


# References https://pythontic.com/containers/bytes/fromhex, https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-the-user, 
# https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods
  
  
