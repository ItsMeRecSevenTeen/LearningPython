#Copy List
#We cannot copy a list with the statement "List2 = List1" because 'List2' will be only a reference to List1
    #And changes in "List1" will automatically also be made in 'List2'
thislist = ["Apple", "Banana", "Cherry"]
copylist = thislist.copy()  #A simple way to make copies of a list without referencing other lists
copylist = list(thislist)   #Another way to make a copy of a list