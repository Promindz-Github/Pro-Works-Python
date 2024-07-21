"""This module helps you use GUI more efficiently. In Widgets you have to always use the Window.get() to give the window. Needs pyautogui and tkinter and webbrowser as modules in site-packages."""
# Dveloper -- Promindz
from tkinter.filedialog import askopenfilename as AskOpenFilePath, askopenfile as AskOpenFile, asksaveasfile as AskSaveAs, asksaveasfilename as AskSaveAsPath, askdirectory as AskPath
from tkinter.messagebox import showinfo as popUp, showerror as warnError, showwarning as warn
from tkinter.colorchooser import askcolor
from tkinter.ttk import Progressbar
from pyautogui import position
import tkinter as Widgets

openFile = open
from webbrowser import open
OpenUrl = open
OpenFileManager = open
"""Opens a directory in the file manager. Can open a file normally too like normal apps."""

def Join(Widget, Scrollbar:Widgets.Scrollbar):
    """Joins a Widget and the ScrollBar."""
    Widget.config(yscrollcommand=Scrollbar.set)
    Scrollbar.config(command=Widget.yview)

class Font:
    """Helps to manage the font."""
    def __init__(self, Style:str="Arial Black", Size:int=10, BOLD:bool=False, UNDERLINE:bool=False, ITALIC:bool=False, Widget=None) -> None:
        if BOLD: BOLD = "bold"
        else: BOLD = ""
        if ITALIC: ITALIC = "italic"
        else: ITALIC = ""
        if UNDERLINE: UNDERLINE = "underline"
        else: UNDERLINE = ""
        self.Font = (Style, Size, BOLD + " " + UNDERLINE + " " + ITALIC)
        self.Widget = Widget
        try: self.Widget.config(font=self.Font)
        except: pass
    
    def getWidget(self):
        """Returns the Widget"""
        return self.Widget
    
    def setWidget(self, Widget):
        """Sets the Widget"""
        self.Widget = Widget
        
    def getStyle(self):
        """Returns the Style"""
        return self.Font[0]
        
    def getSize(self):
        """Returns the Size"""
        return self.Font[1]
    
    def changeSize(self, Num:int=1):
        """Different from set, Adds the given number Whether Negative or Positive To the Size."""
        self.Font = (self.Font[0], self.Font[1]+Num, self.Font[2])
        
    def update(self, Widget=None):
        """Update the widget"""
        if Widget == None:
            self.Widget.config(font=self.Font)
        else:
            Widget.config(font=self.Font); self.Widget = Widget

    def getBold(self):
        """Returns True or False if Bold is applied"""
        if self.Font[2] == 'bold':
            return True
        else:
            return False
        
    def getItalic(self):
        """Returns True or False if Italic is applied"""
        if self.Font[3] == 'italic':
            return True
        else:
            return False
        
    def getUnderline(self):
        """Returns True or False if Underline is applied"""
        if self.Font[4] == 'underline':
            return True
        else:
            return False
        
    def setBold(self, Set:bool=True):
        """Sets the Bold on the basis of True or False"""
        if Set: BOLD = "bold"
        else: BOLD = ""
        ALPHABETS = [
            [
                'a',
                'b',
                'c',
                'd',
                'e'
                'f',
                'g',
                'h',
                'i',
                'j',
                'k',
                'l',
                'm',
                'n',
                'o',
                'p',
                'q',
                'r',
                's',
                't',
                'u',
                'v',
                'w',
                'x',
                'y',
                'z'
            ],
            [
                'A',
                'B',
                'C',
                'D',
                'E'
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'
            ]
        ]
        def getChars(self, Text:str=""):
            """Returns a list of characters."""
            Chars = []
            if Text == "":
                for Char in self.Text:
                    Chars.append(Char)
            else:
                for Char in Text:
                    Chars.append(Char)
            return Chars
    
        def getWords(self, Text:str=""):
            """Returns a list of words."""
            Words = []
            Word = ""
            if Text == "":
                Chars = getChars(self.Text)
            else:
                Chars = getChars(Text)
            for Char in Chars:
                if Char == "\n" or Char == " " or not Char in ALPHABETS[0] or not Char in ALPHABETS[1]:
                    Words.append(Word)
                    Words.append(Char)
                    Word = ""
                    continue
                Word += Char
            return Words
        ThisFont = getWords(self.Font[2])
        self.Font = (self.Font[0], self.Font[1], BOLD + " " + ThisFont[1] + " " + ThisFont[2])
        
    def setItalic(self, Set:bool=True):
        """Sets the Italic on the basis of True or False"""
        ALPHABETS = [
            [
                'a',
                'b',
                'c',
                'd',
                'e'
                'f',
                'g',
                'h',
                'i',
                'j',
                'k',
                'l',
                'm',
                'n',
                'o',
                'p',
                'q',
                'r',
                's',
                't',
                'u',
                'v',
                'w',
                'x',
                'y',
                'z'
            ],
            [
                'A',
                'B',
                'C',
                'D',
                'E'
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'
            ]
        ]
        if Set: ITALIC = "italic"
        else: ITALIC = ""
        def getChars(self, Text:str=""):
            """Returns a list of characters."""
            Chars = []
            if Text == "":
                for Char in self.Text:
                    Chars.append(Char)
            else:
                for Char in Text:
                    Chars.append(Char)
            return Chars
    
        def getWords(self, Text:str=""):
            """Returns a list of words."""
            Words = []
            Word = ""
            if Text == "":
                Chars = getChars(self.Text)
            else:
                Chars = getChars(Text)
            for Char in Chars:
                if Char == "\n" or Char == " " or not Char in ALPHABETS[0] or not Char in ALPHABETS[1]:
                    Words.append(Word)
                    Words.append(Char)
                    Word = ""
                    continue
                Word += Char
            return Words
        ThisFont = getWords(self.Font[2])
        self.Font = (self.Font[0], self.Font[1], ThisFont[0] + " " + ITALIC + " " + ThisFont[2])
        
    def setUnderline(self, Set:bool=True):
        """Sets the Underline on the basis of True or False"""
        ALPHABETS = [
            [
                'a',
                'b',
                'c',
                'd',
                'e'
                'f',
                'g',
                'h',
                'i',
                'j',
                'k',
                'l',
                'm',
                'n',
                'o',
                'p',
                'q',
                'r',
                's',
                't',
                'u',
                'v',
                'w',
                'x',
                'y',
                'z'
            ],
            [
                'A',
                'B',
                'C',
                'D',
                'E'
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'
            ]
        ]
        def getChars(self, Text:str=""):
            """Returns a list of characters."""
            Chars = []
            if Text == "":
                for Char in self.Text:
                    Chars.append(Char)
            else:
                for Char in Text:
                    Chars.append(Char)
            return Chars
    
        def getWords(self, Text:str=""):
            """Returns a list of words."""
            Words = []
            Word = ""
            if Text == "":
                Chars = getChars(self.Text)
            else:
                Chars = getChars(Text)
            for Char in Chars:
                if Char == "\n" or Char == " " or not Char in ALPHABETS[0] or not Char in ALPHABETS[1]:
                    Words.append(Word)
                    Words.append(Char)
                    Word = ""
                    continue
                Word += Char
            return Words
        if Set: UNDERLINE = "underline"
        else: UNDERLINE = ""
        ThisFont = getWords(self.Font[2])
        self.Font = (self.Font[0], self.Font[1], ThisFont[0] + " " + ThisFont[2] + " " + UNDERLINE)
    
