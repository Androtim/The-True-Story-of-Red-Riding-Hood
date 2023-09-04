#default funtions for RRH game

"""
def FUNCTION_NAME():
	TextOnScreen = """

	#TEXT TO PRINT HERE
    
	"""
	
	#print the text above
	print(TextOnScreen)

	#the player's input
	choice = input("").lower()

	#makes the player be able to go back to the main menu at any given moment
	if choice == "main menu":
        ClearScreen()
        StartScreen()

	#if the player's choice does not match any available choices
	else:
        ClearScreen()
        WrongChoice()
        StartScreen()


