thislist = ["Apple", "Banana", "Cherry"]
thislist[1] = "Blackcurrant"    #Changing the value "Banana" to "blackcurrant"
print(thislist)

#Changing a Range of Item Values
thislist = ["Apple", "Banana", "Cherry", "Orange", "Kiwi", "Mango"]
thislist[1:3] = ["Blackcurrant", "Watermelon"]  #"Banana" and "Cherry are reassigned with those values"
print(thislist)
#If we insert more items than we replace, the new items will be inserted whe we specified, the remaining
    #items will move or displace accordingly
thislist = ["Apple", "Banana", "Cherry"]
thislist[1:2] = ["Blackcurrant", "Watermelon"]  #"Blackcurrant" replaces "Banana" but "Watermelon" is added
print(thislist)
#If we insert less item than we replace, the new items will be inserted where we specified, the remaining
    #items will move accordingly
thislist = ["Apple", "Banana", "Cherry"]
thislist[1:3] = ["Watermelon"]  #Takes "Banana" and "Cherry" and replaces them with "Watermelon"
print(thislist)
#Insert Items
thislist = ["Apple", "Banana", "Cherry"]
thislist.insert(2, "Watermelon")    #Inserts in position 2 the item "Watermelon" #Cherry will be moved to right
print(thislist) #Now, the list contains 4 items