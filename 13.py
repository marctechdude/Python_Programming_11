import random

class rooms:
    name = ""
    directions = (0,0,0,0)
    msg = ""

def msg(room):
    if room.msg == '':
        return "You have entered the " + room.name + "."
    else:
        return room.msg

def get_choice(room,dir):
    if dir == 'N':
        choice = 0
    elif dir=='E':
        choice = 1
    elif dir == 'S':
        choice = 2
    elif dir == "W":
        choice = 3
    else:
        return -1

    if room.directions[choice] == 0:
        return 4
    else:
        return choice

def main():
    dirs = (0,0,0,0)

    entrance = rooms()
    livingroom = rooms()
    hallway = rooms()
    kitchen = rooms()
    diningroom = rooms()
    familyroom = rooms()
    garage = rooms()
    office = rooms()

    # define values for all of the rooms
    entrance.name = "Entrance"
    entrance.directions = (livingroom,diningroom,0,garage)

    diningroom.name = "Dining Room"
    diningroom.directions = (kitchen,0,0,entrance)

    # can only go to the entrance from the garage
    garage.name = "Garage"
    garage.directions = (0,entrance,0,0)

    livingroom.name = "Living Room"
    livingroom.directions = (0,kitchen,entrance,hallway)

    # can't go to the garage from the hallway
    hallway.name = "Hallway"
    hallway.directions = (office,livingroom,0,familyroom)

    kitchen.name = "Kitchen"
    kitchen.directions = (0,0,diningroom,livingroom)

    familyroom.name = "Family Room"
    familyroom.directions = (0,hallway,0,0)

    office.name = "Office"
    office.directions = (0,0,hallway,0)

    #get random rooms
    listrooms = [entrance,livingroom,hallway,kitchen,diningroom,familyroom,garage,office]
    item_room = random.choice(listrooms)
    john_room = random.choice(listrooms)
    found = False
    delivered = False
    room = entrance
    print("Find the item and deliver it to John.")

    while True:
        if found and delivered and room.name == "Entrance":
            print("You have delivered the item and returned to the entrance. Now get out.")
            break
        elif found and not delivered and room == john_room:
            print(msg(room))
            print("You've found John and have delivered the item to him.")
            room.msg = "You are back in the " + room.name + "! You have already delivered the item. Get out of here" \
                                                            "before John gets mad."
            delivered = True
        elif not found and not delivered and room == item_room:
            print(msg(room))
            print("You've found the item. Now go find John and deliver the item.")
            found = True
            room.msg = "You are back in the " + room.name + "! You have already found the item; go find John!"
        else:
            print(msg(room))
            room.msg = "You are back in the " + room.name + "."

        stuck = True
        while stuck:
            dir = input("Which direction would you like to go? N,E,S,W? ")
            choice = get_choice(room,dir)
            if choice == -1:
                print("Please enter N,E,S, or W. ")
                print("You are currently in the " + room.name + ".")
            elif choice == 4:
                print("You can't go there yet. Access to the door is a paid DLC.")
            else:
                room = room.directions[choice]
                stuck = False
main()