def OpenFileRead(Path):
    """Reads a file from the given path and returns the text"""
    return openFile(Path, 'r').read()

def OpenFileWrite(Path, WriteText:str=""):
    """Reads a file from the given path and returns the text. If file is no there, raises a error."""
    with openFile(Path, 'w') as File:
        if WriteText != "":
            File.write(WriteText)
        File.close()
    
def OpenFileWrite(Path="C:\\", Text=""):
    """Writes a file to the given wheather created or not."""
    with openFile(Path, 'w')as File:
        File.write(Text)
        File.close()

def OpenFileWriteCreate(Path="C:\\", Text=""):
    """Writes a file to the given wheather created or not. If file is no there, creates a new file."""
    with openFile(Path, 'w+') as File:
        File.write(Text)
        File.close()
        
def OpenFileAdd(Path="C:\\", Text=""):
    """Adds the text given to the given path."""
    with openFile(Path, "a") as File:
        File.write(Text)
        File.close()

def OpenFileAddCreate(Path="C:\\", Text=""):
    """Adds the text given to the given path. If not there, Creates a new if not exists."""
    with openFile(Path, "a+") as File:
        File.write(Text)
        File.close()

def OpenFileReadCreate(Path="C:\\", IfNotExistText:str=""):
    try: return OpenFileRead(Path)
    except: 
        OpenFileWriteCreate(Path, IfNotExistText)
        return OpenFileRead(Path)

ALT = 'Alt'
CTRL = 'Control'
INSERT = 'Insert'
SHIFT = 'Shift'
A="a";B="b";C="c";D="d";E="e";F="f";G="g";H="h";I="i";J="j";K="k";L="l";M="m";N="n";O="o";P="p";Q="q";R="r";S="s";T="t";U="u";V="v";W="w";X="x";Y="y";Z="z"
ADD = 'plus'
PLUS = 'plus'
SUBTRACT = 'minus'
MINUS = 'minus'
HYPHEN = 'minus'
ASTERISK = 'multiply'
MULTIPLY = 'multiply'
DIVIDE = 'divide'
FOREWARD_SLASH = 'divide'
ENTER = 'Return'
HOVER = 'Enter'
STOP_HOVER = 'Leave'
NUM1="1";NUM2="2";NUM3="3";NUM4="4";NUM5="5";NUM6="6";NUM7="7";NUM8="8";NUM9="9";NUM0="0"
LEFTMOUSE = 'Button-1'
SCROLLWHEEL = 'Button-2'
RIGHTMOUSE = 'Button-3'
KEYPRESS = 'KeyPress'
KEYRELEASE = 'KeyRelease'
BUTTONRELEASE = 'ButtonRelease'
BUTTONPRESS = 'ButtonPress'
FUNCTION1 = 'F1'
FUNCTION2 = 'F2'
FUNCTION3 = 'F3'
FUNCTION4 = 'F4'
FUNCTION5 = 'F5'
FUNCTION6 = 'F6'
FUNCTION7 = 'F7'
FUNCTION8 = 'F8'
FUNCTION9 = 'F9'
FUNCTION10 = 'F10'
FUNCTION11 = 'F11'
FUNCTION12 = 'F12'
SPACE = "space"
PRENTHESISOPEN = "("
PRENTHESISCLOSE = ")"
BRACKETOPEN = "["
BRACKETCLOSE = "]"

def getShortcut(*SHORTCUTS):
    """Return shortcuts for keys including mouse."""
    Shortcut = "<"
    for SHORTCUT in SHORTCUTS:
        if SHORTCUT == SHORTCUTS[0]:
            Shortcut += SHORTCUT
            continue
        Shortcut += "-" + SHORTCUT
    Shortcut += ">"
    return Shortcut

