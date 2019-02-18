"""
The deadly game of rock, paper scissor..
"""

from random import randint



def rps():
    "the game function roc, paper, scissor."
    #create a list of play options
    item = ["rock", "paper", "scissors", "q"]
    victorious = False
    rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
    paper = """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """
    scissor = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
    choice = [rock, paper, scissor]

    #assign a random play to the opponent
    opponent = item[randint(0, 2)]

    player_score = 0
    opponent_score = 0


    while player_score != 3 and opponent_score != 3:

        player = input("rock, paper, scissors -->")

        if player != "q":
            print("you played", choice[item.index(player)])
            print("opponent played", choice[item.index(opponent)])

        if player == "q":
            print("giving up are you...")
            break
        elif player == opponent:
            print("Tie!")
        elif player == "rock":
            if opponent == "paper":
                print("You lose!", opponent, "covers", player)
                opponent_score += 1
            else:
                print("You win!", player, "smashes", opponent)
                player_score += 1
        elif player == "paper":
            if opponent == "scissors":
                print("You lose!", opponent, "cut", player)
                player_score += 1
            else:
                print("You win!", player, "covers", opponent)
                player_score += 1
        elif player == "scissors":
            if opponent == "rock":
                print("You lose...", opponent, "smashes", player)
                opponent_score += 1
            else:
                print("You win!", player, "cut", opponent)
                player_score += 1
        else:
            print("That's not a valid play...")

        opponent = item[randint(0, 2)]

    print("final score are User:", player_score, " and Opponent:", opponent_score)

    if player_score == 3:
    #    rooms[current_room]["items"]["door"] = "open"
        victorious = True
    else:
        print("You better try again if you wanna get through that door.")

    return victorious
