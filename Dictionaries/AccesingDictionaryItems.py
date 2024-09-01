#Accesing Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]   #Dictionaries does not have numeric indexes, if we want to use a value, we must refer by the 
                        #key inside square brackets
x = thisdict.get("model")   #The .get() method does the same thing than the above codeline 

#Getting keys
x = thisdict.keys() #The .keys() method returns a list of all the keys in a dictionary  x is a list of those keys
    #The list of keys is a view of the dictionary, and therefore, Any changes done to the dictionary, will be
    #reflected in the keys list
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)    #Before the change
car["color"] = "white"  #Adds a key named "color" with the value "white"
print(x)    #After the change
print(car["color"])

#Getting Values
x = thisdict.values()   #The method .values() returns a list of all the values in the dictionary
    #The list of values is a view of the dictionary, and therefore, any changes done to the dictionary, will be
    #reflected in the values list
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()   #Getting the key's values from the dictionary car 
print(x, "Without a modified value (Before Change)")    #Before the change
car["year"] = 2020  #Assigning a new value to the existing key 'year'
print(x, "With a modified value (After change)")    #After the change
    #If we add a new item, it will be updated anyway
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()    #Getting keys from the dictionary car
print(x, "Without color (before change)")    #Before the change
car["color"] = "red"    #Adding a key named 'color' with the value 'red'
print(x, "With color (After change)")    #After the change

#Get Items
x = thisdict.items()    #The method .items() will return each item in a dictionary as tuples in a list
    #The returned list is a view of the dictionary, meaning that any changes done to the dictionary will be reflected
    #in the items list
car = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
x = car.items() #Getting the items from the dictionary "Car"
print(x)    #Before the changes
car["year"] = 2020  #Modifying an existing key
print(x)    #After change
car["Color"] = "Red"#Adding a new key with a new values
print(x)    #After changes

#Check If Key Exists>Check If key 'model' is present in the dictionary:
if "model" in thisdict: #We must use the keyword 'in' to check if a key is present in a dictionary
    print("Yees, 'model' is one of the keys in the 'thisdict' dictionary")