class Window:
    """A window generater class that generates a window."""
    def __init__(self, Title="Window -- No Title", Width=500, Height=500):
        """Generate a window and set a default title or the given title."""
        self.Root = Widgets.Tk()
        self.Root.title(Title)
        self.setSize(Width, Height)
        
    def usable(self, Class):
        """Returns the Class by adding the window in it."""
        if type(Class) == type(FullScreen):  return Class(self)
        else: return Class(Root=self)
        
    def resizeable(self, Width=True, Height=True):
        """Sets if the user can resize the window manually"""
        self.Root.resizable(Width, Height)
        
    def unresizeable(self, Width=False, Height=False):
        """Sets if the user can resize the window manually"""
        self.Root.resizable(Width, Height)
        
    def setMenu(self, MenuBar:Widgets.Menu):
        """Sets the Menu of the Root"""
        self.Root.config(menu=MenuBar)
        
    def remove(self):
        """Destroys the window and its all widgets."""
        self.Root.destroy()
        
    def setTitle(self, title):
        """Set the title of the window."""
        self.Root.title(title)
        self.Title = title
        
    def setIcon(self, icopath:str | bool=False, pngpath:str | bool=False):
        if not not icopath:
            self.Root.iconbitmap(pngpath)
        elif not not pngpath:
            self.Root.iconphoto(True, Widgets.PhotoImage(file=pngpath))
        
    def afterSeconds(self, command, miliseconds:int=10):
        self.Root.after(miliseconds, command)
        
    def update(self):
        """Updates the window."""
        self.Root.update()
        
    def updateAll(self):
        """Updates the window and the idle tasks going on like of Progress Bars."""
        self.update()
        self.update_idletasks()
        
    def update_idletasks(self):
        """Updates idle tasks on the window."""
        self.Root.update_idletasks()
        
    def setSize(self, Width=int, Height=int):
        """Set the Size of the window"""
        self.Root.geometry(f"{Width}x{Height}")
        self.Width = Width
        self.Height = Height
        
    def getWidth(self):
        """Return the width of the window."""
        try: return self.Width
        except: return "Not Assigned"
    
    def getHeight(self):
        """Return the height of the window."""
        try: return self.Height
        except: return "Not Assigned"
        
    def getTitle(self) -> str:
        """Returns the title of the window."""
        return self.Title
        
    def finishCode(self):
        """After writing the code for the window use this to show the window."""
        self.Root.mainloop()
        
    def get(self) -> Widgets.Tk:
        """Returns the window object."""
        return self.Root
    
    def BackgroundColor(self, Color:str):
        self.Root.configure(background=Color)
   
    def addShortcutKey(self, Shotcut:str, Command, Arguments:list=[], GiveProperties=False):
        """Add a shortcut key to the window. The shortcut key can be got by command, getShortcut() Args: constants. Also known as bindings. Arguments given here will be given to the function. Make sure that your command takes 
        # all args in a list 
        except the Properties to take at the first."""
        if len(Arguments) == 0:
            if GiveProperties: 
                self.Root.bind(Shotcut, Command)
            else:
                self.Root.bind(Shotcut, lambda event: Command())
        else:
            if GiveProperties: 
                self.Root.bind(Shotcut, lambda Event: Command(Event, Arguments))
            else:
                self.Root.bind(Shotcut, lambda Event: Command(Arguments))
        
    def removeShortcutKey(self, Shortcut, Command=None):
        """Remove a shortcut key from the window."""
        self.Root.unbind(Shortcut, Command)
        print()
class ConnectedWindow(Window):
    """A window generater class that generates a window. Closes when the main window is closed. Needs a mainwindow (Window class)."""
    def __init__(self, Title="Window -- No Title", Width=500, Height=500):
        """Generate a window and set a default title or the given title."""
        self.Root = Widgets.Toplevel()
        self.Root.title(Title)
        self.setSize(Width, Height)
        
WIDTH = "width"
HEIGHT = "height"
CENTER = "center"
TOP = "top"
BOTTOM = "bottom"
LEFT = "left"
RIGHT = "right"

def Screen(ATTRIBUTES:str | tuple[str] | list[str] | dict[str]):
    """Get the attributes of screen asked."""
    if ATTRIBUTES == WIDTH:
        INFO_WIDTH = Widgets.Tk()
        WINFO_WIDTH = INFO_WIDTH.winfo_screenwidth()
        INFO_WIDTH.destroy()
        return WINFO_WIDTH
    elif ATTRIBUTES == HEIGHT:
        INFO_HEIGHT = Widgets.Tk()
        WINFO_HEIGHT = INFO_HEIGHT.winfo_screenheight()
        INFO_HEIGHT.destroy()
        return WINFO_HEIGHT
    elif ATTRIBUTES == CENTER: return (Screen(WIDTH)/2, Screen(HEIGHT)/2)
    elif ATTRIBUTES == TOP: return 0
    elif ATTRIBUTES == LEFT: return 0
    elif ATTRIBUTES == BOTTOM: return Screen(HEIGHT)
    elif ATTRIBUTES == RIGHT: return Screen(WIDTH)
    else:
        Result = []
        for ATTRIBUTE in ATTRIBUTES: Result.append(Screen(ATTRIBUTE))
        return Result
            
