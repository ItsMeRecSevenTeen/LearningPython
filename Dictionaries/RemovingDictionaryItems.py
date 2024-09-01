#Remove Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
#Using .pop() method
thisdict.pop("model")   #Removes the key 'model' with its value (specified value)
print(thisdict, "key \"model\" removed")
#Using .popitem() method
thisdict.popitem()  #Removes the last key from the dictionary   (removes 'year')
print(thisdict, "Key \"year\" removed")
#Using keyword 'del'
del thisdict["brand"]   #Removes the key 'brand' with its value (specified value)
print(thisdict)
del thisdict #If we do not especify the index key, 'del' will eliminate the entire dictionary
#Using .clear() method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : "1964"
}
thisdict.clear()    #Empties the dictionary, Therefore, the dictionary will not have any values