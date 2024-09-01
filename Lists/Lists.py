myList = ["Apple", "Banana", "Cherry"]  #Lists are created using Square Brackets
#Lists have numeric indexes, The item number one has index [1], the next item has index [2]...
print(myList)   #Lists are ordered, changeable and allow duplicate values
#Ordered:The items have a defined order, that order will not change, there are methods that allows us
    #to change the order of the items, But the main idea is the order of the items will not change
#Changeable:The lists are changeable, meaning that we can change, add and remove items in a list
    #after it has been created

#Allow duplicates
thisList = ["Apple", "Banana", "Cherry", "Apple", "Cherry"]#Lists allow duplicate values
print(thisList)

#List Length
thisList = ["Apple", "Banana", "Cherry"]
print("Number of items " + str(len(thisList)))  #len() returns the number of items of the list

#List Items - Data Types
list1 = ["Apple", "Banana", "Cherry"]   #List with String Items
list2 = [1, 2, 3, 4, 5]     #List with Int Items
list3 = [True, False, False]        #List with Boolean Items
list4 = ["abc", 34, True, 40, "male"]   #Also Lists can contain different Data Types

#Data Type of a list
myList = ["Apple", "Banana", "Cherry"]
print(type(myList)) #It is a data type 'list'

#The list() Constructor
thisList = list(("Apple", "Banana", "Cherry")) ##Double round of parenthesis or round-brackets
print(thisList)
