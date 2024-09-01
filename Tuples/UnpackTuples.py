#When we create a tuple, we normally assign values to it, This is called 'Packing'
fruits = ("Apple", "Banana", "Cherry")
    #Python allow us to extract the packed values into variables, This is calles 'Unpacking'
(green, yellow, red) = fruits   #Variable green has the value Apple, yellow has the value Banana...
print(green, yellow, red)

#Using Asterisk *
#If the number of variables does not match with the number of values, we can use an asterisk to collect
    #the remaining data to the last variable
fruits = ("Apple", "Banana", "Cherry", "Strawberry", "Raspberry")
(green, yellow, *red) = fruits  #variable 'red' will collect the remaining values from the tuple 'fruits'
    #But will be a list data type
print(green, yellow, red)
#If the asterisk is added to another variable than the last, Python will assign the values to the variable
    #until the number of values left matches the number of variable left
fruits = ("Apple", "Mango", "Papaya", "Pineapple", "Cherry")

(green, *tropic, red) = fruits #Green has 'Apple', tropic has Mango, Papaya and Pineapple items, red has Cherry
print(green, tropic, red)