#undesrstanding errors 
#1. synatx error  - occurs because of the wrong syntax pyhton cant understand what you are saying 
#2. runtime error -error that ocurs after the code is run 
#. logic error - the program runs well but doesnt excute what you want it to

#Debug this program so that it prints out the number of seconds in a week
# goal: print out the number of seconds in a week 
secondsPerMinute = 60
secondsPerHour = secondsPerMinute * 60 # todo: check this!
secondsPerDay = secondsPerHour * 24
daysPerWeek = 5
daysPerWeek = daysPerWeek + 2 # weekends are disabled!?
print(secondsPerDay * daysPerWeek)

#Write a program which reads an integer from input using pancakes = int(input()). 
#If pancakes is more than 3, print out Yum! 
# and if pancakes is not more than 3, print out Still hungry! instead.
pancakes = int("10")
if pancakes > 3 :
   print("Yum!")
if pancakes < 3 :
   print("Still Hungry!")
 


timbitsLeft = int(input()) # step 1: get the input
totalCost = 0              # step 2: initialize the total cost

# step 3: buy as many large boxes as you can
bigBoxes = int(timbitsLeft / 40)
totalCost = totalCost + (bigBoxes * 6.19)    # update the total price

if bigBoxes == 0:
   timbitsLeft = (timbitsLeft - 40)   # calculate timbits still needed
else:
        timbitsLeft = (timbitsLeft - 40) * bigBoxes
if timbitsLeft >= 20:                # step 4, can we buy a medium box?
    totalCost = totalCost + 3.39
    timbitsLeft = timbitsLeft - 20
if timbitsLeft >= 10:                # step 5, can we buy a small box?
    totalCost = totalCost + 1.99
    timbitsLeft = timbitsLeft - 20

totalCost = totalCost + (timbitsLeft * 0.20) # step 6
print(totalCost)                         # step 7
