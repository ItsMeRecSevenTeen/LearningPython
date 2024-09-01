#Creating a function
def my_function(): #We can create a function using the keyword 'def'
    print("Hello from a function")

#Calling a function
my_function()   #Calls the function to be executed

#Arguments
def my_function(fname): #Arguments goes inside the round brackets, if there is more than one, separate them with ','
    print(fname + " Refsnes")

my_function("Emil") #We must specify the arguments when we call the functions
my_function("Tobias")
my_function("Linus")

#Number of Arguments
def my_function(fname, lname):  #Functions can have any parameters we want, but we have to make sure when calling
    #the function must match the number of parameters and the number of arguments -> Two parameters
    print(fname + " " + lname)
my_function("Emil", "Refsnes")  #-> Two Arguments --> If we call the function with 1 or more than 2 arguments, an error
    #Will occur

#Arbitrary Arguments (*args): If we do not know how many arguments will be passed into our functions, add a * before
    #the parameter name in the function definition
def my_function(*kids): #The Function will receive a TUPLE of arguments, and we can access to the items accordingly
    print("The youngest kid is " + kids[2]) 

#Keyword Arguments (kwargs): We can send arguments with the 'key = value' syntax, In this way, the order of the
    #Arguments does not matter
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitrary Keyword Arguments (**kwargs)
def my_function(**kid):#The function will receive a DICTIONARY of arguments, and we can access to the items accordingly
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#Default parameter Value
def my_function(country = "Norway"):    #The default value is 'Norway'
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()#If we call a function without argument, the argument will take the default value defined in the function param
    #> Will print "I am from Norway", because there is no parameters in the call and the default value is "Norway"
my_function("Brazil")

#Passing a List as an Argument> We can pass any data type to a function, will be treated as the same data type inside the func
def my_function(food):  #Will receive a List called 'food'
    for x in food:
        print(x)

fruits = ["Apple", "Banana", "Cherry"]
my_function(fruits) #Data type of List in the arguments

#Return Values: A function can return a value using the 'return' statement
def my_function(x):
    return 5 * x    #Return the result of 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#The pass Statement
def myfunction():
    pass    #With this statement we can avoid to getting an error if for some reason we have an empty function

#Positional-Only Arguments
def my_function(x,y, /):    #This function only accepts positional arguments, meaning that arguments must respect the order
    #That they are established (Order does matter)
    print(x,y)
my_function(3, 6)   #x is equals to 3, y is equals 6

def my_function(x): #Without , / we are actually allowed to use keyword arguments, even if the function expects positional args
    print(x)
my_function(x = 3)  #This is a Keyword Argument

#If we try to send a KEYWORD Argument to a Function that ONLY accepts POSITIONAL-Arguments, we will get an error
""" def my_function(x, /):
    print(x)
my_function(x = 3) """  #Incorrect

#Keyword-Only Arguments
def my_function(*, x):  #This function only accepts Keyword arguments, meaning that arguments must respect the syntax 
    #"key = value" (Order does not matter)
    print(x)
my_function(x = 3)

def my_function(x): #Without *, we are allowed to use positionale arguments, even if the function expects keyword arguments
    print(x)
my_function(3)  #This is a positionale argument

#If we try to send a POSITIONAL argument to a Function that ONLY accepts KEYWORD-Arguments, we will get an error
""" def my_function(*, x):
    print(x)
my_function(3) """#Incorrect

#Combining Positional-Only and Keyword-Only: We can combine the two types in the same function
def my_function(a, b, /, *, c, d):  #Any parameters before the '/,' are ONLY positional, any parameters after the *, are KEYWORD
    print(a + b + c + d)
my_function(5, 6, c = 7, d = 8) #(POSITIONAL, POSITIONAL, KEYWORD, KEYWORD)

#Recursion: Method when a function calls itself, very useful to make efficient and quick operations
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)