from ClearScreenFunction import ClearScreen
from WrongChoiceFunction import WrongChoice
import sys

#Funtion that exits the game
def ExitGame():
    print("""


        Do you want to exit the game? [y] or [n]
    """)

    choice = input("").lower()

    if choice == "y":
        ClearScreen()
        sys.exit()

    elif choice == "n":
        ClearScreen()
        print("""


        Do you want to go back to the main menu? [y] or [n]
        """)

        choice = input("").lower()

        if choice == "y":
            ClearScreen()
            START()

        elif choice == "n":
            ClearScreen()
            ExitGame()

        else:
            ClearScreen()
            WrongChoice()
            ExitGame()


    else:
        ClearScreen()
        WrongChoice()
        ExitGame()


def START():
    from StartScreenFunction import StartScreen
    StartScreen()