##import
import random

debug = True

def main():
    randnum = random.randint(1,100)
    # setting count here as 1 because even if they guessed correctly on the first time, it still took 1 guess, but they
    # "got it on their first guess"
    count = 1
    while True:
        try:
            if debug: print(randnum)
            userinput = input("Guess a number.")
            userint = int(userinput)
            if 100 >= userint >= 1:
                if userint>randnum:
                    print("Your guess is too high")
                    count += 1
                elif userint<randnum:
                    print("Your guess is too low")
                    count += 1
                else:
                    print("You guessed correctly! It took you %s guesses, and your correct guess was %s." % (count, userint))
                    break
            else:
                print("Number not in range")
                continue
        except ValueError:
            print("I didn't understand that, please try again. Perhaps you didn't enter a number?")
            continue

main()