#Access Tuple Items
thistuple = ("Apple", "Banana", "Cherry")
print(thistuple[1]) #Prints "Banana"

#Negative Indexing
print(thistuple[-1])

#Range of Indexes
thistuple = ("Apple", "Banana", "Cherry", "Orange", "Kiwi", "Melon", "Mango")
print(thistuple[2:5])   #Will return a new tuple with the specified items
print(thistuple[:4])    #With no values in the left bracket, the range will start from the start to the index
print(thistuple[2:])    #With no values in the right bracket, the range will end to the end starting by index

#Range of Negative Indexes
print(thistuple[-4:-1])   #Starts from the end to the fourth element and ends to first index (Not included)

#Check if Item Exists
if "Apple" in thistuple:
    print("Yes, \"Apple\" is in the fruits tuple")