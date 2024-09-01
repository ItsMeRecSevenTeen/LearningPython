x = 25
y = 17
#Arithmetic Operators
x + y   #Addition Operator
x - y   #Subtraction Operator
x * y   #Multiplication Operator
x / y   #Division Operator
x % y   #Modulus Operator
x ** y   #Exponentiation Operator
x // y  #Floor Division Operator
#Assignment Operators
x = 3   #Same as x = y
x += 3  #Same as x = x + 3
x -= 3  #Same as x = x - 3
x *= 3  #Same as x = x * 3
x /= 3  #Same as x = x / 3
x %= 3  #Same as x = x % 3
x //= 3 #Same as x = x // 3
x **= 3 #Same as x = x ** 3
x &= 3  #Same as x = x & 3
x |= 3  #Same as x = x | 3
x ^= 3  #Same as x = x ^ 3
x >>= 3 #Same as x = x >> 3
x <<= 3 #Same as x = x << 3
#Comparison Operators
x == y  #Equal
x != y  #Not Equal
x > y   #Greater Than
x < y   #Less Than
x >= y  #Greater than or Equal to
x <= y  #Less than or Equal to
#Logical Operators
x < 5 and x < 10    #True if both statements are True
x < 5 or x < 4      #True if one of the statements are True
not(x < 5 and x < 10)   #Reverse the result, It will be False if the result is True
#Identity Operators
x is y  #Returns True if both variables are the same object
x is not y  #Returns True if both variables are not the same object
#Membership Operator
x in y  #Returns True if a sequence with the specified value is present in the object
x not in y  #Returns True if a sequence with the specified value is not present in the object
#Bitwise Operators
x & y  #AND: Sets each bit to 1 if both bits are 1
x | y   #OR: Sets each bit to 1 if one of two bits is 1
x ^ y   #XOR: Sets each bit to 1 if one one of two bits is 1
~x   #NOT: Inverts all the bits
x << 2  #Zero fill left shift: Shift left by pushing zeros in from right and let the leftmost bits fall off
x >> 2  #Signed right shift: Shift right by pushing copies of the leftmost bit in from the left, and let
        #the rightmost bits fall off
#Operator Precedence:Describes the order in wich operation are performed
print((6 + 3) - (6 + 3))    #6 + 3 are evaluated first, then the subtraction
print(100 + 5 * 3)  #Multiplication has higher precedence than addtion, * is evaluated first, then the +
#Precedence Order
"""()       #Parentheses
**          #Exponentiation
+x -x ~x    #Unary Plus, Unary Minus, and Bitwise NOT
* / // %    #Multiplication, Division, Floor Division, and Modulus
+ -         #Addition and Subtraction
<< >>       #Bitwise left and right shifts
&           #Bitwise AND
^           #Bitwise XOR
|           #Bitwise OR
== != > 
>= < <=
is is not 
in not in   #Comparisons, identity, membership operator
not         #Logical NOT
and         #AND
or          #OR
"""
print(5 + 4 - 7 + 3)#If two operators have the same precedence, the expession will be evalued from left to right