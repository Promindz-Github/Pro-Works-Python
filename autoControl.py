"""Helps to control the window only by python."""
import pyautogui as PAG;from tkinter import Tk as KAILKIJHEGEF_UWGSH
from time import sleep
Root = KAILKIJHEGEF_UWGSH() # An unique name that no one will use ever to hide the window class.
PAG.FAILSAFE = False
del KAILKIJHEGEF_UWGSH
A="a";B="b";C="c";D="d";E="e";F="f";G="g";H="h";I="i";J="j";K="k";L="l";M="m";N="n";O="o";P="p";Q="q";R="r";S="s";T="t";U="u";V="v";W="w";X="x";Y="y";Z="z"
WINDOWS = "win"
"""Windows Key"""
NUM1="1";NUM2="2";NUM3="3";NUM4="4";NUM5="5";NUM6="6";NUM7="7";NUM8="8";NUM9="9";NUM0="0"
PNG="png";JPG="jpg"
ENTER="\n"
# TAB="tab"
DOT = "."
TAB="\t"
SPACE=" "
BROWSERBACK="browserback"
"""Only for windows."""
BROWSERFORWARD="browserforward"
"""Only for windows."""
CAPSLOCK = "capslock"
DECIMAL = "decimal"
CTRL = "ctrl"
ALT = "alt"
SHIFT = "shift"
ESCAPE = "esc"
END = "end"
HOME = "home"
INSERT = "insert"
ASTERIK = "asterik"
PLUS = ADD = "add"
MINUS = HYPHEN = SUBTRACT = "subtract"
MULTIPLY = "multiply"; DIVIDE = "divide"
PRINTSCREEN = "printscreen"
LOWER = ["Caps", -1]
"""Use in the function type()."""
CAPS = ["Caps", 0]
"""Use in the function type()."""
UPPER = ["Caps", +1]
"""Use in the function type()."""
def functionKey(Number:int=1): return f"f{Number}"
ThisFolder=".";Parent="..";GrandParent="..\\..";GrandGrandParent="..\\..\\.."
MIDDLE = (Root.winfo_screenwidth()/2, Root.winfo_screenheight()/2);"""Middle Coordinates."""
TOPRIGHT = (Root.winfo_screenwidth(), 0);"""Top right Coordinates."""
TOPLEFT = (0, 0);"""Top left Coordinates."""
BOTTOMRIGHT = (Root.winfo_screenwidth(), Root.winfo_screenheight());"""Bottom right Coordinates."""
BOTTOMLEFT = (0, Root.winfo_screenheight());"""Bottom left Coordinates."""
MIDDLETOP = (Root.winfo_screenwidth()/2, 0);"""Coordinates at the top in the middle of the screen."""
MIDDLEBOTTOM = (Root.winfo_screenwidth()/2, Root.winfo_screenheight());"""Coordinates at the bottom in the middle of the screen."""
MIDDLERIGHT = (Root.winfo_screenwidth(), Root.winfo_screenheight());"""Coordinates at the bottom in the middle of the screen."""
MIDDLELEFT = (0, Root.winfo_screenheight());"""Coordinates at the left in the middle of the screen."""
Root.destroy()
del Root
# def finishCode(): """Used to not Interrupt the program of GUI. Put it before .finishCode() of the Window()."""; Root.destroy()
def showDesktop(FullScreen:bool=False, AfterCoordinates:tuple[int] | list[int] | dict[int] | dict[float] | list[float] | tuple[float]=MIDDLE):
    if FullScreen:PAG.keyDown("win");PAG.keyUp("win");PAG.moveTo(BOTTOMRIGHT);PAG.leftClick();PAG.moveTo(AfterCoordinates);"""Show the desktop window."""
def moveMouse(*ListOfCoordinates):
    for Coordinates in ListOfCoordinates: PAG.moveTo(Coordinates)
         
