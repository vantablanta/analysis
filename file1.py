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