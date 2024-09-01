class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

#Create a Child Class
class Student(Person):  #The class Student has the same methods and attributes than Person Class
    pass    #Use the 'pass' keyword when we do not want to add any other properties or methods to the class

x = Student("Mike", "Olsen")
x.printname()

#Adding the __init__() Function
class Student(Person):
    def __init__(self, fname, lname):   #If we add the init() function to the child class, this will no longer inherit the
        #Parent's init() Function, Child class will have it's own init() function
        pass
#To keep the inheritance of the parent's init() function, add a call to the parent's init()
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

#Use the super() Function: This function will make the child class inherit all the methods and properties from it's parent
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  #Automatically will inherit the methods and properties

#Adding properties
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019
#Doing the same thing but using __init__() function:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = Student("Mike", "Olsen", 2019)

#Add Methods
class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Ricardo", "Gomez", 2023)
x.welcome()