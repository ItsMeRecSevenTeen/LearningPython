#Joinning Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2   #We can join or concatenate two or more lists using the + operator
print(list3)

for x in list2:
    list1.append(x)     #Also we can join each item from list2 to list1 by looping through list2 using append()
print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)     #Otherwise, we can use extend() method to add all the elements 
print(list1)