class Text:
    """A class that creates a text object."""
    def __init__(self, Master:Window=None, text:str=False, bg:str=False, fg:str=False, font:str | tuple[str] | list[str] | dict[str]=False, PlaceInitially:bool=False, PlaceCoordinates:list[int]=[0, 0], PackInitially:bool=False, GridInitially:bool=False, GridCoordinates:list[int]=[0, 0]):
        """Get all the attributes needed. Grid Coordinates [Row, Column]. Place Coordinates [X, Y]. Pack Normally. Use Gird/Place/PackInitially. font size should be a string"""
        def atFirst(self, String:str, Text:str=""):
            """This returns boolean value indicating if the given string is at the first or not"""
            if Text == "":
                Index = 0
                Bool = True
                for Letter in String:
                    if self.Text[Index] == Letter: pass
                    else: Bool = False; break
                    Index += 1
                    
            else:
                Index = 0
                Bool = True
                for Letter in String:
                    if Text[Index] == Letter: pass
                    else: Bool = False; break
                    Index += 1
                
            return Bool
        def isString(String:str):
            try:
                atFirst("")
                try: String.clear(); return False
                except:
                    return True
            except: return False
        if not not text:
            self.text = text
        if not not bg:
            self.bg = bg
        if not not fg:
            self.fg = fg
        if not not font:
            if not isString(font):
                self.font = font[0]
                for fnt in font:
                    if fnt == font[0]:
                        continue
                    self.font += " " + fnt
                self.font = font
        self.Master = Master
        if GridInitially:
            try:
                self.Label = Widgets.Label(
                    self.Master.get(), text=self.text
                )
            except: 
                self.Label = Widgets.Label(
                    text=self.text
                )
            try: self.Label["bg"] = self.bg
            except: pass
            
            try: self.Label["fg"] = self.fg
            except: pass
            
            try: self.Label["font"] = self.font
            except: pass
            
            self.Label.grid(row=GridCoordinates[0], column=GridCoordinates[1])
        elif PlaceInitially:
            try:
                self.Label = Widgets.Label(
                    self.Master.get(), text=self.text
                )
            except: 
                self.Label = Widgets.Label(
                    text=self.text
                )
            try: self.Label["bg"] = self.bg
            except: pass
            
            try: self.Label["fg"] = self.fg
            except: pass
            
            try: self.Label["font"] = self.font
            except: pass
            
            self.Label.place(x=PlaceCoordinates[0], y=PlaceCoordinates[1])
        elif PackInitially:
            try:
                self.Label = Widgets.Label(
                    self.Master.get(), text=self.text
                )
            except: 
                self.Label = Widgets.Label(
                    text=self.text
                )
            try: self.Label["bg"] = self.bg
            except: pass
            
            try: self.Label["fg"] = self.fg
            except: pass
            
            try: self.Label["font"] = self.font
            except: pass
            
            self.Label.pack()
        
    def change(self, Master:Window=False, text:str=False, bg:str=False, fg:str=False, font:str | tuple[str, int] | list[str, int] | dict[str, int]=False):
        """Change any attribute."""
        def atFirst(self, String:str, Text:str=""):
            """This returns boolean value indicating if the given string is at the first or not"""
            if Text == "":
                Index = 0
                Bool = True
                for Letter in String:
                    if self.Text[Index] == Letter: pass
                    else: Bool = False; break
                    Index += 1
                    
            else:
                Index = 0
                Bool = True
                for Letter in String:
                    if Text[Index] == Letter: pass
                    else: Bool = False; break
                    Index += 1
                
            return Bool
        def isString(String:str):
            try:
                atFirst("")
                try: String.clear(); return False
                except:
                    return True
            except: return False
        if not not text:
            self.text = text
        if not not bg:
            self.bg = bg
        if not not fg:
            self.bg = fg
        if not not font:
            if not isString(font):
                self.font = font[0]
                for fnt in font:
                    if fnt == font[0]:
                        continue
                    self.font += " " + fnt
                self.font = font
        if not not Master:
            self.Master = Master

    def addShortcutKey(self, Shotcut:str, Command, Arguments:list=[], GiveProperties=False):
        """Add a shortcut key to the window. The shortcut key can be got by command, getShortcut() Args: constants. Also known as bindings. Arguments given here will be given to the function. Make sure that your command takes 
        # all args in a list 
        except the Properties to take at the first."""
        if len(Arguments) == 0:
            if GiveProperties: 
                self.Label.bind(Shotcut, Command)
            else:
                self.Label.bind(Shotcut, lambda event: Command())
        else:
            if GiveProperties: 
                self.Label.bind(Shotcut, lambda Event: Command(Event, Arguments))
            else:
                self.Label.bind(Shotcut, lambda Event: Command(Arguments))
        
    def removeShortcutKey(self, Shortcut, Command=None):
        """Remove a shortcut key from the window."""
        if Command == None:
            self.Label.unbind(sequence=Shortcut)
        else:
            self.Label.unbind(Shortcut, Command)
    config = change
    configure = change
    BOTH = 'both'
    """Pack Options"""
    X = 'x'
    """Pack Options"""
    Y = 'y'
    """Pack Options"""
    LEFT = 'left'
    """Pack Options"""
    RIGHT = 'right'
    """Pack Options"""
    BOTTOM = 'bottom'
    """Pack Options"""
    TOP = 'top'
    """Pack Options"""
    def pack(self, padx:int=False, pady:int=False, anchor:str=False, expand:bool=False, fill:str=False, side:str=False):
        """Pack a widget. fill can be X, Y or BOTH."""
        try:
            self.Label = Widgets.Label(
                self.Master.get(), text=self.text
            )
        except: 
            self.Label = Widgets.Label(
                text=self.text
            )
        try: self.Label["bg"] = self.bg
        except: pass
        
        try: self.Label["fg"] = self.fg
        except: pass
        
        try: self.Label["font"] = self.font
        except: pass
        
        if not not padx:
            if not not pady:
                if not not anchor:
                    if not not fill:
                        if not not side:
                            self.Label.pack(padx=padx, pady=pady, anchor=anchor, expand=expand, fill=fill, side=side)
                        else:
                            self.Label.pack(padx=padx, pady=pady, anchor=anchor, expand=expand, fill=fill)
                    else:
                        if not not side:
                            self.Label.pack(padx=padx, pady=pady, anchor=anchor, expand=expand, side=side)
                        else:
                            self.Label.pack(padx=padx, pady=pady, anchor=anchor, expand=expand)
                else:
                    if not not fill:
                        if not not side:
                            self.Label.pack(padx=padx, pady=pady, anchor=anchor, expand=expand, side=side)
                        else:
                            self.Label.pack(padx=padx, pady=pady, anchor=anchor, expand=expand)
                        self.Label.pack(padx=padx, pady=pady, expand=expand, fill=fill)
                    else:
                        self.Label.pack(padx=padx, pady=pady, expand=expand)
            else:
                if not not anchor:
                    if not not fill:
                        self.Label.pack(padx=padx, pady=pady, anchor=anchor, expand=expand, fill=fill)
                    self.Label.pack(padx=padx, anchor=anchor, expand=expand)
                else:
                    if not not fill:
                        self.Label.pack(padx=padx, pady=pady, anchor=anchor, expand=expand, fill=fill)
                    self.Label.pack(padx=padx, expand=expand)
        else:
            if not not pady:
                if not not anchor:
                    if not not fill:
                        if not not side:
                            self.Label.pack(pady=pady, anchor=anchor, expand=expand, fill=fill, side=side)
                        else:
                            self.Label.pack(spady=pady, anchor=anchor, expand=expand, fill=fill)
                    else:
                        if not not side:
                            self.Label.pack(pady=pady, anchor=anchor, expand=expand, side=side)
                        else:
                            self.Label.pack(pady=pady, anchor=anchor, expand=expand)
                else:
                    if not not fill:
                        if not not side:
                            self.Label.pack(pady=pady, expand=expand, fill=fill, side=side)
                        else:
                            self.Label.pack(pady=pady, expand=expand, fill=fill)
                    else:
                        if not not side:
                            self.Label.pack(pady=pady, expand=expand, side=side)
                        else:
                            self.Label.pack(pady=pady, expand=expand)
            else:
                if not not anchor:
                    if not not fill:
                        if not not side:
                            self.Label.pack(anchor=anchor, expand=expand, fill=fill, side=side)
                        else:
                            self.Label.pack(anchor=anchor, expand=expand, fill=fill)
                    else:
                        if not not side:
                            self.Label.pack(anchor=anchor, expand=expand, side=side)
                        else:
                            self.Label.pack(anchor=anchor, expand=expand)
                else:
                    if not not fill:
                        if not not side:
                            self.Label.pack(expand=expand, fill=fill, side=side)
                        else:
                            self.Label.pack(expand=expand, fill=fill)
                    else:
                        if not not side:
                            self.Label.pack(expand=expand, side=side)
                        else:
                            self.Label.pack(expand=expand)

    def grid(self, row:int=0, column:int=0):
        try:
            self.Label = Widgets.Label(
                self.Master.get(), text=self.text
            )
        except: 
            self.Label = Widgets.Label(
                text=self.text
            )
        try: self.Label["bg"] = self.bg
        except: pass
        
        try: self.Label["fg"] = self.fg
        except: pass
        
        try: self.Label["font"] = self.font
        except: pass
        
        self.Label.grid(row=row, column=column)
        
    def place(self, x:int=0, y:int=0):
        try:
            self.Label = Widgets.Label(
                self.Master.get(), text=self.text
            )
        except: 
            self.Label = Widgets.Label(
                text=self.text
            )
        try: self.Label["bg"] = self.bg
        except: pass
        
        try: self.Label["fg"] = self.fg
        except: pass
        
        try: self.Label["font"] = self.font
        except: pass
        
        self.Label.place(x=x, y=y)
            
    TEXT = 'text'
    FONT = 'font'
    BG = 'bg'
    ALL = 'all'
    FG = 'fg'
            
    def update(self, Item:str=ALL):
        def atFirst(self, String:str, Text:str=""):
            """This returns boolean value indicating if the given string is at the first or not"""
            if Text == "":
                Index = 0
                Bool = True
                for Letter in String:
                    if self.Text[Index] == Letter: pass
                    else: Bool = False; break
                    Index += 1
                    
            else:
                Index = 0
                Bool = True
                for Letter in String:
                    if Text[Index] == Letter: pass
                    else: Bool = False; break
                    Index += 1
                
            return Bool
        def isString(String:str):
            try:
                atFirst("")
                try: String.clear(); return False
                except:
                    return True
            except: return False
        if Item.lower()=="all":
            if not isString(self.font):
                    self.font = self.font[0]
                    for fnt in self.font:
                        if fnt == self.font[0]:
                            continue
                        self.font += " " + fnt
                    self.font = self.font
            self.Label['font'] = self.font
            self.Label['fg'] = self.fg
            self.Label['bg'] = self.bg
            self.Label['text'] = self.text
        elif "text" in Item.lower():
            self.Label['text'] = self.text
        elif "bg" in Item.lower():
            self.Label['bg'] = self.bg
        elif "fg" in Item.lower():
            self.Label['fg'] = self.fg
        elif "font" in Item.lower():
            if not isString(self.font):
                    self.font = self.font[0]
                    for fnt in self.font:
                        if fnt == self.font[0]:
                            continue
                        self.font += " " + fnt
            self.Label['font'] = self.font
        
            
            
