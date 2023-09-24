from ClearScreenFunction import ClearScreen
from WrongChoiceFunction import WrongChoice

#Game credits
def Credits():
    print("""
        Thank you for playing the game!


        Main dev      :  Timothée Béghin

        Story idea    :  My mom and dad

        Story writer  :  Timothée Béghin


        (To go back to the main menu, type [main])
    """)

    choice = input("> ").lower()

    if choice == "main":
        ClearScreen()
        START()

    else:
        ClearScreen()
        WrongChoice()
        Credits()


def START():
    from StartScreenFunction import StartScreen
    StartScreen()