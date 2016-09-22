# Empty List
mylist = []
#set count to 0
count = 0
# start function that counts from 0 to 15
for i in range(0,16):
    # write count to list and increase count by 1
    mylist.append(count)
    # not sure what "(output will be on separate lines)" means so i'm just going to print
    # the number here
    print(count)
    count += 1
# output list
print(mylist)
###

print("-----------")

###
# second empty list
mylist2 = []
# second count variable (already set as 55, so that's 1 less count)
count2 = 55
# same function as above, but only counts to 4 because count2 is already 55
for i in range(0,5):
    #append to list
    mylist2.append(count2)
    # not sure what "(output will be on separate lines)" means so i'm just going to print
    # the number here
    print(count2)
    # increase count by 1
    count2 += 1
# output list
print(mylist2)
###

print("-----------")

###
# third empty list
mylist3 = []
# third count variable
count3 = 4
# again, same function as above, counting to 4
for i in range(0,5):
    mylist3.append(count3)
    print(count3)
    # need to increase by 3 this time, not 1
    count3 += 3
print(mylist3)
###

print("-----------")

###
#forth count variable, this one is a little different because of the while loop
count4 = 90
# oh wow, a while loop this time
while count4 >= 76:
    print(count4)
    count4 -= 1
###

print("-----------")

###
#fifth count variable
count5 = 97
while count5 >= 87:
    # check for odd number
    if not count5 % 2 == 0:
        print(count5)
    count5 -= 1
###

print("-----------")

###
# new count variable
counter = 0
while True:
    print(counter)
    # ever increasing but breaks at specific value
    if counter == 9:
        break
    counter += 1
###

print("-----------")

###
# another new count variable
numcount = 0
while True:
    print(numcount)
    numcount += 1
    if numcount <= 10:
        continue
    else:
        break
###

print("-----------")

###
# here we go again
# that's 3 while loop variations that do the exact same thing
counter2 = 0
while True:
    if counter2 < 20:
        counter2 += 1
        continue
    else:
        print("Second counter hit 20, ending loop")
        break
###

print("-----------")

###
# final count variable
counter3 = 1
for num in range(0,20):
    counter += 1
    if counter == 10:
        print("This should be printed")
        break
else:
    print("This should not be printed")
###