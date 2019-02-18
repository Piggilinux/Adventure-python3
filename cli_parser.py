"""
Parse CLI options.

Using argparse to parse options.
"""

import argparse

VERSION = "Linus super awesome game 1.0"
#Skriver ut en beskrivning av programmet och vilka parameterar som fungerar.

INFO = """\n
    This is a game where enter 5 different rooms and you have to solve
    how to get to the next room by figuring out how to unlock the door or
    earn the game to unlock it by say winning a game in the game.\n
"""
ABOUT = """\n
    Linus Rosenholm is, the master of disaster, king of everything and also know
    as the symbol of hope for this world, that have created this game. He is 25
    years old and have come all the way from Stockholm to Karlskrona to study
    the art of computer science and perfection. in the future you will likely
    see him in magazine such as The New York Times and The Wall Street Journal.
    \n
"""
CHEAT = """\n
    ROOM 1:
    Open the box, pick up the key, use the key, move forward to the next from.
    ROOM 2:
    Open the candybag, pick up candy, use candy, pick up the key, use the key,
    move forward to the next room.
    ROOM 3:
    riddle 1 >> towel
    riddle 2 >> silence
    riddle 3 >> fire
    riddle 4 >> moon
    riddle 5 >> hole
    riddle 6 >> breath
    ROOM 4:
    Move Albert and accept his challange. There is no cheat for you to beat him
    in rock, paper, scissor. After you win move Albert again and move forward.
    ROOM 5:
    Open the computer and win the tic tac toe game. Tip is to star by chosing
    the middle (row 2, column 2).\n
"""

options = {}

def parse_options():
    """
    Parse all command line options and arguments and return them as a dictionary.
    """

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-s", "--silent", dest="silent", default="False",
                       help="decrease output verbosity", action="store_true")


    parser.add_argument("-V", "--version",
                        action="version",
                        version=VERSION,
                        help="Prints the version of the game.")

    parser.add_argument("-i", "--info",
                        action="version",
                        version=INFO,
                        help="Prints a description of the game and game idea.")

    parser.add_argument("-a", "--about",
                        action="version",
                        version=ABOUT,
                        help="Prints a short description of the creator of the game.")

    parser.add_argument("-c", "--cheat",
                        action="version",
                        version=CHEAT,
                        help="Prints the shortest possible way to complete the game.")

    #subparsers = parser.add_subparsers(
    #                title="commands (positional arguments)",
    #                help='Available commands',
    #                dest="command")

    #subparsers.add_parser("command1", help="information on command1")


    args, unknownargs = parser.parse_known_args()

    options["known_args"] = vars(args)
    options["unknown_args"] = unknownargs

    return options
