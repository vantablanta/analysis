print ("Hello World!")
#This is a comment
print ('Hi Michelle')
#this is a second comment 
print (2021 - 1996)
print("hello" + "john")
#multiline strings
print("""
First Line 
Second Line 
Third Line 
""")
#escaped characters
print("hello \n World")#newline
print("hello \t world")#tab
print ("hello \\ world")#to show the backlash as a string

print ("Hello Michelle")

print ("There are two types os slashes: \\ and /")

print ("\n\t This is a tabbed line \n This is a newline")
print ("""
(\\(\\
(-.-)
o_(\") (\")
""")

print("""
Roses are red 
Violets are \\blue/
I love \\\\Python//
And I hope you do too!\U0001F601
""")

dogs = 3
cats = "Many fluffy cats"

print (cats)
print (dogs)

name = "Michelle"
message = "Hello"
age = 5

print ( name + " "+ message)

print (age * dogs)
print (age + dogs)

dogs = 2 #new assingment of the dogs variable 
print(dogs)
print (age + dogs) #works with the new value of dogs 

cats, dogs, rabbits = 5, 2 , 3
print (rabbits)

product_amount = 20
product_price = 25

total_price = product_amount * product_price

print (total_price)

radius = 16
pi = 3.14159
area = pi * radius * radius

print (area)

product_cost = 20
print ("The cost of the produtc is {}" .format(product_cost))
#string formating making the the number able tobe printed with a strring

#adding multiple things to be formatted 
dresses = 2
houses = 1
cups = 4
new_message = "I have {} dresses with {} house and {} cups".format(dresses, houses, cups) 
print (new_message)

#we can also formatt using indexes to rea arrange the order of the varibles 
cakes = 4
sweets = 10
snacks = 4 * 10
second_message =   "I have {1} sweets which makes a total of {2} snacks and {0} cakes ".format(cakes, sweets, snacks )

print (second_message)

cakes = 4
sweets = 10
snacks = 4 * 10
second_message =   """I have {s} sweets which makes a total of {s2} snacks
and {c} cakes """.format(c=cakes, s=sweets, s2 =snacks )
print (second_message)





