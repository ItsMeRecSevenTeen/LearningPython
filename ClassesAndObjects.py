#Create a Class
class MyClass:
    x = 5
#Create Object
p1 = MyClass()  #Creates an object called p1 using the constructor MyClass()
print(p1.x) #Prints the value of x from the object 1

#The _init_() Function: It is the constructor for the objects, initializes the attributes each time we create an object
class Person:
    def __init__(self, name, age):  #The fucntion __init__() assign or initialize values to object properties, this function
            #is always executed when the class is being initiated
        self.name = name
        self.age = age
p1 = Person("John", 36) #__init__() is called automatically every time the class is being used to create a new object
print(p1.name)  #Prints the attribute "name" of the object 'p1' INITIALIZED by __init__() function
print(p1.age)   #Prints the attribute "age" of the object 'p1' INITIALIZED by __init__() function

#The __str__() Function:Controls what should be returned when the class object is representes as a string
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):#The friendly representation of our created objects
        #We can return a string with the attributes of our objects when we print it in form of string in the console
        return f"{self.name} is {self.age} years old"   #String formatting
    
p1 = Person("John", 36)
print(p1)

#Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):   #We can define functions inside the class, those defined functions will belong to the objects created
            #from the class
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#The 'self' Parameter> 'self' parameter is a reference to the current instance of the class, and is used to access variables
    #that belongs to the class> However, it does not have to be called 'self', we can use any word BUT, must be the 
    #first parameter in any function in the class
class Person:
    def __init__(selfObject, name, age):#selfObject works like 'self' parameter
        selfObject.name = name
        selfObject.age = age
    def myfunc(abc):    #abc works like 'self' parameter
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Modifying Object Properties: We can modify properties on objects
p1.age = 40
#nameOfObject.AttributeOfObject = value

#Deleting Object Properties: We can delete properties on objects using the 'del' keyword
del p1.age

#Deleting Objects: We can delete entire objects using the 'del' keyword
del p1

#The pass Statement: Classes cannot be empty, but if for some reason we have an empty class, we can use the 'pass' keyword
    #to avoid getting an error
class Person:
    pass