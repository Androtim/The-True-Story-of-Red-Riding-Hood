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
        StartGame()

    elif choice == "tutorial":
        ClearScreen()
        Tutorial()

    elif choice == "credits":
        ClearScreen()
        Credits()

    elif choice == "settings":
        ClearScreen()
        Settings()

    elif choice == "exit":
        ClearScreen()
        ExitGame()

    else:
        ClearScreen()
        WrongChoice()
        StartScreen()