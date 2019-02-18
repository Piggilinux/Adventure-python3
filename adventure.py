    #!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
cheat and clue must be fixed in rom 2 and further.
"""
import sys
#import pprint
import cli_parser

import bag
import game
import helping

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""


def main():
    "This is the main game function"



    # Code is from Marvin 4 assignment.
    ###########################################################################
    inv = []
    num_lines = sum(1 for line in open("inv.data"))
    for i in range(num_lines):
        inv.append(bag.read_inventory(i))
        inv[i] = inv[i].split("\n")
        inv[i] = "".join(inv[i])
    ###########################################################################

    game.introduction()

    current_room = 1
    rooms = game.generate_room()
    game.current_status(rooms, current_room)

    helping.describe_room(current_room)
    game.look_around(rooms, current_room)


    enter_new_room = False

    while True:

        if enter_new_room is True:
            helping.describe_room(current_room)
            enter_new_room = False

        choice = input("> ")

        if choice == "q" or rooms[5]["items"]["monkey"] == "humble":
            print("Bye, bye - and welcome back anytime!")
            break
        elif choice == "cheat" or choice == "c":
            helping.cheats(rooms, current_room)
        elif choice == "h" or choice == "help":
            # same describes the room you are in.
            game.helping_commands()
        elif choice == "i" or choice == "info":
            helping.describe_room(current_room)
        elif choice == "see":
            # Describes the room and all objects that are currently shown.
            #helping.describe_room(current_room)
            game.look_around(rooms, current_room)
        elif choice == "fo" or choice == "forward":
            if rooms[current_room]["items"]["door"] == "open":
                # Moves you to the next room as long as you're not in the last room.
                if current_room < 5:
                    current_room += 1
                    enter_new_room = True
                    game.current_status(rooms, current_room)
                    game.look_around(rooms, current_room)
                else:
                    print("this is the last room...")
            else:
                print("The door is locked!")
        elif choice == "ba" or choice == "back":
            # Moves you to the previous room as long as you're not in the first room.
            if current_room > 1:
                current_room -= 1
                enter_new_room = True
                game.current_status(rooms, current_room)
                game.look_around(rooms, current_room)
            else:
                print("this is the first room.")
        elif choice == "obj" or choice == "object":
            # show all objects that are currently visable.
            game.look_around(rooms, current_room)
        elif "clue" in choice:
            #gives you a clue on what to do next.
            helping.clues(rooms, current_room, inv)
        elif choice == "-o" or choice == "--options":
            # Shows you both helping and interacting commands.
            game.helping_commands()
        ########################################################################
    #    elif "inv" in choice:
        elif "pick" in choice:
            # Picks up an object and adds it to your inventory
            bag.pick_item(rooms, current_room, choice, inv)
        elif "drop" in choice:
            # drops choosen or all items in inventory depending on your choice
            bag.drop_item(choice, inv)
        elif "use" in choice:
            splited = choice.split()
            item = splited[1]
            if bag.item_exists(item) is True:
                inv = bag.use_item(rooms, current_room, item, inv)
        elif choice == "inv":
            # Show content in inventory
            print(*inv, sep='\n')
        ########################################################################
        elif "l" in choice or "k" in choice or "o" in choice or "m" in choice:

            #if "open" in choice or "kick" in choice or "look" in choice\
                #or "move" in choice:
                # sends room dictionary, current room splited string into open function
            splited = choice.split()
            interaction = splited[0]
            item = splited[1]

            rooms = game.to_open(rooms, current_room, interaction, item)

        else:
            game.notValid()
        # Detta gick inte igenom valideringen....... :(
        # elif "open" in choice or "k" in choice or "kick" in choice\
        #     or "l" in choice or "look" in choice or "o" in choice\
        #     or "open" in choice or "m" in choice or "move" in choice:
        #     # sends room dictionary, current room splited string into open function
        #     splited = choice.split()
        #     interaction = splited[0]
        #     item = splited[1]
        #
        #     rooms = game.to_open(rooms, current_room, interaction, item)
        #
        # else:
        #     game.notValid()

    sys.exit()
#    input("\nPress enter to continue...")

if __name__ == "__main__":
    cli_parser.parse_options()
    #print(cli_parser.parse_options())
    #print(cli_parser.options["known_args"]["command"])

    main()
