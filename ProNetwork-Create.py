# Create a directory of ProNetwork where:
#   Main.py - Main project
#   Tut - Tut File
#   Intro - Intro File
# These files should be in the same directory as this file.
from os import makedirs
from shutil import move

makedirs(".\\ProNetwork") # The Folder
makedirs(".\\ProNetwork\\Main") # The Main Directory
move("Main.py", ".\\ProNetwork\\")
move("Tut", ".\\ProNetwork\\Main\\")
move("Intro", ".\\ProNetwork\\Main\\")
