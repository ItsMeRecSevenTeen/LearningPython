fruits = ["Apple", "Banana", "Cherry"]
for x in fruits:    #for loops does not require an indexing variable to be set beforehand
    print(x)

#Looping through a String
    for x in "Banana":
        print(x)    #It will print each character of the string "Banana"

#The break Statement
for x in fruits:
    print(x)
    if x == "Banana":
        break   #Break the current iteration
for x in fruits:
    if x == "Banana":
        break   #This time, the breakpoint comes before the print
    print(x)

#The continue Statement
for x in fruits:
    if x == "Banana":   
        continue    #Stop the current iteration and continues with the next> Won't print "Banana"
    print(x)

#The range() Function: This function return a sequence of number startin from the 0 by default and ends at a specified
    #number
for x in range(6):  #The real values are from 0 to 6 with 6 not included (From 0 to 5)
    print(x)
#By default the range() function has 0 as a starting value, but we can specify a starting value by adding a new
    #parameter to the arguments
for x in range(2, 6):   #The real values are from 2 to 6 (6 not included)
    print(x)
#By default, the range() function has increment by 1 to the sequence, however, we can specify the increment value
    #by adding a third parameter to the function arguments
for x in range(2, 30, 3):   #range(Starting index, Ending index, number of increments per iteration)
    print(x)

#Else in For Loop: Specifies a block code to be executed when the loop is finished
for x in range(6):
    print(x)
else:   #The 'else' block will NOT be executed if the loop is stopped by a 'break' statement>See example below
    print("Finally Finished")
for x in range(6):
    if x == 3: 
        break   #Breaks the current iteration, in this case, when x is equals to 3
    print(x)
else:
    print("Finally Finished!")  #Due the 'break' statement, this code block won't be executed, because this code block
        #only will be executed once the entire loop is finished
    
#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#The pass Statement> for loops cannot be empty, but if we for some reason have a for loop with no content, use 'pass'
    #To avoid getting an error
for x in [0, 1, 2]:
    pass