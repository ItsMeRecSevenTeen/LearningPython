#We cannot change the items of a set, but we can add new items using .add() method
thisset = {"Apple", "Banana", "Cherry"}
thisset.add("Orange")
print(thisset)  #Remember that the items appears in random order with each use or reference of the Set

#Add Sets:  We can add another set into the current set using the update() method:
thisset = {"Apple", "Banana", "Cherry"}
tropical = {"Pineapple", "Mango", "Papaya"}
thisset.update(tropical)    #With .update() We can add new items to the current set
print(thisset)

#Adding Any Iterable: The .update() method can accept any iterable object such as tuples, lists, dictionaries..
thisset = {"Apple", "Banana", "Cherry"}
mylist = ["Kiwi", "Orange"]
thisset.update(mylist)  #Be carefull with the order, The new items will be items of a Set, in viceversa will be a list
print(thisset)