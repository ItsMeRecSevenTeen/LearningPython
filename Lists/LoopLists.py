#Loop Through a List
thislist = ["Apple", "Banana", "Cherry"]
for x in thislist:
    print(x)

#Loop Through the Index Numbers with for
for i in range(len(thislist)):
    print(thislist[i])  #The iterable i is [0, 1, 2]

#Loop through the Index Numbers with while
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#Looping Using List Comprehension
[print(x) for x in thislist]