"""
Here all 'helping commands' function are stored. all except
forward and back, they are made in the adventure file.
"""
import sys
import interactions

def describe_room(current_room):
    "describes the current room you are in."

    if current_room == 1:
        print("The room you are in apears to be empty except for a small box "
              "on the floor. ")
    elif current_room == 2:
        print("You have entered the second room and it looks like it is the"
              " Candymans office. He is just standing there with a key in his"
              " hand.. But why does he look so sad?")
    elif current_room == 3:
        print(
            "You have entered the third room, the room of riddles. in front"
            " of you there is an computer.")
    elif current_room == 4:
        print(
            "When you enter the forth room you see a weird looking fella "
            "standing in front of the door..."
        )


def clues(rooms, current_room, inv):
    "Helps the player with clues in the current room"

    if current_room == 1:
        if rooms[current_room]["items"]["door"] == "locked":
            print("Maby there's something in the box?")
        else:
            print("Pick up key and use it?")
    elif current_room == 2:
        if "candy" not in rooms[current_room]["items"] and "candy" not in inv:
            print("Have you looked in the bag?")
        elif "candy" in rooms[current_room]["items"]:
            print("Candy always sets people in a good mood.")
        elif rooms[current_room]["items"]["candyman"] == "sad":
            print("Maby the candyman likes candy?")
    elif current_room == 3:
        print("Maby Google can be to some help?")
    elif current_room == 4:
        "Albert stands in the way of the door..."
    elif current_room == 5:
        print("Looks like the monkey want you to open the game.")



        #    print(rooms[current_room]["items"]["door"])

def cheats(rooms, current_room):
    "Unlocks the door in current room."
    rooms[current_room]["items"]["door"] = "open"
    if current_room != 5:
        print("The door is now unlocked you little cheater :-)")
    else:
        interactions.end_of_game()
        sys.exit()
