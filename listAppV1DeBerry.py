"""
Program Goals:
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INTs from StRs
3. We need to provide choices to the user
    a. Add more values to the list
    b. Return a value a speciftic index
"""
import random
myList = []
uniqueList = []

def mainProgram():
    #build a while loop here!
    while True:
        try: 
            print("Hello, there! Lets work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""1. Add to list ,
2. Add a bunch of numbers,
3. Return the value at an index,
4. Random Search,
5. Linear Search,
6. Recursive Binary Search,
7. Iterative Binary Search
8. Sort list,
9. Print contents of list
10. Exit program.  """)
            #add a way to catch bad user responses
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                searchItem = input("What are you looking for?  ") 
                recursiveBinarySearch(uniqueList, 0, len(uniqueList)-1, int(searchItem))
            elif choice == "7":
                searchItem = input("What are you looking for?  ") 
                result = iterativeBinarySearch(uniqueList,  int(searchItem))
                if result != -1:
                    print("Your number is at index {}".format(result))
                else:
                    print("Your number isn't in this list!")
            elif choice == "8":
                sortList(myList)
            elif choice == "9":
                printList()
            
            else:
                break
            
        except:
                print("You made a whoopsie!")

    #TO ADD: 1. a way to loop the action, 2. a way to quit, 3. think of repetition

def addToList():
    print("Adding to list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("How many new integers would you like to add?")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")

def indexValues():
    print("Ohhh! I heard you a particular piece of data!")
    indexPos = input("What index position are you curious about?  ")
    print(myList[int(indexPos)])

def sortList(myList):
    print("A little birdy told me you needed some data")
    for x in myList:
        if x not in uniqueList:
            uniqueList.append
    uniqueList.sort()
    showMe = input("Wanna see your new list?  Y/N")
    if showMe.lower() == "y":
        print(uniqueList)

def randomSearch():
    print("RaNDoM SeaRCH!")
    print(myList [random.randint(0, len (myList)-1)])

def linearSearch():
    print("We're gonna check out each item one at a time in your list! this sucks.")
    searchItem = input("What you lookin for pardner?  ")
    for x in range(len(myList)):
        print("Your item is at index posistion {}".format(x))

def recursiveBinarySearch(uniqueList, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if uniqueList[mid] == x:
            print("You ding dang found it at index position {}".format(mid))
            return mid
        elif uniqueList[mid] > x:
            return recursiveBinarySearch(uniqueList, low, mid -1, x)
        else: recursiveBinarySearch(uniqueList, mid + 1, high, x)
    
    else:
        print("Your number isn't here!")

def iterativeBinarySearch(uniqueList, x):
    low = 0
    high = len(uniqueList)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if uniqueList[mid] < x:
            low = mid + 1
        elif uniqueList[mid] > x:
                high = mid - 1
        else:
            return mid
        return -1

def printList():
    if len(uniqueList) == 0:
        print(myList)
    else:
        which0ne = input("Which list? sorted or unsorted?  ")
        if Which0ne.lower() == "sorted":
            print(uniqueList)
        else:
            print(myList)

#dunder main -> Double Underscore---dunder
if __name__ == "__main__":
    mainProgram()
