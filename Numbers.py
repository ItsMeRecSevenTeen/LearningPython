x = 17  #int
y = 2.8 #float
z = 1j  #complex
#Get the Data Type
print(type(x))
print(type(y))
print(type(z))
#Int Type: Whole number, positive or negative, without decimals, of unlimited length
x = 1
y = 6581984198411546
z = -35
#Float Type: Number, positive or negative, contains one or more decimals
x = 1.10
x = 1.0
x = -35.68
x = 35e3    #A Float number can be a scientific number with an "e", indicating "The power of 10"
x = 12E4
x = -87.7e100
#Complex Type: Numbers written with a "j" as the imaginary part
x = 3+5j
y = 5
z = -5j
#Type Conversion
x = 1
y = 2.8
z = 1j
a = float(x)#From int to float
b = int(y)#From float to int
c = complex(x)#From int
#Note: I cannot convert complex numbers into another number type
#Random Number
import random#Import the module random to make random numbers
print(random.randrange(1, 10))#Prints a random number between 1 and 9