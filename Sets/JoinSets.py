#Joining Two Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #We can use the .union() method to join two sets    RETURNS A NEW set
set1.update(set2)    #Also the .update() INSERTS items in same set
print(set3)
print(set1)         #Note: Both methods WILL EXCLUDE any duplicate items

#Keeping ONLY the Duplicates    (Intersection)
x = {"Apple", "Banana", "Cherry"}
y = {"Google", "Microsoft", "Apple"}
x.intersection_update(y)    #This method WILL UPDATE the items that ARE PRESENT in both sets, x will have those items
z = x.intersection(y)   #This method RETURNS a new set with the items that are present in both sets
print(x)
print(z)

#Keep All but NOT the Duplicates    (Symmetric Difference)
x = {"Apple","Banana" , "Cherry"}
y = {"Google", "Microsoft", "Apple"}
x.symmetric_difference_update(y)    #This method UPDATES the items that ARE NOT PRESENT in both sets
z = x.symmetric_difference(y)   #This method RETURNS a new set with the items that ARE NOT PRESENT in both sets
print(x)
print(z)

#The values True and 1 are considered the same value in Sets, and are treated as duplicates
x = {"Apple", "Banana", "Cherry", True} #True and 1 will not be included in the new set
y = {"Google", 1, "Apple", 2}
z = x.symmetric_difference(y)
print(z)