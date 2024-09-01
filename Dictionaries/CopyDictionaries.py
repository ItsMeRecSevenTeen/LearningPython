#Copy a Dictionary> We cannot copy a dictionary doing this: "dict2 = dict1" because dict2 will be only a reference
    #to dict1, meaning that any changes made in dict1 will automatically also be made in dict2
#Using .copy()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
mydict = thisdict.copy()    #The correct way to make a copy of a dictionary
mydict = dict(thisdict)     #Another way to make a copy using the dict() constructor
print(mydict)