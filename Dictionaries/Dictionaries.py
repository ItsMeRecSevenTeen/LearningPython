thisdict = {    #Dictionaries are created by using curly braces and colons, Dictionaries are used to store data
    "brand": "ford",    #In key values: value pairs, Are collections that ARE ORDERED, CHANGEABLE, AND DO NOT ALLOW
    "model": "Mustang", #DUPLICATES
    "year": 1964
}
print(thisdict)
#Dictionary Items
print(thisdict["brand"])    #We can print or use items by referring the KEY NAME    referring 'brand', Outputs 'ford'
#Dictionaries are ordered, meaning that items have a defined order, Unordered means thath the items do not have a
    #defined order, and therefore, We cannot refer to an item by using an index
#CHANGEABLE: Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary was
    #created
#DUPLICATES NOT ALLOWED: Dictionaries cannos have two items with the same key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020    #Duplicate values will overwrite existing values
}
print(thisdict)

#Dictionary Length
print(len(thisdict))    #To determinate how many items a dictionary has, we can use the len() method

#Dictionary Items - Data types
thisdict = {    #A dictionary can contain any data of any type
    "brand": "Ford",    #String data type key
    "electric": False,  #Boolean data type key
    "year": 1964,       #Int data type key
    "colors": ["red", "white", "blue"]  #List data type key
}

#type() #Python classifies this data types as dict:
print(type(thisdict))   #Outputs <Class: dict>

#The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")    #There is no double brackets, just the key and values