"""
File inclueds a tic tac toe game and also the possebility to save and load
the game.
"""


#import datetime
import random
#from random import shuffle

def tic_tac_main(matrix):
    "here the game loops and call all its helpfiunctions"
    print("Enter your cordinates: ")

    whos_turn = 1
    victorious = False

    while True:
        if whos_turn % 2:
            move = "X"
        else:
            move = "O"
        whos_turn += 1

        #pick a chice and check to see that the range is right and also not taken
        while True:
            if move == "X":
                posY = input("Enter a row: ")
                posX = input("Enter a column (or q for quit): ")
            else:
                posY = random.randint(1, 3)
                posX = random.randint(1, 3)
            if posX != "l" and posX != "s" and posX != "q":
                if 1 <= int(posX) < 4 and 1 <= int(posY) < 4:
                    if matrix[int(posY) - 1][int(posX) - 1] == "_":
                        break
                    elif move == "X":
                        print("Already taken! Choose another one.")
                elif move == "X":
                    print("Out of range! Choose another one.")
            else:
                break


        if posY == "q" or posX == "q":
            print("Quiting game.")
            break
        elif posY == "s" or posX == "s":
            print("Saving game.")
            saveGame(matrix)
            continue
#        elif posY == "l" or posX == "l":
#            print("Loading game.")
#            loadMatrix(matrix)
#            continue

        matrix[int(posY) - 1][int(posX) - 1] = move
        printMatrix(matrix)

        winner = check_winner(matrix, "X", "O")
        if winner == "X":
            print("You won!")
            victorious = True
            return victorious
#            break
        elif winner == "O":
            print("Lol, you lost to  monkey ^^ ")
            victorious = False
            return victorious
#            break




def check_winner(mat, Xval, Oval):
    "Checks to see if there is 3 in a row and if so, return the winner variable"
    winner = "none"
    "Checks columns"
    for i in range(3):
        Xcounter = 0
        Ocounter = 0
        for k in range(3):
            for row in mat[i][k]:
                if row is Xval: # add count to either X or O value
                    Xcounter += 1
                elif row in Oval:
                    Ocounter += 1
                if Xcounter == 3: # confirmes a 3 in row
                    winner = "X"
                elif Ocounter == 3:
                    winner = "O"
#    print(to_check, "colums")
    "Checks rows"
    if Xcounter != 3 or Ocounter != 3:
        Xcounter = 0
        Ocounter = 0
        for i in range(3):
            Xcounter = 0
            Ocounter = 0
            for k in range(3):
                for row in mat[k][i]:
                    if row is Xval: # add count to either X or O value
                        Xcounter += 1
                    elif row in Oval:
                        Ocounter += 1
                    if Xcounter == 3: # confirmes a 3 in row
                        winner = "X"
                    elif Ocounter == 3:
                        winner = "O"
#    print(to_check, "rows")
    "diagonally left to right"
    Xcounter = 0
    Ocounter = 0
    for i in range(3):
        for row in mat[i][i]:
            if row is Xval: # add count to either X or O value
                Xcounter += 1
            elif row in Oval:
                Ocounter += 1
            if Xcounter == 3: # confirmes a 3 in row
                winner = "X"
            elif Ocounter == 3:
                winner = "O"
#    print(to_check, "left to right")
    "diagonally right to left"
    Xcounter = 0
    Ocounter = 0
    countdown = 3
    for i in range(3):
        countdown -= 1
        for row in mat[i][countdown]:
            if row is Xval: # add count to either X or O value
                Xcounter += 1
            elif row in Oval:
                Ocounter += 1
            if Xcounter == 3: # confirmes a 3 in row
                winner = "X"
            elif Ocounter == 3:
                winner = "O"
#    print(to_check, "right to left")

    return winner

def saveGame(matrix):
    "Saves the matrix in one row"

    with open("tictac.txt", 'w') as f:
        for row in matrix:
            f.write("".join(row) + '\n')


def loadGame(matrix):
    "Loads the file/game"
    with open("tictac.txt", 'r') as f:
        #save to one row in file
        content = f.read().splitlines()

        matrix_len = len(matrix)
        for i in range(matrix_len):
            matrix[i] = list(content[i])

    return matrix

def createMatrix(y, x, filler):
    "Create a two-dimensional array and returns it."
    return [[filler for _ in range(x)] for _ in range(y)]

def printMatrix(matrix):
    "Prints the game (matrix)"
    print("_____________")
    for row in matrix:
        print("|", " | ".join(row), "|")
