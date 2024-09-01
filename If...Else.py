#elif: it is the abreviation to the sructure else if, it means "if the previous conditions were not true, try this one"
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#else: this keyword catches anything wich was not caught by the preceding conditions
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
#Also, we can use the 'if statement' without 'elif'
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#Short Hand If: If we have only one statement to execute, we can put it on the same line as the if statement
if a > b: print("a is greater than b")

#Short Hand If: If we have only one statement to execute, one for if, and one for else, put it all on the same line
a = 2
b = 330
print("A") if a > b else print("b")
    #We can use the same technique for multiple statements
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#And>'and' keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c < a: #First condition is True BUT the second one is False, so does nothing because one of them is False
    print("Both condition are True")

#Or>'or' keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:#First condition is True BUT the second one is False, However, it will print the True code block
    print("At least one of the conditions is True")

#Not>'not' keyword is a logical operator,and is used to reverse the result of the conditional statement:
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

#Nested If: We can have if statement inside if statements, this is called nested if statements
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#The pass Statement: if statements cannot be empty, but if you for some reason have an if statement with no content,
    #Put in the 'pass' statement to avoid getting an error.
a = 33
b = 200
if b > a:
    pass    #To avoid errors