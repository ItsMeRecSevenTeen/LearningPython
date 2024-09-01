#Strings are surrounded by either single quotation mark, or double quotation marks
a = "Hello"#Is the same as the next code line
a = 'Hello'
#Multiline Strings
#The line
a = """Hello, This is a multiline
string value, and we are assigning it
to the variable named 'a'"""#It can be with Three Double Quotes or Three Single Quotes
#Strings are Arrays     In Python there's not char data types
a = "Hello World!"
print(a[1])#Accessing to the second character of the string "Hello World!", outputting 'e'
#Looping Through a String
for x in "Banana":
    print(x)
#String length
print(len(a))#Outputs 12
#Checking String
txt = "The best things in life are free!"
print("free" in txt)#Checks if a certainf phrase of character is in a string    Outputs True
if "free" in txt:
    print("Yes, 'free' is in the String")
#Check if NOT
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No. 'Expensive is NOT present")