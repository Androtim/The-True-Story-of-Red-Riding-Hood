from ClearScreenFunction import ClearScreen
from WrongChoiceFunction import WrongChoice
import os

#Game settings
def Settings():
    print("""


        Type [save]

        (To go back to the main menu, type [main])
    """)

    choice = input("> ").lower()

    if choice == "save":
        ClearScreen()

        with open('Game_files/Params/Settings.txt', 'r') as f:
            autosave_status = f.readline(16)

        print(autosave_status)

        if autosave_status == 'autosave = False':
            ClearScreen()
            print("""
              Do you want to turn autosaves on? [y][n]
              """)
            choice = input("> ").lower()

            if choice == "y":
                ClearScreen()
                autosave_status = autosave_status.replace('autosave = False', 'autosave = True')
                with open('Game_files/Params/Settings.txt', 'w') as f:
                    f.write(autosave_status)
                print("""
                      Autosave is now turned on!
                      """)

            elif choice == "n":
                ClearScreen()
                Settings()

            else:
                ClearScreen()
                WrongChoice()
                Settings()

        elif autosave_status == 'autosave = True':
            print("""
              Do you want to turn autosaves off? [y][n]
              """)
            choice = input("> ").lower()
            
            if choice == "y":
                ClearScreen()
                autosave_status = autosave_status.replace('autosave = True', 'autosave = False')
                with open('Game_files/Params/Settings.txt', 'w') as f:
                    f.write(autosave_status)
                print("""
                      Autosave is now turned off!
                      """)

            elif choice == "n":
                ClearScreen()
                Settings()
            
        else:
            print("""
                \033[1;31m
                There seems to be a problem with the save file, please check if autosave is set to either 'True' or 'False'.
                \033[0m""")

    elif choice == "main":
        ClearScreen()
        START()

    elif choice == "exit":
        ClearScreen()
        EXIT()

    else:
        ClearScreen()
        WrongChoice()
        Settings()


def START():
    from StartScreenFunction import StartScreen
    StartScreen()

def EXIT():
    from ExitGameFunction import ExitGame
    ExitGame()