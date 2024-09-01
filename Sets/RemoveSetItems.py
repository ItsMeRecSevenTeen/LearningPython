#Removing Items We can use the remove() and discard() methods, giving them the value or item as argument
thisset = {"Apple", "Banana", "Cherry"}
thisset.remove("Banana")    #If the item to remove does not exists in the set, .remove() WILL RAISE an error
thisset.discard("Cherry")   #If the item to remove does not exists in the set, .discard() WILL NOT RAISE an error
print(thisset)
#Also, we can use the .pop() method, BUT, this method will remove a random item, We will not see what item was removed
thisset = {"Apple", "Banana", "Cherry"}
x = thisset.pop()   #Removes a random item from the Set #And the return value of .pop() is the removed item
print(x)    #Prints the item that was removed from the Set
print(thisset)

#If we use the method clear(), the Set will be cleared, having no items itself
thisset = {"Apple", "Banana", "Cherry"}
thisset.clear()
print(thisset)
#Also we can use the keyword 'del' to delete the set completely
thisset = {"Apple", "Banana", "Cherry"}
del thisset
print(thisset)  #An error will occur because the Set 'thisset' does not exist