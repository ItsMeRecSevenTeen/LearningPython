i = 1
while i < 6:
    print(i)
    i +=1   #While Loops always need initialized variables

#The break Statement
i = 1
while i < 6:
    print(i)
    if i ==3:
        break   #we can stop the loop even if the while condition is true
    i += 1

#The continue Statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue#We can stop the current iteration to continue with the next one>   Won't print 3
    print(i)

#The else Statement
i = 1
while i < 6:
    print(i)
    i += 1
else:   #We can run a block of code once when the condition no longer is true
    print("i is no longer less than 6")
