#Append Items
thislist = ["Apple", "Banana", "Cherry"]
thislist.append("orange")   #append() adds an item to the end of the list
print(thislist)     #Now, the list has 4 items
#Insert Items
thislist = ["Apple", "Banana", "Cherry"]
thislist.insert(1, "Orange")    #Adds an item in the index number [1] and the value of it
print(thislist)
#Extend List
thislist = ["Apple", "Banana", "Cherry"]
tropical = ["Mango", "Pineapple", "Papaya"]
thislist.extend(tropical)   #Appends another list to 'thislist', Adding all elements from 'Tropical' in the end
print(thislist)

#Add any iterable
thislist = ["Apple", "Banana", "Cherry"]
thistuple = ("Kiwi", "Orange")
thislist.extend(thistuple)  #extend() can add any iterable object such as Tuples, lists, and dictionaries
print(thislist)