"""Download Libraries used by pyEasy."""
from subprocess import run

run("pip install pyautogui", shell=True, capture_output=True, text=True)
run("pip install opencv-python", shell=True, capture_output=True, text=True)
run("pip install requests", shell=True, capture_output=True, text=True)
run("pip install flask  ", shell=True, capture_output=True, text=True)