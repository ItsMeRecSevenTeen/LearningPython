#Change values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018 #We can change a key value by referring to its key name> Here is changing the value of key
    #"year" from 1964 to 2018

#Update Dictionary
thisdict.update({"year": 2020}) #We can do the same thing than the above codeline with .update() method, The argument
    #must be a dictionary or an iterable object with key in value pairs> Here is changing the value of key "year"
    #from 2018 to 2020