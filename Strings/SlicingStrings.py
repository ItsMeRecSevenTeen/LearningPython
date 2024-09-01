b = "Hello, World!"
#[startPos:endPos]
print(b[2:5])   #Prints the characters from position 2 to 5 (Not included)   "llo"
print(b[:5])    #Prints from String start to position 5 (Not included)
print(b[2:])    #Prints from position 2 (Not included)to end String
#Negative indexing
print(b[-5:-2]) #Starts the slice from the end of the String to the -2 position (Not included)