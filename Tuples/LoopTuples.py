#Looping through a Tuple
thistuple = ("Apple", "Banana", "Cherry")
for x in thistuple:
    print(x)

#Looping through the Index Numbers
for i in range(len(thistuple)):
    print(thistuple[i])
#Using a While Loop
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1