from ClearScreenFunction import ClearScreen
from WrongChoiceFunction import WrongChoice

#RRH's starting story
def RrhStory():
    TextOnScreen = """

        \033[1m
	    Once upon a time there was a dear little girl who was loved by every one who looked at her, but
        most of all by her grandmother, and there was nothing that she would not have given to the child.
        Once she gave her a little cap of red velvet, which suited her so well that she would never wear
        anything else. So she was always called Little Red Riding Hood.
        \033[0m

        You are in your room, laying on your bed reading your book. From downstairs, you hear your mom
        call for you : "Red Riding Hood! Please come down! I need to you to bring something to Granny.
        She is ill and very tired and is unnable to get out of bed!

        After hearing this, Red Riding Hood really wants to help her mom and grandma by 
        going [downstairs] but she'd prefer to play with her friends to have a good time [outside]
        before the end of the day.
    
	    """
	
	#print the text above
    print(TextOnScreen)

	#the player's input
    choice = input("").lower()

	#makes the player be able to go back to the main menu at any given moment
    if choice == "main":
        ClearScreen()
        START()

    elif choice == "downstairs":
        ClearScreen()
        RrhDowstairsMom()

    elif choice == "outside":
        ClearScreen()
        RrhOutsideFirstTime()

	#if the player's choice does not match any available choices
    else:
        ClearScreen()
        WrongChoice()
        RrhStory()

#This function is used if RRH goes downstairs in her home
def RrhDowstairsMom():
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
        RrhDowstairsMom()

#This function is displayed if RRH goes outside at the start
def RrhOutsideFirstTime():
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
        RrhOutsideFirstTime()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def START():
    from StartScreenFunction import StartScreen
    StartScreen()