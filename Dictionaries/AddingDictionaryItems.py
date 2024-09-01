#Adding Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
thisdict["color"] = "red"   #We use a new index key and the new value of this key, this adds a key named 'color'
    #With the value "red"
print(thisdict)

#Updating Dictionary

thisdict.update({"color": "red"})   #We can do the same thing with .update() method, in the arguments must be a
    #dictionary or any iterable object