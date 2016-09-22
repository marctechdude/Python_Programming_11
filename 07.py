###
# Create a function that returns a tuple of your favorite foods.
# This function does not receive any arguments.

# first function
def myvar():
    #tuple of favorite foods
    return "Pizza", "Pasta", "Noodles"
print(myvar())
###

print("-----------")

###
# Create a second function that returns the text “--food item-- is one of my favorite foods.”
# Make sure this function includes one argument which will be the food item and remember to use this
# argument with the return text.

# second function
def myvar2(item):
    # old modulo because it's easier
    return "--%s-- is one of my favorite foods." % item
print(myvar2("Pizza"))
###

print("-----------")

###
# Create a third function that has two parts:
# A line of code that creates a new reference to the first function you made, the favorite
# foods list (a reference is like creating a shortcut to the function and the reason you do this
# is that you are not able to directly loop a function but you can loop a reference to the function)

# And a loop that assigns the value of the loop (remember it’s going loop through the list of foods)
# to what will become an argument...because inside the loop is:
# A single print command which calls on the second function (outputs favorite foods) you made
# and passes the argument from the loop to it. The second function will return the text, with the
# included argument value, back to the print command.


#third function
def myvar3():
    # line of code that references first function
    favfoods = myvar()
    # for each tuple in in myvar
    for i in favfoods:
        # print the sentence from myvar2 with tuple as the item
        print(myvar2(i))
# so this should print each tuple as a sentence
print(myvar3())
# why not just use a for loop with list?
###

print("-----------")

###
