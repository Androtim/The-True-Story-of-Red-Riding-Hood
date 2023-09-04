#This funtion displays a line of text when the player inputs an invalid choice
def WrongChoice():
    print("""
        \033[1;31m
        Please enter one of the choices available, not anything else :)
        \033[0m""")

    return