"""
lots of Middle state function to make the code more clear. it helps make
the conditon more clear by sluicing them. Also the intro function and
helping commans is here.
"""

import pprint
import interactions


def generate_room():
    """
    Here all rooms are created. they contain a room name and items with
    different qualitys. each room will be placed in 'rooms' so they get a room
    number.
    """
    riddles = {
        1 : {
            "question" : "1: What gets wet while drying?",
            "answer" : "towel"
        },
        2 : {
            "question" : "2: What is it that you will break even when you name it?",
            "answer" : "silence"
        },
        3 : {
            "question" : "3: Feed me and I live, give me something to "
                         "drink and I'll die. What am I?",
            "answer" : "fire"
        },
        4 : {
            "question" : "4: It's been around for millions of years, but "
                         "it's no more than a month old. What is it?",
            "answer" : "moon"
        },
        5 : {
            "question" : "5: The more you take away the larger it becomes?",
            "answer" : "hole"
        },
        6 : {
            "question" : "6: I am lighter than a feather, yet no man can "
                         "hold me for very long. What am I?",
            "answer" : "breath"
        }
    }
    room1 = {
        "name" : "room_of_mysteries",
        "items" : {
            "box" : "key",
            "door" : "locked"
            },
        "receivable" : ["key"]
    }
    room2 = {
        "name" : "candyroom",
        "items" : {
            "door" : "locked",
            "candyman" : "sad",
            "bag" : "candy"
            },
        "receivable" : ["key", "candy"]
    }
    room3 = {
        "name" : "riddle room",
        "items" : {
            "computer" : {"riddles" : riddles},
            "door" : "locked"
            },
        "receivable" : ["key"]
    }
    room4 = {
        "name" : "the room of mental skills room",
        "items" : {
            "door" : "locked",
            "albert" : "stable"
            }
    }
    #        "receivable" : ["football"]
    room5 = {
        "name" : "Gameroom",
        "items" : {
            "game" : "closed",
            "monkey" : "cocky"
        }
    }

    rooms = {
        1 : room1,
        2 : room2,
        3 : room3,
        4 : room4,
        5 : room5
    }
    #    pprint.pprint(rooms, width=2)
    return rooms

def current_status(rooms, current_room):
    "Shows which room you are in and what the room name is."
    print("You are currently in room:", current_room, "\n")
    pprint.pprint(rooms[current_room]["name"])

def look_around(rooms, current_room):
    "prints all object in the room."
    print("You look around and find some things:")
    # goes through all items in rooms at current position.
    for key in rooms[current_room]["items"]:
        print(key)

def to_open(rooms, current_room, interaction, item):
    """
    Here elif will be used for interaction with different objects
    and show status or changes that have been made while doing so.
    """
    item_exists = does_item_exist(rooms, current_room, item)

    #item exists an atemt of opening it will be done.
    if item_exists is True:
        # for open box to get key
        new_item = rooms[current_room]["items"][item]
        # adds a key to dictionary with value unlock (value is of no interrest in this case...)
        if item == "box":
            # function checks for choosen interaction and makes it on box.
            interactions.box(rooms, current_room, interaction, new_item)
        # for opening door
        elif item == "door":
            # function checks for choosen interaction and makes it on door.
            interactions.door(rooms, current_room, interaction)
        elif item == "bag":
            # function checks for choosen interaction and makes it on door.
            interactions.candybag(rooms, current_room, interaction, new_item)
        elif item == "computer":
            interactions.computer(rooms, current_room, interaction, new_item)
        elif item == "albert":
            interactions.albert(rooms, current_room, interaction)
        elif item == "game":
            interactions.lastplay(rooms, current_room, interaction)
        elif item == "monkey":
            interactions.monkey(interaction)


    else:
        print("There is no such item in this room..")

    return rooms

#def kick():
#    item_exists = item_exists

    # ROOM 1 == if item exists item will be kicked
    #    if item_exists == True and current_room == 1:


def does_item_exist(rooms, current_room, item):
    "checks if the typed item exists"
    item_exists = False
    for key in rooms[current_room]["items"]:
        if key == item:
            item_exists = True
            break
    return item_exists

def introduction():
    "Startup text with introduction and helping commands."

    print("\n\n                       WELCOME TO ")
    text = """
         /|      | |               | |
        /  |   __| |_   _____ _ __ | |_ _   _ _ __ ___
       / /| | / _` | | / / _ | '_  | __| | | | '__/ _ |
      / ____ | (_| || V /  __/ | | | |_| |_| | | |  __/
     /_/    |_|__,_| |_/ |___|_| |_|___|___,_|_|  |___|

    """


    print("\n", text)
    print("================================================================")
    print("\nHere you will ventrure into different rooms which\n"
          "will contain different items that you can use or interact\n"
          "with. The purpose is to get through all 5 rooms.\n"
          "\n\n")
    helping_commands()

def helping_commands():
    """
    Prints all helping command. will be show at the start of the game or
    when player press -o / --options
    """
    print("Helping commands:\n")
    print("h or help               Describes the room you are in.")
    print("fo or forward           Moves to next room.")           # is made in adventure
    print("ba or back              Moves to the previous room.")   # is made in adventure
    print("see                     You look around the room.")     # samma som object???
    print("c or clue               Will give you a clues.")
    print("cheat                   Will give you cheats to finish quickly.\n\n")
    print("interacting commands:\n")
    print("obj or object          Shows all objects that are in the room.")
    print("l or look [object]     Describes an object.")
    print("o or open [object]     If posible, opens chosen object.")
    print("k or kick [object]     Kicks the object to see if it can be broken.")
    print("m or move [object]     Moves the object if posible.")
    print("pick      [object]     Picks up an receivable object")
    print("use       [object]     Use an object from you bag")
    print("inv                    Shows items in inventory\n\n")



def notValid():
    "A non valid choise."
    print("That is not a valid choice. press -o or --options for help.")
