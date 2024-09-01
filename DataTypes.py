"""Python has data types built-in by default
text Type: str      Numeric Types: int, float, complex      Sequence Types: list, tuple, range
Mapping type: dict   Set Types: set, frozenset      Boolean Type: bool
Binary Types: bytes, bytearray, memoryview          None Type: noneType"""
#getting the Data Type
x = 17
print(type(x))#It returns the Data Type, in this case, of the variable named x
#Setting the Data Type
#The data type is set when we assign a value to variables
x = "Hello World"   #str Type
x = 20              #int Type
x = 20.5            #float Type
x = 1j              #complex Type
x = ["Apple", "Banana", "Cherry"]   #list Type 
x = ("Apple", "Banana", "Cherry")   #tuple Type
x = range(6)        #range Type
x = {"name" : "Rich" , "age" : 17}  #dict Type
x = {"Apple", "Banana", "Cherry"}     #set Type
x = frozenset({"Apple", "Banana", "Cherry"})    #frozenset Type
x = True            #bool Type
x = b"Hello"        #bytes
x = bytearray(5)    #bytearray Type
x = memoryview(bytes(5))            #memoryview Type
x = None            #NoneType
#Setting the Specific Data Type
#Useful If we want to specify the Data Type
x = str("Hello World")  #str
x = int(20)             #int
x = float(20.5)         #float
x = complex(1j)         #complex
x = list(("Apple", "Banana", "Cherry"))     #list
x = tuple(("Apple", "Banana", "Cherry"))    #tuple
x = range(6)            #range
x = dict(name = "Rich", age = 18)           #dict
x = set(("Apple", "Banana", "Cherry"))      #set
x = frozenset(("Apple", "Banana", "Cherry"))#frozenset
x = bool(5)             #bool
x = bytes(5)            #bytes
x = bytearray(5)        #bytearray
x = memoryview(bytes(5))#memoryview