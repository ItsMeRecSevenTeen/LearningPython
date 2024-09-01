thisList = ["Apple", "Banana", "Cherry"]
print(thisList[0])  #We can access to the item of the list referring to the index number

#Negative Indexing: Start from the end
print(thisList[-1]) #[-1] refers to the last item, [-2] refers to the second last item  #outputs Cherry

#Range of Indexes
thisList = ["Apple", "Banana", "Orange", "Kiwi", "Melon", "Mango"]
print(thisList[2:5])    #Prints the index 2 (Included), index 3 and index 4, Index 5 (No included)
print(thisList[:4])     #Prints from the start of the list to the index 4 (Not included)
print(thisList[2:])     #Prints from the index 2 (Included) to the end of the list

#Range of negative Indexes: If we want to start from the end of a list
print(thisList[-4:-1])  #Prints "Orange" to "Mango" BUT is not included

#Check If Item Exists
if "Apple" in thisList:
    print("Yes, \"Apple\" is in the fruits  list")