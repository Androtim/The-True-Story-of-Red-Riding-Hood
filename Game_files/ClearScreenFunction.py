import subprocess
from sys import platform

global user_os
if platform == "linux" or platform == "linux2":
    user_os = "linux"

elif platform == "darwin":
    user_os = "mac"

elif platform == "win32":
    user_os = "Windows"

#This funtion clears the player's screen
def ClearScreen():

    if platform == "linux" or platform == "linux2" or platform == "darwin":
        subprocess.run('clear')

    elif platform == "win32":
        subprocess.call('cls', shell=True)

    else:
        print("""
        \033[1;31m
        An error occured while trying to clear the screen. 
        Please restart the program
        \033[0m""")

    return

def blank_line(n=1):
    for i in range(n):
        print()