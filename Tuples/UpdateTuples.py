#Tuples are unchangeable, meaning that we cannot change, add or remove items once the tuple have been created
#But there is some ways to do it

#Change Tuple Values: We can convert the main tuple into a list, change the values and convert again the list
    #To a tuple using list() constructor
x = ("Apple", "Banana", "Cherry")
y = list(x)
y[1] = "Kiwi"
x = tuple(y)
print(x)

#Add Items: 1.- We can use the same logic from above, using .append() to lists and then, convert it back to a tuple
thistuple = ("Apple", "Banana", "Cherry")
y = list(thistuple)
y.append("Orange")
thistuple = tuple(y)

#2.- We can add a Tuple to another Tuple,We can add the items from a tuple to give it to another tuple
thistuple = ("Apple", "Banana", "Cherry")
y = ("Orange",) #Remember the comma if the tuple only has one item
thistuple += y
print(thistuple)

#Remove Items: 1.- We can use the same workarounds as we used in add and change items from a list
thistuple = ("Apple", "Banana", "Cherry")
y = list(thistuple) #Convert the tuple into a list
y.remove("Apple")   #Remove the item Apple from the list 'y'
thistuple = tuple(y)#Convert the list 'y' into a tuple again

#2.- Or we just can delete the tuple completely with a keyword
thistuple = ("Apple", "Banana", "Cherry")
del thistuple   #Delete the tuple with the keyword 'del'
print(thistuple)    #An error will occur because the tuple 'thistuple' no longer exists