class FullScreen:
    """A class that helps with the handling of fullscreen mode"""
    def __init__(self, Root:Window, Mode:bool=False):"""Takes a Tk and a Mode. Tk will be fullscreen is mode is True, if mode is False, it will be False.""";self.Mode = Mode;self.Root = Root.Root;self.Root.attributes("-fullscreen", self.Mode)
    def On(self):"""Remove the fullscreen mode."""; self.Mode = True ;self.Root.attributes("-fullscreen", self.Mode)
    def Off(self):"""Set the fullscreen mode."""; self.Mode = False ; self.Root.attributes("-fullscreen", self.Mode) 
    def Toggle(self):"""If in fullscreen mode, remove it and if not there, put it."""; self.Mode = not self.Mode; self.Root.attributes("-fullscreen", self.Mode)

def Destroy(List:list):
    """Destroy a list of Widgets given."""
    for Widget in List: 
        try: Widget.destroy() 
        except: Widget.remove()
        
class Yes: pass
class No: pass
        
class Form:
    """A class that helps with the creation of a form with some entries."""
    def __init__(self, Master:Window, Entries:list[str], Types:list, TitleEffect:Yes | No=No, OutputPATH:str=".\\"):
        """A class that creates form.\n
        Write StringVar for text,\n
                IntVar for number,\n
                DoubleVar for Deciamal,\n
                BooleanVar for True or False,\n
        # Only two lists can change all the form.\n
        The Entries should have the names of the entries you want.\n
        The Types should have the type of the entries you want index should be same of relatives.\n
        # Output Path is compalsary that stores the values entered by the user at that path.\n
        Output Path should contain the file name and extension. If it is not created, do not worry just give the path."""

        Root = Master.get()
        self.Master = Master

        self.Entries = Entries
        self.Types = Types
        self.PATH = OutputPATH
        self.TitleEffect = TitleEffect

        if TitleEffect == Yes:
            Root.title("Form - Unsumbitted")


        self.CustEntries = []
        self.CustLabels = []
        self.CustVars = []

        Widgets.Label(Root, text="Welcome !", font="Arial 10 bold").grid(row=0, column=0)

        Index = 0
        Row = 2
        Column = 0
        for Entr in Entries:
            self.CustVars.append(Types[Index]())
            self.CustLabels.append(Widgets.Label(
                Root, text=Entr, font="Arial 10 bold"
            ))
            self.CustEntries.append(Widgets.Entry(
                Root, textvariable=self.CustVars[Index]
            ))
            if Entr.lower() == "password":
                self.CustEntries[Index]['show'] = "*"
            
            self.CustLabels[Index].grid(row=Row, column=Column)
            self.CustEntries[Index].grid(row=Row, column=Column+2)
            
            Row += 2
            
            Index += 1
            
        Widgets.Button(Root, text="Sumbit", font="Arial 10 bold", command=self.Sumbit).grid(row=Row+2, column=0)
            
        Root.mainloop()
        
    def Sumbit(self):
        INDEX = 0
        Write = "\n"
        for Var in self.CustVars:
            Write += f"{self.Entries[INDEX]}:{Var.get()}, "
            INDEX += 1
        openFile(self.PATH, 'a+').write(Write)
        if self.TitleEffect == Yes:
            self.Master.setTitle("Form - Sumbitted")
            
    def setTitleEffect(self, TitleEffect: Yes | No=Yes):
        self.TitleEffect = TitleEffect
        
BooleanVar = Widgets.BooleanVar
StringVar = Widgets.StringVar
DoubleVar = Widgets.DoubleVar
IntVar = Widgets.IntVar


