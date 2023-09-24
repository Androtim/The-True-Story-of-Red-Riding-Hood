from ClearScreenFunction import ClearScreen
from WrongChoiceFunction import WrongChoice

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

    choice = input("> ").lower()

    if choice == "main":
        ClearScreen()
        START()

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ START GAME ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def START():
    from StartScreenFunction import StartScreen
    StartScreen()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Red Riding Hood story ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def RRH():
    from RRH_STORY import RrhStory
    RrhStory()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ WOLF STORY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def WOLF():
    from WOLF_STORY import WolfStory
    WolfStory()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MOM STORY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def MOM():
    from MOM_STORY import MomStory
    MomStory()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GRANNY STORY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def GRANNY():
    from GRANNY_STORY import GrannyStory
    GrannyStory