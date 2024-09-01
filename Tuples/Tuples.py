#A tuple is a data collection wich is ordered and UNCHANGEABLE
thistuple = ("Apple", "Banana", "Cherry")   #Tuple items are ordered, unchangeable and allow duplicate values
print(thistuple)
#ORDERED: Tuple items have a defined order, that means that order will not change
#UNCHANGEABLE: Tuples are unchangeable, That means that we cannot change, add, or remove items after it was created
#ALLOWS DUPLICATES: Tuples can have items with the same value
thistuple = ("Apple" ,"Banana", "Cherry", "Apple", "Cherry")
print(thistuple)

#Tuple Length
thistuple = ("Apple", "Banana", "Cherry")
print(len(thistuple))   #Prints and return the number of item in the tuple

#Create Tuple With One Item
thistuple = ("Apple",)  #A tuple
print(type(thistuple))

thistuple = ("Apple")   #Not a Tuple
print(type(thistuple))

#Tuple Items - Data Types
#Tuples can be of any data type:
tuple1 = ("Apple", "Banana", "Cherry")  #String type
tuple2 = (1, 5, 7, 9, 3)                #int type
tuple3 = (True, False, False)           #boolean type
tuple4 = ("abc", 34, True, 40, "male")  #A tuple with any other data type

#type()
myTuple = ("Apple", "Banana", "Cherry")
print(type(myTuple))    #Outputs "<class 'tuple'>"

#The tuple() Constructor
thistuple = tuple(("Apple", "Banana", "Cherry")) #Makes a tuple with constructor tuple() with double (())
print(thistuple)