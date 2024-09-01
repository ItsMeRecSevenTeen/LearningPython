#Sort list alphanumerically
thislist = ["Orange", "Mango", "Kiwi", "Pineapple", "Banana"]
thislist.sort() #sort() will sort the list alphanumerically in ascending way by default
print(thislist)
#Numeric Example
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#Sort Descending
thislist = ["Orange", "Mango", "Kiwi", "Pineapple", "Banana"]
thislist.sort(reverse = True)   #We must write the argument 'reverse' in True to sort alphanumerically descending
print(thislist)
#Numeric Example
thisList = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thisList)

#Customize Sort Function
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #We can create a func to sort our lists using as argument 'key = function'
print(thislist)

#Case Sensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]   #With letters, sort() will sort capital letters first
thislist.sort() #Then will sort lower case letters
print(thislist)
thislist.sort(key = str.lower) #If we want a case-insensitive sort function, we must write 'key = ' and the built-in function
    # in the arguments, in this case, str.lower
print(thislist)

#Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()  #We can reverse the sort of a list like a mirror, regardless of the alphabet 
print(thislist)