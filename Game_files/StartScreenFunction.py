from ClearScreenFunction import ClearScreen
from WrongChoiceFunction import WrongChoice

#The main start-screen
def StartScreen():

    TextOnScreen = """
    
        \033[1m
        WELCOME in The True Story of Red Riding Hood.
        \033[0m

    
        This is a choice based game where you will create your own story.

        To start the game, type [start].

        To learn how to play the game, type [tutorial].

        To open settings, type [settings].

        To view credits, type [credits].

        To exit, type [exit].
    
    """
    
    print(TextOnScreen)

    choice = input("").lower()

    if choice == "start":
        ClearScreen()
        START()

    elif choice == "tutorial":
        ClearScreen()
        TUTO()

    elif choice == "credits":
        ClearScreen()
        CREDS()

    elif choice == "settings":
        ClearScreen()
        SET()

    elif choice == "exit":
        ClearScreen()
        EXIT()

    else:
        ClearScreen()
        WrongChoice()
        StartScreen()


def START():
    from StartGameFunction import StartGame
    StartGame()

def TUTO():
    from TutorialFunction import Tutorial
    Tutorial()

def CREDS():
    from Game_files.SettingsFunction import Credits
    Credits()

def SET():
    from SettingsFunction import Settings
    Settings()

def EXIT():
    from ExitGameFunction import ExitGame
    ExitGame()