#age = 17
#txt = "My name is Rich, and I am " + age   #Ilegal way to concatenate Strings and Numbers
age = 17
txt = "My name is Rich, and I am {}" #Legal way to concatenate Strings with Numbers
print(txt.format(age))#format() method takes unlimited arguments, and are placed into the respective {}

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."#quantity goes first, itemno as second, and price as third
print(myorder.format(quantity, itemno, price))
#we can use index numbers in placeholders to be sure the arguments are placed correctly
myorder = "I want to pay {2} dollars for {0} pieces of item {1}" #price '2', quantity '0', itemno '1'
print(myorder.format(quantity, itemno, price))