def Grid(InOneRow:int, NowWidget:list, InitRow:int=0, InitColumn:int=0):
    """Helps to grid items more efficiently.If a widget is found None, then the widget is not gridded and the next or previous grid's posittion does not change."""
    for Widget in NowWidget:
        if Widget == None:
            if InitColumn == InOneRow:
                InitRow += 1
                InitColumn = 0            
            continue
        Widget.grid(row=InitRow, column=InitColumn)
        InitColumn += 1
        if InitColumn == InOneRow:
            InitRow += 1
            InitColumn = 0

class TextArea:
    """Creates a text area to write the text."""
    def __init__(self, Root:Window=None, PackInitially:bool=False, GridInitially:bool=False, Width:int=500, Height:int=500, PlaceInitially:bool=False, GridCoordinates:tuple[int]=(0, 0), PlaceCoordinates:tuple[int]=(0, 0), PackFullScreen:bool=False, PackFullWindow:bool=True, bg:str="#ffffff", fg:str="#000000", CursorColor:str="#000000") -> None:
        """Grid Coordinates [Row, Column] 
        \n Place Coordinates [x, y]"""
        self.MyTextArea = Widgets.Text(width=Width, height=Height, bg=bg, fg=fg, insertbackground=CursorColor)
        if Root != None:
            if type(Root) != type(self):
                self.MyTextArea.master = Root.get()
            else:
                self.MyTextArea.master = Root
        if PackInitially:
            if PackFullScreen: self.MyTextArea.config(width=Screen(WIDTH), height=Screen(HEIGHT)); self.MyTextArea.pack()
            elif PackFullWindow: self.MyTextArea.pack(expand=True, fill='both')
        elif PlaceInitially: self.MyTextArea.place(x=PlaceCoordinates[0], y=PlaceCoordinates[1])
        elif GridInitially: self.MyTextArea.grid(row=GridCoordinates[0], column=GridCoordinates[1])

        self.config = self.MyTextArea.config
        self.configure = self.MyTextArea.configure
        self.get = self.MyTextArea.get
        self.insertText = self.MyTextArea.insert
        self.deleteText = self.MyTextArea.delete
        
        self.delete = self.MyTextArea.destroy
        self.index = self.MyTextArea.index
        self.pack = self.MyTextArea.pack
        
    def font(self, font:Font):
        """Saves the font to the text area."""
        font.update(self)
        
    def getAll(self):
        """Returns all the text."""
        return self.MyTextArea.get('1.0', 'end')
        
    def getAllDividedLines(self, STRINGX) -> list[list[str]]:
        """Returns all the text in lines and utted deeper in words (multiList). Needs a PythonHelp.STRINGX (the class should be called before the method is called.)"""
        retur = STRINGX.getSentences(self.getAll()[:len(self.getAll())-2])
        retu = []
        for r in retur:
            retu.append(STRINGX.getWords(r))
        return retu

    def getAllLines(self, STRINGX) -> list[str]:
        """Returns all the text in lines. Needs a PythonHelp.STRINGX (the class should be called before the method is called.)"""
        return STRINGX.getSentences(self.getAll()[:len(self.getAll())-2])

    def grid(self, Row:int=0, Column:int=0):
        """Grid the textarea on the specified location."""
        self.MyTextArea.grid(row=Row, column=Column)

    def packInMode(self, FullScreen:bool=False, FullWindow:bool=False):
        """Pack the textarea on the specified location."""
        if FullScreen: self.MyTextArea.config(width=Screen(WIDTH), height=Screen(HEIGHT)); self.MyTextArea.pack()
        elif FullWindow: self.MyTextArea.pack(expand=True, fill='both')

    def place(self, X:int=0, Y:int=0):
        """Place the textarea on the specified location."""
        self.MyTextArea.place(x=X, y=Y)
        
    def deleteAllText(self):
        """Deletes all the text."""
        self.MyTextArea.delete("1.0", 'end')
        
    def insertAtLast(self, Text, Color="#fff"):
        """Insert all the text at the last."""
        self.MyTextArea.insert('end', Text, Color)
        
    def insertAtStart(self, Text, Color="#fff"):
        """Insert all the text at the first."""
        self.MyTextArea.insert("1.0", Text, Color)
    
    def getIndex(self, Line:int=0, Char:int=0, Chars:str=""):
        """Returns the index of the char given. Line index starts from 1. Char index starts from 0. Chars are the characters whose last index should be given."""
        if Chars == "":
            return str(Line) + "." + str(Char)
        else:
            Indexes = []
            index = 0
            for char in Chars:
                if char == "\n":
                    Indexes.append(index)
                index += 1
            Line = len(Indexes)-2
            Char = len(Chars)-Indexes[len(Indexes)-2]-2
            return self.getIndex(Line, Char)

    def getCurrent(self):
        """Returns current index position"""
        return self.MyTextArea.index('insert')
    
    END = 'end'
    START = 'start'
    FIRST = 'start'
    LAST = 'end'
    CURRENT = 'current'
    
    def indexIncrement(self, oldIndex:str='current', indexToIncrease:str="None", Line:int=0, Char:int=0):
        """Choose one - indexToIncrease or Line and Char. Return the increased index. oldIndex can be start, end or current. oldIndex can also be gotten by getIndex"""
        if oldIndex == "current":
            oldIndex = self.float(self.getCurrent())
        elif oldIndex == "start":
            oldIndex = 1.0
        elif oldIndex == "end":
            oldIndex = self.float(self.getIndex(Chars=self.getAll()))
            
        if indexToIncrease != "None":
            indexToIncrease = float(indexToIncrease)
            oldIndex = float(oldIndex)
        else:
            indexToIncrease = float(self.getIndex(Line, Char))
        return str(oldIndex + indexToIncrease)
    
    def float(self, String):
        """Returns the string representation of a int or float."""
        return float(f"{String}")
    
    def normalStr(self, String):
        """Returns the string representation in a string."""
        return f"{String}"
    
    def indexDecrement(self, oldIndex:str='current', indexToDecrease:str="None", Line:int=0, Char:int=0):
        """Choose one - indexToDecrease or Line and Char. Return the decreased index. oldIndex can be start, end or current. oldIndex can also be gotten by getIndex"""
        if oldIndex == "current":
            oldIndex = self.float(self.getCurrent())
        elif oldIndex == "start":
            oldIndex = 1.0
        elif oldIndex == "end":
            oldIndex = self.float(self.getIndex(Chars=self.getAll()))
            
        if indexToDecrease != "None":
            indexToDecrease = float(indexToDecrease)
            oldIndex = float(oldIndex)
        else:
            indexToDecrease = float(self.getIndex(Line, Char))
    
        return str(oldIndex - indexToDecrease)
        
    
        
    def select(self, start:str="1.0", end:str="end"):
        """Select the text in the range."""
        self.MyTextArea.tag_add("sel", start, end)
        
    def deselect(self, start:str="1.0", end:str="end"):
        """Deselect the text in the range."""
        self.MyTextArea.tag_remove("sel", start, end)

    def moveCursor(self, index):
        self.MyTextArea.mark_set("insert", index)    
        
    def selectionColorFg(self, color:str):
        """Change the color of the text selected."""
        self.MyTextArea.tag_config(color+"colored", foreground=color)
        
    def selectionColorBg(self, color:str):
        """Change the color of the text selected."""
        self.MyTextArea.tag_config(color+"colored", background=color)

    def inRangeColorBg(self, start:str, end:str, color:str):
        """Change the color of the text in the range given."""
        self.MyTextArea.tag_add(color, start, end)
        self.MyTextArea.tag_config(color, background=color)

    def inRangeColorFg(self, start:str, end:str, color:str):
        """Change the color of the text in the range given."""
        self.MyTextArea.tag_add(color, start, end)
        self.MyTextArea.tag_config(color, foreground=color)
        
    def addShortcutKey(self, Shotcut:str, Command, Arguments:list=[], DictArgs:dict={}, GiveProperties=False):
        """Add a shortcut key to the window. The shortcut key can be got by command, getShortcut() Args: constants. Also known as bindings. Arguments given here will be given to the function. Make sure that your command takes
        the Properties to take at the first.Arguments Second"""
        if len(Arguments) == 0:
            if len(DictArgs) == 0:
                if GiveProperties: 
                    self.MyTextArea.bind(Shotcut, Command)
                else:
                    self.MyTextArea.bind(Shotcut, lambda event: Command())
            else:
                if GiveProperties: 
                    self.MyTextArea.bind(Shotcut, lambda event: Command(event, **DictArgs))
                else:
                    self.MyTextArea.bind(Shotcut, lambda event: Command(**DictArgs))
        else:
            if len(DictArgs) == 0:
                if GiveProperties: 
                    self.MyTextArea.bind(Shotcut, lambda event: Command(event, *Arguments))
                else:
                    self.MyTextArea.bind(Shotcut, lambda event: Command(*Arguments))
            else:
                if GiveProperties: 
                    self.MyTextArea.bind(Shotcut, lambda event: Command(event, *Arguments, **DictArgs))
                else:
                    self.MyTextArea.bind(Shotcut, lambda event: Command(*Arguments, **DictArgs))
        
    def removeShortcutKey(self, Shortcut, Command=None):
        """Remove a shortcut key from the window."""
        if Command == None:
            self.MyTextArea.unbind(sequence=Shortcut)
        else:
            self.MyTextArea.unbind(Shortcut, Command)
    def colorWordFg(self, words:list[str] | str, color:str, tillLast:bool=False):
        """Colors the words. Needed to update every second. Use loops to do this."""
        if type(words) == str: words = [words]
        def color_word(text_widget:Widgets.Text, word, color, tillLast):
            start = "1.0"
            while True:
                start = text_widget.search(word, start, stopindex='end')
                if not start:
                    break
                if not tillLast:
                    end = f"{start}+{len(word)}c"
                else:
                    end = f"{start[0]}.end-0c"
                text_widget.tag_add(color+"colored", start, end)
                text_widget.tag_config(f"{color}colored", foreground=color)
                start = end
        for word in words:
            color_word(self.MyTextArea, word, color, tillLast)

    def removeColor(self, color:str, Area:tuple[str, str] | list[str, str]=["1.0", "end"]):
        """Removes the color or selection given. Area is not compalsary, it defines from where to where the color should be removed. Normally defines the whole area."""
        self.MyTextArea.tag_remove(color+"colored", Area[0], Area[1])

    def colorWordBg(self, words:list[str] | str, color, tillLast:bool=False):
        """Colors the words. Needed to update every second. Use loops to do this."""
        if type(words) == str: words = [words]
        def color_word(text_widget:Widgets.Text, word, color, tillLast):
            start = "1.0"
            while True:
                start = text_widget.search(word, start, stopindex='end')
                if not start:
                    break
                if not tillLast:
                    end = f"{start}+{len(word)}c"
                else:
                    end = f"{start[0]}.end-0c"
                text_widget.tag_add(f"{color}colored", start, end)
                text_widget.tag_config(f"{color}colored", background=color)
                start = end
        for word in words:
            color_word(self.MyTextArea, word, color, tillLast)
    def removeColorWordFg(self, words:list[str] | str, color:str, tillLast:bool=False):
        """Colors the words. Needed to update every second. Use loops to do this."""
        if type(words) == str: words = [words]
        def color_word(text_widget:Widgets.Text, word, color, tillLast):
            start = "1.0"
            while True:
                start = text_widget.search(word, start, stopindex='end')
                if not start:
                    break
                if not tillLast:
                    end = f"{start}+{len(word)}c"
                else:
                    end = f"{start[0]}.end-0c"
                text_widget.tag_remove("colored", start, end)
                text_widget.tag_config("colored", foreground=color)
                start = end
        for word in words:
            color_word(self.MyTextArea, word, color, tillLast)

    def removeColorWordBg(self, words:list[str] | str, color, tillLast:bool=False):
        """Colors the words. Needed to update every second. Use loops to do this."""
        if type(words) == str: words = [words]
        def color_word(text_widget:Widgets.Text, word, color, tillLast):
            start = "1.0"
            while True:
                start = text_widget.search(word, start, stopindex='end')
                if not start:
                    break
                if not tillLast:
                    end = f"{start}+{len(word)}c"
                else:
                    end = f"{start[0]}.end-0c"
                text_widget.tag_remove("colored", start, end)
                text_widget.tag_config("colored", background=color)
                start = end
        for word in words:
            color_word(self.MyTextArea, word, color)
    def colorCursor(self, Color):
        self.config(insertbackground=Color)
            
