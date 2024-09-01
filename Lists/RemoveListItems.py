#Remove Specified Item
thislist = ["Apple","Banana","cherry"]
thislist.remove("Banana")   #With Function remove(), We can remove a specified item by giving the value
print(thislist)

thislist = ["Apple", "Banana", "Cherry", "Banana", "Kiwi"]#If there is more items with the same value...
thislist.remove("Banana")#...The method remove() will remove the first occurance 
print(thislist)

#Remove Specified Index
thislist = ["Apple", "Banana", "Cherry"]
thislist.pop(1) #pop() allow us to remove a specified index, in this case the index [1] ("Banana")
print(thislist)
thislist = ["Apple", "Banana", "Cherry"]
thislist.pop()
print(thislist) #If we do not especify the index number, the method will remove the last item in the list
#Also, the keyword 'del' does the same thing than pop() function
thislist = ["Apple", "Banana", "Cherry"]
del thislist[0] #Deletes the item 'Apple'
print(thislist)
#We must be carefull at the moment to use this keyword, if we do not write the Square Brackets, it will
    #delete the entire list
del thislist

#Clearing the list
thislist = ["Apple", "Banana", "Cherry"]
thislist.clear()    #This method just empties the list, but the list still remains without content
print(thislist)