def ClickOn(*Coordinates): 
    if len(Coordinates) == 1:
        moveMouse(Coordinates[0]); PAG.leftClick()
    else:
        moveMouse(Coordinates); PAG.leftClick()
def presskey(*Keys):
    """# Single or Group.\n* SINGLE: Give the names of keys stored in vars like A contains "a". Without keeping them in brackets or prenthesis we say. They will be pressed individually.\n\n* GROUP: Give the names of keys stored in vars like A contains "a". With keeping them in brackets or prenthesis we say. They will be pressed and holded till the last key of the gorup is not pressed."""
    try:
        for key in Keys:PAG.keyDown(key);PAG.keyUp(key)
    except:
        for Group in Keys:
            for key in Group:PAG.keyDown(key)
            for key in Group:PAG.keyUp(key)
def type(String:str, *Letters):
    """Type a string. Giving a var CAPS before typing a letter will add a capslock on till the CAPSLOCK is not given again. Using keyword UPPER or LOWER will make the next argument uppcase or lowercase repectively."""
    LOWERE = [False]
    UPPERE = [False]
    for Num in Letters: LOWERE.append(False); UPPERE.append(False)
    Index = 1
    if String == CAPS:
        presskey(CAPSLOCK)
    elif String == LOWER:
        LOWERE[0] = True
        Index = 0
    elif String == UPPER:
        UPPERE[0] = True
        Index = 0
    else:
        for Letter in String: 
            presskey(Letter)
    for Letter in Letters:
        if Letter == CAPS:
            presskey(CAPSLOCK)
            Index += 1
            continue
        if LOWERE[Index]:
            presskey(Letter.lower())
            Index += 1
            continue        
        if UPPERE[Index]:
            presskey(Letter.upper())
            Index += 1
            continue        
        if Letter == UPPER:
            UPPERE[Index+1] = True
            Index += 1
            continue        
        if Letter == LOWER:
            LOWERE[Index+1] = True
            Index += 1
            continue        
        presskey(Letter)
        Index += 1
def openTaskbarApp(*NameNumbers:int):
    """Open the taskbar apps given. If a app is open and showing in the taskbar, then too it will work."""
    for NameNumber in NameNumbers:Name = str(NameNumber);presskey((WINDOWS, Name))
def ClickWin(): """Click Windows Icon."""; presskey("win");moveMouse(BOTTOMLEFT)
def Screenshot(FilePath:str, FileName:str="Screenshot", Extension:str="png"):PAG.screenshot(f"{FilePath}\\{FileName}.{Extension}")
def openRun(): """Open Run"""; presskey([WINDOWS, R])
def openTerminal(): """Open Terminal"""; presskey(WINDOWS); sleep(2); type(UPPER, T, E, R, M, I, N, A, L); presskey(ENTER)
def openApp(AppName:str): """Open a app."""; presskey(WINDOWS); type(AppName)
def accept(Tab:bool=False): 
    """Accept a input by Enter or Tab."""
    if Tab: presskey(TAB)
    else: presskey(ENTER)
def give(Tab:bool=False): 
    """Give a input/command by Enter or Tab."""
    if Tab: presskey(TAB)
    else: presskey(ENTER)
def changeSelection():
    """In a app, change the selection by pressing Tab."""
    presskey(TAB)
    
LeftKey = PAG.leftClick
RightKey = PAG.rightClick
ScrollClick = PAG.middleClick

def Scroll(Amount:float, Up:bool=False, Down:bool=True):
    """Scroll in the amount given up or down."""
    if Up: Amount = Amount.__abs__()
    if Down: Amount = 0-(Amount.__abs__())
    PAG.scroll(Amount)

DoubleClick = PAG.doubleClick
TripleClick = PAG.tripleClick

def closeApp(): """Closes any app"""; presskey([ALT, functionKey(4)])
def getCoordinates(): """Returns the current coordinates as Point class."""; return PAG.position()
def pointToCoordinates(Point:PAG.Point): """Get x and y as [x, y] from a Point class."""; return [Point.x, Point.y]