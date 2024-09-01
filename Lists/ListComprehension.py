fruits = ["Apple", "Banana", "Cherry", "Kiwi", "Mango"]
newlist = []    #List comprehension allows us to create another list with items from another list

for x in fruits:
    if "A" in x:
        newlist.append(x)
print(newlist)  #Prints the list with one item, because Apple starts with letter 'A'

newlist = [x for x in fruits if "A" in x]   #Here is another way to do the same thing with one code line
    #Sintax:  [expression for item in iterable if condition == True]    The expression will be valid if only True
#Condition
newlist = [x for x in fruits if x != "Apple"]   #It can be use as a filter, because only accepts items that
    #valuate to True, if the expression is True, the Item will be added to the new list
        #The list will contain all fruits from 'fruits' list except "Apple"
#With no if statement
newlist = [x for x in fruits]
#Iterable
newlist = [x for x in range(10)]    #We can use the range() function to create an iterable
#Adding a condition to it
newlist = [x for x in range(10) if x < 5]   #Accept only numbers lower than 5
#Expression
newlist = [x.upper() for x in fruits]   #We can manipulate or format the item before to assign it to the list

newlist = ['Hello' for x in fruits] #Set all values in the new list to 'Hello', This expression can also contain conditions, without being a
    #Filter, but as a way to manipulate the outcome
newlist = [x if x != "Banana" else "Orange" for x in fruits]    #The expression says: Return the item if is not Banana, if it is Banana return
    #Orange