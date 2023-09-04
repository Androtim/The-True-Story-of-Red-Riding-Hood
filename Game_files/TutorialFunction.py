from ClearScreenFunction import ClearScreen
from WrongChoiceFunction import WrongChoice

#Game tutorial
def Tutorial():
    print("""


        Feature under development...

        (To go back to the main menu, type [main])
    """)

    choice = input("").lower()

    if choice == "main":
        ClearScreen()
        START()

    else:
        ClearScreen()
        WrongChoice()
        Tutorial()


def START():
    from StartScreenFunction import StartScreen
    StartScreen()