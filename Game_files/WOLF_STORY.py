from ClearScreenFunction import ClearScreen
from WrongChoiceFunction import WrongChoice

#Wolf's starting story
def WolfStory():
    TextOnScreen = """


        Feature under development...

        (To go back to the main menu, type [main])
	"""
	
	#print the text above
    print(TextOnScreen)

	#the player's input
    choice = input("").lower()

	#makes the player be able to go back to the main menu at any given moment
    if choice == "main":
        ClearScreen()
        START()

	#if the player's choice does not match any available choices
    else:
        ClearScreen()
        WrongChoice()
        WolfStory()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def START():
    from StartScreenFunction import StartScreen
    StartScreen()