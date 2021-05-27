from tkinter import *
import random

top = Tk()
playlist = []
myRolls = []
shoppingListYAY = []


def printList():
    print(playlist)

def exportPlaylist():
    with open('playlist.txt', 'w') as f:
        for song in playlist:
            f.write("%s\n" % song)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text="Block 5 GUIs")
    LMain.grid(column = 0, row = 1)
    
    B1Main = Button(text = "Week 1", bg = "#E1FFFC", command = week1)
    B1Main.grid(column = 0, row = 2)

    B2Main = Button(text = "week 2", bg = "#E1FFFC", command = week2)
    B2Main.grid(column = 0, row = 3)
    
    B3Main = Button(text = "week 3", bg = "#E1FFFC", command = week3)
    B3Main.grid(column = 0, row = 4)

def shoppingList():
    print(shoppingList)

def week1():

    def addSong():
        playlist.append(E1.get())
        E1.delete(0, END)

    clearWindow()
    #this is a lable widget
    L1 = Label(top, text="Add your songs!")
    L1.grid(column = 0, row = 1)

    #this is a text entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #this is a button widget
    B1 = Button(text=" + ", bg = "#B4E9FF", command = addSong)
    B1.grid(column = 1, row = 2)

    B2 = Button(text = "Print List", bg = "#D9B1FF", fg = "white", command = printList)
    B2.grid(column = 0, row = 3)

    B3 = Button(text = "Export List", bg = "#FFD4FE", command = exportPlaylist)
    B3.grid(column = 1, row = 3)

    
    Bclear = Button(text = "Main Menu", bg = "purple", command = mainMenu)
    Bclear.grid(column = 1, row = 4)

def week2():
    def rollDice():
        #access the entry data
        rollTimes = E2W2.get()
        dieType = E1W2.get()
        
        #clear the window
        clearWindow()
        
        #perform the dice roll calculations
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
            
        #display the results with two labels and a button that goes to main menu
        L1RD = Label (top, text= "Here's your rolls!")
        L1RD.grid(column= 0, row=1)
        
        L2RD = Label (top, text = myRolls)
        L2RD.grid(column= 0, row=2)
        
        B1RD = Button (text= "Main Menu", bg = "yellow", command = mainMenu)
        B1RD.grid(column= 0, row= 3)
        

        
    clearWindow()

    L1W2 = Label(top, text= "Dice Roller App")
    L1W2.grid(column=2, row= 1)
    
    L2W2 = Label(top, text= "# of Sides")
    L2W2.grid(column=0, row= 2)
    
    L3W2 = Label(top, text= "# of Rolls")
    L3W2.grid(column=3, row= 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column=0, row= 3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column=3, row= 3)

    B1W2 = Button(text="roll 'em", bg = "yellow", command = rollDice)
    B1W2.grid(column=2, row= 4)
    #dont forget .grid()


def week3 ():
    def shoppingList():
        shoppingListYAY.append(E1W3.get())
        E1W3.delete(0, END)

    clearWindow()
    #this is a lable widget
    L1W3 = Label(top, text="What's on your shopping list?")
    L1W3.grid(column = 0, row = 1)

    #this is a text entry widget
    E1W3 = Entry(top, bd = 5)
    E1W3.grid(column = 0, row = 2)

    #this is a button widget
    B1W3 = Button(text=" + ", bg = "#82FFBF", command = shoppingList)
    B1W3.grid(column = 1, row = 2)

    B2W3 = Button(text = "Print List", bg = "#82FFF4", command = printGroceryList)
    B2W3.grid(column = 0, row = 3)
    
    BclearW3 = Button(text = "Main Menu", bg = "#82DBFF", command = mainMenu)
    BclearW3.grid(column = 1, row = 4)

    

    


if __name__ == "__main__":
    mainMenu()
    top.mainloop()
