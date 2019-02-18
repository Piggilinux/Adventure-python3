"""
Here all items functions are. all functions contains the different
choices like kick, open and so on.
"""

#import bag
import rock_paper_scissor
import tic_tac

def box(rooms, current_room, interaction, new_item):
    "function checks for choosen interaction acts on it."
    if interaction == "open" or interaction == "o":
        if interaction == "open" or interaction == "o":
            print("Seems like a", new_item, "appeard")
            rooms[current_room]["items"][new_item] = "unlocks"
            #rooms[current_room]["items"].append({new_item : "unlocks"})
    elif interaction == "k" or interaction == "kick":
            # extra commments just for fun.. möjligen gör till function????
        if "key" in rooms[current_room]["items"]:
            print("Well now you're just wasting your own time...")
        else:
            print("Sounds like there is someting inside the box.")
    elif interaction == "l" or interaction == "look":
        print("The box on the floor looks very old..")
    elif interaction == "m" or interaction == "move":
        print("how neat, you moved the box. Very usefull move.....")

def door(rooms, current_room, interaction):
    "# function checks for choosen interaction and makes it on door."

    if interaction == "open" or interaction == "o":
        # if you have key it will unlock
        #if "key" in rooms[current_room]["items"]:
        #if bag.item_exists("key") is True:
        if rooms[current_room]["items"]["door"] == "open":
            #changes status on door from locked to unlocked
            #rooms[current_room]["items"]["door"] = "unlocked"
            print("Door is ", rooms[current_room]["items"]["door"], "and you can enter the next room.")
        # if no key door will be locked
        else:
            print("The door is", rooms[current_room]["items"]["door"])
    elif interaction == "k" or interaction == "kick":
        print("That door is rock solid and now you foot hurts...")
    elif interaction == "l" or interaction == "look":
        print("The door looks solid as hell.")
    elif interaction == "m" or interaction == "move":
        print("Dude you can't move a door...")

def candybag(rooms, current_room, interaction, new_item):
    "function checks for choosen interaction acts on it."
    if interaction == "open" or interaction == "o":
        if interaction == "open" or interaction == "o":
            print("Seems like there's a lot of ", new_item, "in the bag.")
            rooms[current_room]["items"][new_item] = "unlocks"
    elif interaction == "k" or interaction == "kick":
            # extra commments just for fun.. möjligen gör till function????
        print("Stop kicking the candymans bag! Now he looks even more sad..")
    elif interaction == "l" or interaction == "look":
        print("It looks like a candybag with lots of candy in it!")
    elif interaction == "m" or interaction == "move":
        print("You moved the bag.. Stop moving stuff for no reason!")

def computer(rooms, current_room, interaction, new_item):
    "interactions with the computer"
    correct_answer = 0
    if interaction == "open" or interaction == "o":
        print(
            "text on the computerscreen apears:\n\n To be able to "
            "continue to the next room you must answer at least two of the"
            " six riddles!")
        print(
            "If you dont know the answer just type 'x' as an answer.\n"
            "tip! The answer is in one word ;-)"
        )

        #print(rooms[current_room]["items"]["computer"]["riddles"])
        for i in range(1, 7):
            print(new_item["riddles"][i]["question"])
            answer = input(": ")
            if answer in new_item["riddles"][i]["answer"]:
                correct_answer += 1
        if correct_answer >= 2:
            print("You got", correct_answer, "out of 6. The door is now open!")
            rooms[current_room]["items"]["door"] = "open"
        else:
            print(
                "Not enough correct answers, better try again! maby try "
                "use google.")

    elif interaction == "k" or interaction == "kick":
        print(
            "Carefull! That is a fragile computer which must be"
            "handled with care.")
    elif interaction == "l" or interaction == "look":
        print(
            "You look at the closed computer and see a note"
            "that says open me!")
    elif interaction == "m" or interaction == "move":
        print("Please don't move the computer!")

def albert(rooms, current_room, interaction):
    "This functions starts a rock, paper, scissors game"

    if interaction == "open" or interaction == "o":
        print(
            "albert doesn't wanna open up to you, he only does that with "
            "his therapist")
    elif interaction == "m" or interaction == "move":
        if rooms[current_room]["items"]["albert"] == "stable":
            accept = input(
                "The man seems too stable to move and now he looks "
                "concerned.. He now challange you to a game of rock, paper, "
                "scissor! do you accept his challange? y/n: "
            )
            if accept == "y":
                print("Alright lets begin!\n\n")
                if rock_paper_scissor.rps() is True:
                    rooms[current_room]["items"]["albert"] = "unstable"
                    print("albert looks a little unstable after the heavy loss...")
            else:
                print("okay suit your self...")
        else:
            print("You move albert out of the way and the door is unlocked.")
            rooms[current_room]["items"]["door"] = "open"
    elif interaction == "k" or interaction == "kick":
        print(
            "at first you were gonna kick albert but then you"
            " realise that he looks to old to be kicked at.."
        )
    elif interaction == "l" or interaction == "look":
        print("You look at albert and albert looks back at you.")
        r = r"""\n\n
                         -''--.
                         _`>   `.-'<
                      _.'     _     '._
                    .'   _.='   '=._   '.
                    >_   / /_| /_| |   _<
                      / (  \o/| o/  )
                      >._| .-,_)-. /_.<
                          /__/ |__
                            '---'
            """
        print(r, "\n\n\n")

