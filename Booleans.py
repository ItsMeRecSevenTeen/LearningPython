a = 200
b = 33
if b > a:#returns false, So, Executes the else data block 
    print("b is greater than a")
else:
    print("b is not greater than a")
#Evaluating Values and Variables
print(bool("Hello"))#With the function bool() we can evaluate any value     #Returns True
print(bool(17))     #Returns True
print(bool())       #Returns False
x = "Hello"
y = 15
print(bool(x))  #Returns True
print(bool(y))  #Returns True
#Note: Almost any value is evaluated to True if it has some sort of content
print(bool("abc"))  #Returns True
print(bool(""))     #Returns False
print(bool(17))     #Returns True
print(bool(0))      #Returns False
print(bool(["Apple", "Cherry", "Banana"]))  #Returns True
print(bool([]))     #Returns False
#Otherwise, empty values are evaluated in False, even the own value False (Obviously)
print(bool(False))  #These examples are False
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
    def _len_(self):
        return 0
myobj = myclass()
print(bool(myobj._len_()))  #Evaluates and prints False because the function _len_() returns 0
print(bool(myobj))          #Evaluates and prints True because myobj has content like function _len_()
#Functions can Return a Boolean
def myFunction():
    return True
print(myFunction()) #Prints True, because the function returns True

def myOtherFunction():
    return True
if myFunction():    #'if' evaluates the function, if function returns True, execute the First Data Block 
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x, int))   #Returns True, because x is instance of int (x is an integer)