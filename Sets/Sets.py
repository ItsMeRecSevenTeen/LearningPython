#Sets
#A set is a collection wich is UNORDERED, UNCHANGEABLE, UNINDEXED and DOES NOT ALLOWS duplicate values
#UNORDERED: The items in sets does not have a defined order, the items will appear in random order each use of it
#UNCHANGEABLE: We cannot modify the items of a set once the set was created, However, We can add and remove items
#UNINDEXED: There is no index numbers to refer an item
thisset = {"Apple", "Banana", "Cherry"} #A set has curly braces
print(thisset)

#Duplicates Not Allowed:    #Sets cannot have two items with the same value
thisset = {"Apple", "Banana", "Cherry", "Apple"}    #Duplicate values like 'Apple' will be ignored
print(thisset)
    #The values True and 1 are considered the same values in Sets, and are treated as duplicates
thisset = {"Apple", "Banana", "Cherry", True, 1, 2} #True will be considered first, 1 is ignored
print(thisset)
    #The values Flase and 0 are considered the same values in Sets, and are treated as duplicates
thisset = {"Apple", "Banana", "Cherry", False, True, 0} #False will be considered first, 0 is ignored
print(thisset)

#Getting the length of a Set
thisset = {"Apple", "Banana", "Cherry"}
print(len(thisset)) #Outputs 3

#Set Items - Data Types
set1 = {"Apple", "Banana", "Cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
    #A set can contain different data types:
set1 = {"abc", 34, True, 40, "Male"}

#type()
#Python clasifies this data type as 'Set'
myset = {"Apple", "Banana", "Cherry"}
print(type(myset))

#The set() Constructor
thisset = set(("Apple", "Banana", "Cherry"))    #Do not forget to write the Double Round-Brackets