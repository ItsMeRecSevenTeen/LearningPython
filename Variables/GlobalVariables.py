#Every variable created outside of a function are known as GLOBAL VARIABLES
x = "Awesome"#x is global, and every function can use it
def myfunc():
    x = "fantastic"#Local Variable: it can be used only inside of this function
    print("Python is " + x)#Outputs: "Python is fantastic"
myfunc()
print("Python is " + x)#Outputs: "Python is Awesome"

#'Global' Keyword
y = "perfect"
def myotherfunc():
    global z#Creates a global variable named x, we can use the 'global' keyword inside of a function
    global y#Refering the global variable named y
    y = "excelent"#Reassigning a new value to y: "perfect" to "excelent"
    z = "fantastic"
myotherfunc()
print("Python is " + z)
print("Python is " + y)