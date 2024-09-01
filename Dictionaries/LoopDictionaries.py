#Loop trough a Dictionary>When we do this , the return value will be the keys of dictionary, but there are methods
    #that returns the values as well
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
for x in thisdict:  #Prints all key names in the dictionary, one by one:
    print(x)
for x in thisdict:
    print(thisdict[x])  #Prints all values in the dictionary, one by one
for x in thisdict.values():
    print(x)        #Prints all values in the dictionary, same thing as the above codeline
for x in thisdict.keys():
    print(x)    #Prints all keys in the dictionary one by one
for x, y in thisdict.items():
    print(x, y) #Prints keys and values by using the method .items()