class Attributes: """A class that helps to add attributes to the var in which this class it saved"""; pass
            
        
class Menubar:
    """Create a Menubar"""
    def __init__(self, Root:Window, Texts:tuple[str] | list[str] | dict[str]=[], Commands:list | tuple | dict=[], Cascade:bool=False, Cutoff:bool=False, Name:str=""):
        """Texts contains the list of names of Texts it should have. Commands are the commands of the Text when it is pressed. If you want to add a Menu in the Bar, Create another Menubar and give Cascade to True and give Root to the Bar by tab(). It gives automatically.. and then you can manage both of them differently. Likewise, a menu can also have a menu in it that can be created as I told earlier. Cutoff tells if it can be cut of the window or not by pressing the button '- - - - -'. Give the menu name nesssacary if a menu in a bar."""
        if not Cascade:
            self.Menu = Widgets.Menu(Root.get())
            Root.Root.config(menu=self.Menu)
        elif Cascade:
            self.Menu = Widgets.Menu(Root.get())
            if not Cutoff: self.Menu['tearoff'] = 0
            Root.tab(Name, self.Menu)
            
        Index = 0
        for Text in Texts:
            self.Menu.add_command(label=Text, command=Commands[Index])
            Index += 1
    
    def tab(self, Tabname:str, Tab):
        """Add a tab to the menu."""
        self.Menu.add_cascade(label=Tabname, menu=Tab)
        
    def addSeparator(self):
        """Add a separator to the menu."""
        self.Menu.add_separator()
            
    def addCommand(self, text:str, command):
        """Add a command to the menu."""
        self.Menu.add_command(label=text, command=command)
        
    def get(self):
        """Returns the main worker."""
        return self.Menu
    
