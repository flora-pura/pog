# program goals
# create a random number generator
# interfacing with the user by:
# 1. asking questions
# 2. delivering rolls to user
# roll multiple times
# display toltal rolls and highest/lowest

import random

print("dice rolling v. 1.0")
print("what kind of die do you want to roll?")
dieType = input("type d20, d12, d8, d6, d4:    ")
rollCount = input("how many times should i roll?")
rollTotal = 0
print("*shakes dice*")

if dieType == 'd20':
    rollTotal = (random.randint(1,20) * int(rollCount))
    print (rollTotal)

elif dieType == 'd12':
    rollTotal = (random.randint(1,12) * int(rollCount))
    print (rollTotal)

elif dieType == 'd8':
    rollTotal = (random.randint(1,8) * int(rollCount))
    print (rollTotal)

elif dieType == 'd6':
    rollTotal = (random.randint(1,6) * int(rollCount))
    print (rollTotal)

elif dieType == 'd4':
    rollTotal = (random.randint(1,4) * int(rollCount))
    print (rollTotal)

else:
    print("please choose a die i have.")
