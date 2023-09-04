import sys, subprocess
from sys import platform
from ClearScreenFunction import ClearScreen
from WrongChoiceFunction import WrongChoice
from StartScreenFunction import StartScreen

global choice, user_os

if platform == "linux" or platform == "linux2":
    user_os = "linux"

elif platform == "darwin":
    user_os = "mac"

elif platform == "win32":
    user_os = "Windows"

#hello

#The game starts
def StartGame():
    print("""

    
        You have now entered the wonderful world of Red Riding Hood...


        With which character do you wish to start your journey?


        Red Riding Hood [RRH]

        Wolf            [Wolf]

        Mother          [Mom]

        Grandmother     [Granny]


        (To go back to the main menu, type [main])
    """)

    choice = input("").lower()

    if choice == "main":
        ClearScreen()
        StartScreen()

    elif choice == "rrh":
        ClearScreen()
        RRH()

    elif choice == "wolf":
        ClearScreen()
        WOLF()

    elif choice == "mom":
        ClearScreen()
        MOM()

    elif choice == "granny":
        ClearScreen()
        GRANNY()


    else:
        ClearScreen()
        WrongChoice()
        StartGame()

#Game tutorial
def Tutorial():
    print("""


        Feature under development...

        (To go back to the main menu, type [main])
    """)

    choice = input("").lower()

    if choice == "main":
        ClearScreen()
        StartScreen()

    else:
        ClearScreen()
        WrongChoice()
        Tutorial()

#Game settings
def Settings():
    print("""


        Feature under development...

        (To go back to the main menu, type [main])
    """)

    choice = input("").lower()

    if choice == "main":
        ClearScreen()
        StartScreen()

    else:
        ClearScreen()
        WrongChoice()
        Settings()

#Game credits
def Credits():
    print("""
        Thank you for playing the game!


        Main dev      :  Timothée Béghin

        Story idea    :  My mom and dad

        Story writer  :  Timothée Béghin


        (To go back to the main menu, type [main])
    """)

    choice = input("").lower()

    if choice == "main":
        ClearScreen()
        StartScreen()

    else:
        ClearScreen()
        WrongChoice()
        Credits()

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
            StartScreen()

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Red Riding Hood story ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def RRH():
    from RRH_STORY import RrhStory
    RrhStory()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ WOLF STORY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def WOLF():
    from WOLF_STORY import WolfStory
    WolfStory()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MOM STORY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def MOM():
    from MOM_STORY import MomStory
    MomStory()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GRANNY STORY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def GRANNY():
    from GRANNY_STORY import GrannyStory
    GrannyStory

ClearScreen()
StartScreen()