def lastplay(rooms, current_room, interaction):
    "the last play that is a tic tac toe game. it is in the tic_tac.py file"
    if interaction == "m" or interaction == "move":
        print("Lets not move the game lets just play the game!")
    elif interaction == "open" or interaction == "o":
        if rooms[current_room]["items"]["monkey"] == "cocky":
            print(
                "The game you opened is Tic Tac Toe! it shouln't be to  "
                "difficult to beat a monkey right? ")
            print("Alright lets begin!\n\n")

            matrix = tic_tac.createMatrix(3, 3, "_")
            game = input(
                "If you have an old game press l to load game "
                " else just press anykey: ")
            if game == "l":
                print("Loading game...")
                matrix = tic_tac.loadGame(matrix)
                tic_tac.printMatrix(matrix)
            else:
                print("Starting a new game.")
                if tic_tac.tic_tac_main(matrix) is True:
                    rooms[current_room]["items"]["monkey"] = "humble"
                    end_of_game()


    elif interaction == "k" or interaction == "kick":
        print("What good does that do?")
    elif interaction == "l" or interaction == "look":
        print("You look at the game and you see that it is a tic tac toe game!")

def end_of_game():
    "Here ending text is made (with a big ending 8-) )"
    print("\n\n\n\n\n")
    t = r"""
   _____                                  _           _         _    _                      _
  / ____|                                | |         | |       | |  (_)                    | |
 | |      ___   _ __    __ _  _ __  __ _ | |_  _   _ | |  __ _ | |_  _   ___   _ __   ___  | |
 | |     / _ \ | '_ \  / _` || '__|/ _` || __|| | | || | / _` || __|| | / _ \ | '_ \ / __| | |
 | |____| (_) || | | || (_| || |  | (_| || |_ | |_| || || (_| || |_ | || (_) || | | |\__ \ |_|
  \_____|\___/ |_| |_| \__, ||_|   \__,_| \__| \__,_||_| \__,_| \__||_| \___/ |_| |_||___/ (_)
                        __/ |
                       |___/
                       """
    print(t,
          "\n\n\n",
          "You have finished all rooms and you can now roam the "
          "world as u see fit! ")
    m = r"""

               ,;;;;;;;;;,
              /////////\\\\        _______________________________
             |// __   __ \\|     /                                |
             \/=(_o)^(o_)=\/    / Thank you playing my epic game! |
            (_    (___)    _)  /__________________________________|
              \  \_____/  /
               `-._   _.-'
               __.-)_(-,__
            ./'  \_\_/_/  `\.
           / >   | //\ |   < |
          /  \   | |/| |   /  |
         /   |\  | |/| |  /|   |
        /   /| \ | |/| | / |\   |
       (   ( |  \| |/| |/  | )   )
        \   \|   Y |/| Y   |/   /
         \   |  o| |/| |-  |   /
          `\ |   | `^` |   | /'
            `|  o|=[Ll=|-  |'
             |   /     \   |
             ~~|`  \    `|~~
               |    |    |
               |    |    |
               |    |    |
               |    |    |
               |    |    |
               |    |    |
               |    |    |
               |    |    |
               |____|____|
               /   / \   |
          jgs /   /   \   |
             `---'     `---`
             """
    print(m)

def monkey(interaction):
    "here interactions with monkey is made"

    m = r"""
                  .-''''-.
                 _/-=-.   |
                (_|a a/   |_
                 / "  \   ,_)
            _    \`=' /__/
           / \_  .;--'  `-.
           \___)//      ,  |
            \ \/;        \  |
             \_.|         | |
              .-\ '     _/_/
            .'  _;.    (_  |
           /  .'   `\   \\_/
          |_ /       |  |\\
         /  _)       /  / ||
        /  /       _/  /  //
        \_/       ( `-/  ||
                  /  /   \\ .-.
                  \_/     |'-'/
                           `"`
    """

    if interaction == "m" or interaction == "move":
        print(
            "The monkey moves up and down and all around"
            "so i think he moves enough")
    elif interaction == "open":
        print("You can't open a monkey.....")
    elif interaction == "k" or interaction == "kick":
        print("Lol, like you would ever be able to kick that monkey!")
    elif interaction == "l" or interaction == "look":
        print("You look at the monkey and he looks so cute :D")
        print(m)
