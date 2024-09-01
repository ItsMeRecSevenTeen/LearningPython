#We cannot access to an item by referring the index, but we can use for loops and the membership keyword 'in'
thisset = {"Apple", "Banana", "Berry"}
for x in thisset:
    print(x)    #Prints each item from the set by the iterable x
print("Banana" in thisset)  #Prints True, because "Banana" is in thisset
#Note: We cannot change the items of a Set, but We can add new items