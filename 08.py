###
# all variables for Car1
class Car1:
    name = "Fer"
    cost = 60000
    color = "red"
    type = "convertible"
    def message(self):
        print("This is Car1")

# all variables for Car2
class Car2:
    name = "Jump"
    cost = 10000
    color = "blue"
    type = "van"
###

print("-----------")

###
# assigning both classes to variables
mycar1 = Car1()
mycar2 = Car2()
# outputting name and cost of car 1 without using the variables
print(Car1.name)
print(Car1.cost)
# outputting name and cost of car 1 WITH the variables
# this is done just for the sake of showing both methods
print(mycar1.name)
print(mycar1.cost)
###

print("-----------")

###
# assigning a new value to the variable outside of the class
Car1.cost = 70000
print(Car1.cost)
###

print("-----------")

###
# printing car2's name before changing it
print(Car2.name)
Car2.name = "Van"
print(Car2.name)
# printing car2's name after changing it to show how python reads code line by line
###

print("-----------")

###
# printing function
# Note: You MUST use a variable assigned to a class here. 'Car1.message()' will not work here!
mycar1.message()