import random
import string
def get_word():
    ## shortcut to get a bunch words, too lazy
    words = "Coding Task: Create your own Hangman game. After watching the tutorial, create your own game but make " \
            "sure to change the words. Include at least 30 words. Have your friends try your game! Please ensure that" \
            " before beginning your own game you fully understand each of the functions in the game, including"
    # make everything uppercase
    # remove punctuation
    # split it up into an iterable list
    # choose a random one
    # return it
    return random.choice(words.upper().translate(string.punctuation).split())

def check(word, guesses, userguess):
    userguess = userguess.upper()
    status = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'
        if letter == userguess:
            matches += 1

    if matches > 1:
        print("Correct. The word contains {} '{}'s" .format(matches, userguess))
    elif matches == 1:
        print("Correct. The word contains the letter '{}'" .format(userguess))
    else:
        print("Sorry, the word does not contain the letter '{}'" .format(userguess))

    return status

def main():
    word = get_word()
    guesses = []

    print("The word contains {} letters." .format(len(word)))
    print("*" * len(word))
    while True:
        userguess = input("Please enter one letter or a {}-letter word. " .format(len(word)))
        userguess = userguess.upper()
        if userguess in guesses:
            print("You already guessed '{}'!" .format(userguess))
        elif len(userguess) == len(word):
            guesses.append(userguess)
            if userguess == word:
                print("Yes, the word is '{}'. You got the answer in {} tries." .format(word, len(userguess)))
                break
            else:
                print("Sorry, that guess is incorrect")
        elif len(userguess) == 1:
            guesses.append(userguess)
            result = check(word,guesses,userguess)
            if result == word:
                print("Yes, the word is '{}'. You got the answer in {} tries." .format(word, len(userguess)))
                break
            else:
                print(result)
        else:
            print("Invalid Entry")
main()
