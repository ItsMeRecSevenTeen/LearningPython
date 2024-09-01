#A lambda function is a small anonymous function> a lambda function can take any number of arguments, but can only
    #have one expression followed by the syntax: lambda arguments : expression
    #Lambda functions are useful when we want to make simple operations or we need temporary functions to perform operations
    #in a short period of time
x = lambda a : a + 10   #Results are returned
print(x(5))
#Lambda functions can take any number of arguments
x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b ,c : a + b +c
print(x(5, 6, 2))

#Why Use Lambda Functions? > We can use Anonymous Functions (Lambda functions) inside another function, E.G: A number doubler
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)   #n is the argument two (2)
mytripler = myfunc(3)   #>We can create any functions with the same function definition
print(mydoubler(11))    #a is the argument eleven (11)
print(mytripler(11))    #>