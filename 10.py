import random

## function for rolling dice
def roll(sides):
    ## assign random int to a variable between 1 and 6
    num = random.randint(1,6)
    return num

def main():
    while True:
        userinput = input("Press 'RETURN' to roll or type 'q' to quit.")
        sides = 6
        if userinput.lower() != "q":
            print("You rolled %s. "% roll(sides))
        else:
            break
        print("Thanks for playing")

main()