import os
from position import Position

actualPosition = Position()


def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def displayScreen(message):
    clear_terminal()
    actualPosition.performRequest(message)