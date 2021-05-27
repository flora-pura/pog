"""
program goals:
1. roll a specified die a certain number of times
2. store rolls in a list
3. display: sum total of, highest roll, lowest roll
4. program run till user quits
"""

import random

def diceEngine():
    myRolls = []
    while True:
        dieType = input("how many sides does your dice have?:    ")
        rollTimes = input("how many times should i roll?   ")
        print("*shakes dice*")

        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        print ("here are my rolls: {}".format(myRolls))
        print ("your roll total is: {}".format(sum(myRolls)))
        print ("your highest roll was: {}".format(max(myRolls)))
        print ("your your lowest roll was: {}".format(min(myRolls)))

        myRolls.clear()

        #how do we use "break" to exit
        #how can we use inputs and an if statement to ask the user to quit?

        playerQuit = input("do you want to quit? Y/N    ")
        if playerQuit.lower() == "y":
            break


if __name__== "__main__":

    diceEngine()



if __name__== "__main__":

    diceEngine()
