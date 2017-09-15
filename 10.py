import random

## function for rolling dice
def roll(sides):
    ## assign random int to a variable between 1 and 6
    num = random.randint(1,6)
    return num

def main():
    ## always loop
    while True:
        ## get userinput
        userinput = input("Press 'RETURN' to roll or type 'q' to quit.")
        ## set sides
        sides = 6
        ## check if they typed q
        if userinput.lower() != "q":
            print("You rolled %s. "% roll(sides))
        else:
            break
        print("Thanks for playing")

main()