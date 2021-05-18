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

#we can also formatt using indexes to reaarrange the order of the varibles 
cakes = 4
sweets = 10
snacks = 4 * 10
second_message =   "I have {1} sweets which makes a total of {2} snacks and {0} cakes ".format(cakes, sweets, snacks )

print (second_message)

#format using keys 
cakes = 4
sweets = 10
snacks = 4 * 10
second_message =   """I have {s} sweets which makes a total of {s2} snacks
and {c} cakes """.format(c=cakes, s=sweets, s2 =snacks )
print (second_message)

#formatiing using aukto spacing
price = 20
number  = 10
total = number * price 
message = "\n{txt_price:<30} => {pri}\n{txt_num: <30} => {num}\n{txt_total: <30} => {tot}"


print(message.format(txt_price = "Price of single item", 
pri = price, txt_num = "Number of items",num = number, txt_total = "Total price of items", tot = total))

#using f strings 
message1 = f"\nIndividual price of the items is {price}"
message2 = f"Total price of all the items is {price * number }"

print(message1)
print (message2)

#multiline f strings

greeting, name, proffesion = "Hello everyone", " Michelle", " software developer"

message = (
    f"\n{greeting}\n"
    f"My name is {name}\n"
    f"I am a {proffesion}"
)
print (message)
message = (
f"""\n{greeting}
My name is {name}
I am a professional{proffesion}
"""
)
print (message)
# string formatting 
cats,dogs, guinea_pigs = 3, 5, 10 
message = f"The animals hosted in a shelter are {cats} cats, {5} dogs, {10} guinea pigs "
message = "The animals hosted ina shelter are {} cats, {} dogs and {} guinea pigs ".format(cats, dogs, guinea_pigs)
#message20 = "{intro: < 30}\n{c_name: < 30} =>{c}\n{d_name: < 30} =>{d}\n{g_name: < 30} =>{g}"
print (message)
print (message)
#print (message20.format(intro  = "The animals hosted in a shelter are :", 
#c_name="Cats", c=cats, d_name="Dogs", d=dogs, g_name = "Guinea pigs", g = guinea_pigs)) 

total_money = 1000000
total_friends = 5
money_each_friend_gets = total_money / total_friends
message = f"\nEach friend is going to get {total_money} divided by {total_friends} which is equivalent to {money_each_friend_gets}" 
print(message)

cat_age = 5 #5 human years 
dog_age = 3 #7 human years 
cat_to_human = 5 
dog_to_human = 7
message1 = f"The cat is {cat_age * cat_to_human }  human years"
message2 = f"The dog is {dog_age * dog_to_human} human years"

print (message1)
print(message2)

#string functions split()

text = "Hey its so nice to finally meet you "
words = text.split(" ") #result is a list
print(words)

#upper method transforms the message to allcaps 
print (text.upper())
#lower method tranforms the message all lower case 
print (text.lower())
#replace method replaces sth in the text with another letter 
print (text.replace("H", "M"))
# you can specify if you wish to replace all occurences of a letter or only certain occurences.
print(text.replace("y" ,"l", 2))
#find method returns the index of the first occurence of the letter in a word 
print(text.find("meet"))# returns the index of the first letter of the word meet.
#len funtion retunr the length of the string
print(len(text))

input = "My cat is the cutest cat out of all the cats I have seen"
print(input.replace("cat", "dog"))
input = "Look, john and mary are walking down the street"
new_input = input.replace('john', 'John').replace('mary', 'Mary')
print(new_input.find("John"))
print(new_input.find("Mary"))
#replace function 
my_string = "I love my cat, cat and cat."
string1 = my_string.replace('cat', 'dog', 1)
string2 = string1.replace('cat', 'parrot', 1)
string3 = string2.replace('cat', 'hamster', 1)
print(string3)