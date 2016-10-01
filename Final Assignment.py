# a quick battleship game


# importing
from random import randint

from math import floor

from time import sleep

# don't really need a class for this but "challenge yourself"
class Settings:
    columns = 0
    rows = 0
    style = ""
    stylemiss = ""
    turns = 0
    bombcost = 0
    bombcount = 0

# debugging toggle (yes this gives you cheats)
debug = False


# making an object
battleBoard = Settings()

# defining number of columns, rows, and styling of the board
# basically just repeated the function over and over again
# will fix this once i figure out a way, but it works for now.
if debug:
    while True:
        try:
            battleBoard.columns = int(input("How many columns would like your board to have?: "))
        except ValueError:
            print("Please input a valid number")
        else:
            break
    while True:
        try:
            battleBoard.rows = int(input("How many rows would like your board to have?: "))
        except ValueError:
            print("Please input a valid number")
        else:
            break
    while True:
        try:
            battleBoard.turns = int(input("How many turns would like to have?: "))
        except ValueError:
            print("Please input a valid number")
        else:
            break
    while True:
        try:
            battleBoard.bombcost = int(input("How much should your bombs cost? "))
        except ValueError:
            print("Please input a valid number")
        else:
            break
    while True:
        try:
            battleBoard.bombcount = int(input("How many bombs would like to have?: "))
        except ValueError:
            print("Please input a valid number")
        else:
            break
    sleep(0.5)

# setting constant variables first
battleBoard.style = "O"
battleBoard.stylemiss = "-"
battleBoard.bombcount = 3
# setting the difficulty
if not debug:
    while True:
        try:
            diff = input("Please enter a difficulty. (easy, normal, hard, hell)")
            if diff.lower() == 'easy':
                battleBoard.columns = 5
                battleBoard.rows = 5
                battleBoard.turns = 15
                battleBoard.bombcost = 3
            elif diff.lower() == 'normal':
                battleBoard.columns = 7
                battleBoard.rows = 7
                battleBoard.turns = 10
                battleBoard.bombcost = 4
            elif diff.lower() == 'hard':
                battleBoard.columns = 10
                battleBoard.rows = 10
                battleBoard.turns = 10
                battleBoard.bombcost = 5
            elif diff.lower() == 'hell':
                battleBoard.columns = 20
                battleBoard.rows = 20
                battleBoard.turns = 10
                battleBoard.bombcost = 7
                battleBoard.bombcount = 1
            # the following else statement is already a fail safe
            else:
                print("You have selected an invalid difficulty. Please try again.")
                sleep(0.5)
                continue
        # a second fail safe in case something goes horribly wrong
        except ValueError:
            print("You have selected an invalid difficulty. Please try again.")
            sleep(0.5)
            continue
        else:
            print("You have selected the %s difficulty. Good luck!" % diff.upper())
            sleep(0.5)
            break
# function to make the board
fullboard = []
# does this as many times as there are rows
for i in range(battleBoard.rows):
    # appends the list with the column (takes the style and multiplies it by column to get 1 row
    fullboard.append([battleBoard.style] * battleBoard.columns)
if debug:
    print(fullboard)
    print("-----------------")
    sleep(0.5)
# function to fix formatting and make the board multiline
def fullrows(boardx):
    for i in boardx:
        print(" ".join(i))
# should print regardless of the state of debug, but won't print twice.
if debug:
    fullrows(fullboard)
    print("-----------------")
    sleep(0.5)

if not debug:
    fullrows(fullboard)
    sleep(0.5)
# random position for computer
battleloccol = randint(0,battleBoard.columns-1)
battlelocrow = randint(0,battleBoard.rows-1)

if debug:
    # added 1 because it starts from 0
    print("Computer's Choices:")
    print(battleloccol+1)
    print(battlelocrow+1)
    print("-----------------")
    sleep(0.5)

if debug:
    fullrows(fullboard)
    print("-----------------")
    sleep(0.5)


turncounter = 0
numturns = battleBoard.turns
# big for loop for turns
while numturns > 0:
    turnsremain = int((battleBoard.turns-turncounter)-1)
    ### after riley tried meticulously to break my code, I decided to include a fail safe
    while True:
        try:
            userguess = input("What column,row is your guess? Please give the coordinates in the 'x,y' format: ")
            # parsing text
            # takes userguess and converts it to a list (because of the [])
            # ie. userguess = '3,2' becomes ['3,2']
            # then it splits it from the comma (',')
            # so userguess = ['3','2']
            # then it takes each index in ['3','2'] (which is userguess) and converts it to a number (the for loop and int(i))
            # then it takes the integer and assignes it to the variables, in this case it's ux and uy
            ux,uy = [int(i)-1 for i in userguess.split(",")]
            sleep(0.5)
        # if there's an error
        except ValueError:
            # try again
            print("Sorry, I didn't understand that. Please try again, and remember to use proper formatting (eg '1,5')")
            sleep(1)
            continue
        else:
            # coordinates successfully parsed
            break
    if debug:
        print("User Guesses:")
        print(ux+1)
        print(uy+1)
        print("-----------------")
    # simple if statement to see if userguess and computer guess match
    if ux == battleloccol and uy == battlelocrow:
        print("Congrats! You win")
        fullboard[uy][ux] = "X"
        fullrows(fullboard)
        break
    # check to see if position is on map
    if uy >= battleBoard.rows or ux >= battleBoard.columns or ux < 0 or uy < 0:
        print("Your selected position is not on the board. Please pick a new position or increase the size of the board.")
        sleep(1)
        continue
    # check to see if they already guessed that position
    elif fullboard[uy][ux] == "-":
        print("You already picked this position. Please try again")
        sleep(1)
        continue
    # replace userguess with miss styling if it's incorrect
    else:
        fullboard[uy][ux] = battleBoard.stylemiss
        print("You missed!")
        sleep(1)
    # print turns
    if not turnsremain == 0:
        print("Turns Remaining: %d" % turnsremain)
        sleep(1)
    else:
        print("You lose!")
        sleep(1)
    turncounter += 1
    numturns -= 1
    # printing the damn thing
    fullrows(fullboard)
    ### End of code