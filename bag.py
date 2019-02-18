"""
The bag file where all funcitons such as add, remove show and also save exists.
"""

def read_inventory(line):
    "is for reading the inv.data file in the start of the script"
    #    path = "/mnt/c/dbwebb-kurser/python/me/kmom04/marvin3/inv.data"
    f = open("inv.data", "r")
    that_is_read = f.readlines()
    return that_is_read[line]

def show_inventory(array):
    "just prints the item"
    print(array)

def add_to_inventory(item):
    "adds item to the data file and then returns the added item"
    #    path = "/mnt/c/dbwebb-kurser/python/me/kmom04/marvin3/inv.data"
    f = open("inv.data", "a")
    f.write(item)
    f.close()
    return item


def  drop_from_inventory(item):
    """
    removes string from data-file
    """

    #    path = "/mnt/c/dbwebb-kurser/python/me/kmom04/marvin3/inv.data"
    with open("inv.data", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if item not in line:
                f.write(line)
        f.truncate()


def clear_bag():
    "Clears all items in bag"
    #    path = "/mnt/c/dbwebb-kurser/python/me/kmom04/marvin3/inv.data"
    open("inv.data", 'w').close()

def pick_item(rooms, current_room, choice, inv):
    "PIMPA DENNA FUNKTION SENARE!!!!"
    if len(inv) < 4:
        choice = choice.split("inv")
        choice = "".join(choice)
        choice = choice.split("pick")
        choice = "".join(choice)
        choice = choice.split(" ")
        choice = "".join(choice)


        if choice in rooms[current_room]["receivable"]:
            #if object is receivable it is added to bag.
            inv.append(choice)
            # Removes picked upp item from room and puts it in bag.
            del rooms[current_room]["items"][choice]
            add_to_inventory(choice+"\n")
            print("You picked up {0}" .format(choice))
        else:
            print("Item is not receivable.")

    else:
        print("Inventory is full..")

def item_exists(item):
    "uses item that are in bag to its purpose"
    usage = False
    with open("inv.data", "r") as f:
        for line in f:
            if item in line:
                usage = True

    return usage



def drop_item(choice, inv):
    "PIMPA DENNA FUNKTION SENARE!!!!"
    choice = choice.split("inv")
    choice = "".join(choice)
    choice = choice.split("drop")
    choice = "".join(choice)
    choice = choice.split(" ")
    choice = "".join(choice)
    #            choice = re.split("inv|drop| | ", choice)
    if not choice:
        inv.clear()
        clear_bag()
        print("Inventory has been cleared.")
    elif choice in inv:
        drop_from_inventory(choice)
        inv.remove(choice)
        print("You droped {0}" .format(choice))
    else:
        print("Could not find item..")

def use_item(rooms, current_room, item, inv):
    "Uses an item that has been picked up"
    if item == "key":
        #changes door to open
        rooms[current_room]["items"]["door"] = "open"
        print("You use the key to unlock the door.")
        drop_from_inventory(item)
        inv.remove(item)
    elif item == "candy":
        #makes candyman happy and key appears.
        rooms[current_room]["items"]["candyman"] = "happy"
        rooms[current_room]["items"]["key"] = "unlocks"
        print("You gave", item, "to the candyman and now"
              " he's happy! He puts away the key and starts"
              " eating more candy.")
        drop_from_inventory(item)
        inv.remove(item)
    return inv