class DoubleClickEvent:
    """When double clicked what will happen."""
    def __init__(self, Widget, onSingleClick, onDoubleClick, key:str="<Button-1>", Properties:bool=False, singleClickArguments:tuple=(), doubleClickArguments:tuple=(), toNormal=False) -> None:
        """Takes a Root as a Window. onSingleClick means the function to call when we click on time. The next time onDoubleClick wil run. The key to check is LEFTMOUSE can be changed by key parameter. If you want to change key, make sure you have gotten the shortcut (event) key by getShortcut(). To get the properties, set Properties to false. Argumnets can also be given by singleArguments and doublearguments. onIdle means when it is to be switched to normal."""
        self.Widget, self.key, self.onSingleClick, self.onDoubleClick, self.singleClickArguments, self.doubleClickArguments, self.Properties = Widget, key, onSingleClick, onDoubleClick, singleClickArguments, doubleClickArguments, Properties
        if not not toNormal: self.toNormal = toNormal
        def Cmd(): 
            onSingleClick()
            try: 
                Widget.removeShortcutKey(key)
                Widget.addShortcutKey(key, Ccmd, GiveProperties=Properties, Arguments=singleClickArguments)
            except:
                Widget.unbind(key)
                if Properties:
                    Widget.bind(
                        key,
                        Ccmd
                    )
                else:
                    Widget.bind(
                        key,
                        lambda event: Ccmd()
                    )
        def Ccmd():
            onDoubleClick()
            try:
                Widget.removeShortcutKey(key)
                Widget.addShortcutKey(key, Cmd, GiveProperties=Properties, Arguments=doubleClickArguments)
            except:
                Widget.unbind(key)
                if Properties:
                    Widget.bind(
                        key,
                        Cmd
                    )
                else:
                    Widget.bind(
                        key,
                        lambda event: Cmd()
                    )

        try:
            Widget.addShortcutKey(
                key,
                Cmd,
                GiveProperties=Properties,
                Arguments=singleClickArguments
            )
        except:
            if Properties:
                Widget.bind(
                    key,
                    Cmd
                )
            else:
                Widget.bind(
                    key,
                    lambda event: Cmd()
                )
                
    def recreate(self, Widget, onSingleClick, onDoubleClick, key:str="<Button-1>", Properties:bool=False, singleClickArguments:tuple=(), doubleClickArguments:tuple=(), toNormal=False) -> None:
        """Takes a Root as a Window. onSingleClick means the function to call when we click on time. The next time onDoubleClick wil run. The key to check is LEFTMOUSE can be changed by key parameter. If you want to change key, make sure you have gotten the shortcut (event) key by getShortcut(). To get the properties, set Properties to false. Argumnets can also be given by singleArguments and doublearguments."""
        self.Widget, self.key, self.onSingleClick, self.onDoubleClick = Widget, key, onSingleClick, onDoubleClick
        if not not toNormal: self.toNormal = toNormal
        def Cmd(): 
            onSingleClick()
            try: 
                Widget.removeShortcutKey(key)
                Widget.addShortcutKey(key, Ccmd, GiveProperties=Properties, Arguments=singleClickArguments)
            except:
                Widget.unbind(key)
                if Properties:
                    Widget.bind(
                        key,
                        Ccmd
                    )
                else:
                    Widget.bind(
                        key,
                        lambda event: Ccmd()
                    )
        def Ccmd():
            onDoubleClick()
            try:
                Widget.removeShortcutKey(key)
                Widget.addShortcutKey(key, Cmd, GiveProperties=Properties, Arguments=doubleClickArguments)
            except:
                Widget.unbind(key)
                if Properties:
                    Widget.bind(
                        key,
                        Cmd
                    )
                else:
                    Widget.bind(
                        key,
                        lambda event: Cmd()
                    )

        try:
            Widget.addShortcutKey(
                key,
                Cmd,
                GiveProperties=Properties,
                Arguments=singleClickArguments
            )
        except:
            if Properties:
                Widget.bind(
                    key,
                    Cmd
                )
            else:
                Widget.bind(
                    key,
                    lambda event: Cmd()
                )
                
    def leaveClick(self):
        """Runs the onIdle command to leave the widget."""
        self.toNormal()
        self.deleteEvent()
        self.recreate(self.Widget, self.onSingleClick, self.onDoubleClick, self.key, self.Properties, self.singleClickArguments, self.doubleClickArguments, self.toNormal)
                
    def deleteEvent(self):
        try:
            self.Widget.removeShortcutKey(self.key)
        except:
            self.Widget.unbind(self.key)