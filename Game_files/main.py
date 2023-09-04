import sys, subprocess
from sys import platform
from ClearScreenFunction import ClearScreen
from WrongChoiceFunction import WrongChoice
from StartScreenFunction import StartScreen

global choice, user_os

if platform == "linux" or platform == "linux2":
    user_os = "linux"

elif platform == "darwin":
    user_os = "mac"

elif platform == "win32":
    user_os = "Windows"

ClearScreen()
StartScreen()