"""Helps to manage the python works efficiently."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep as delayTime
from winsound import PlaySound, Beep, MessageBeep, SND_FILENAME
from requests import get
import pyautogui as auto
import tkinter as mmp
import cv2 as Camera
import numpy as np
import os as Oper

def tryToDo(Function):
    """Returns True if the function is called successfully, returns False otherwise."""
    try: Function(); return True
    except: return False

from shutil import move as moveFiles
from winshell import CreateShortcut
from os import remove as removeFiles, removedirs as removeFolders, makedirs as makeFolders

GetUrl = get

def setattr(obj, key, value):
    """Set the attribute to a pirticular object, the key should be a string containing the name."""
    setattr(obj, key, value)

def getattr(obj, key):
    """Get the attribute from a pirticular object, the key should be a string containing the name."""
    return getattr(obj, key)

def surround(String, LineUp, LineDown, LineLeft, LineRight):
    """Sorround a string by some strings from four directions."""
    String += LineRight + "\n" + LineDown
    return (LineUp + "\n" + LineLeft + String)

def Error(Message='Not Found', Item='File'):
    return f'''Got an Error during the Task that the {Item} was {Message}'''

def Sound(FilePath):
    """Plays the sound using the filepath given. PlaySound() takes two args, if you use it, give the second arg as SND_FILENAME"""
    PlaySound(FilePath, SND_FILENAME)


getUSERNAME = lambda: Oper.getenv('USERNAME')
getEnvVar = Oper.getenv
def newVariable(Name:str, Value:str):
    """Enviourment Variables are set using this. These are later used by system for many purposes ex: CLI apps in terminal are always written relatively untill their directory path is not in env variables."""
    Oper.environ[Name] = Value
getBasename = Oper.path.basename

ALPHABETS = [
    [
        'a',
        'b',
        'c',
        'd',
        'e',
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
        'E',
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
SPECIALS = [
    "(",
    ")",
    "*",
    "&",
    "^",
    "%",
    "$",
    "#",
    "₹",
    "@",
    "!",
    "\\",
    "/",
    "?",
    ".",
    ",",
    "<",
    ">",
    "'",
    "\"",
    "`",
    "~",
    "-",
    "+",
    ";",
    ":",
    "[",
    "]",
    "{",
    "}",
    "|",
    " ",
    "\n",
    "\t"
]
UNUSED = [
    "\r",
    "\0",
    "\b",
    "\f",
    "\v",
    "\u0000",
    "\u0001",
    "\u0002",
    "\u0003",
    "\u0004",
    "\u0005",
    "\u0006",
    "\u0007",
    "\u0008",
    "\u0009",
    "\u000a",
    "\u000b",
    "\u000c",
    "\u000d",
    "\u000e",
    "\u000f",
    "\u0010",
    "\u0011",
    "\u0012",
    "\u0013",
    "\u0014",
    "\u0015",
    "\u0016",
    "\u0017",
    "\u0018",
    "\u0019",
    "\u001a",
    "\u001b",
    "\u001c",
    "\u001d",
    "\u001e",
    "\u001f",
    "\u0020",
    "\u0021",
    "\u0022",
    "\u0023",
    "\u0024",
    "\u0025",
    "\u0026",
    "\u0027",
    "\u0028",
    "\u0029",
    "\u002a",
    "\u002b",
    "\u002c",
    "\u002d",
    "\u002e",
    "\u002f",
    "\u0030",
    "\u0031",
    "\u0032",
    "\u0033",
    "\u0034",
    "\u0035",
    "\u0036",
    "\u0037",
    "\u0038",
    "\u0039",
    "\u003a",
    "\u003b",
    "\u003c",
    "\u003d",
    "\u003e",
    "\u003f",
    "\u0040",
    "\u0041",
    "\u0042",
    "\u0043",
    "\u0044",
    "\u0045",
    "\u0046",
    "\u0047",
    "\u0048",
    "\u0049",
    "\u004a",
    "\u004b",
    "\u004c",
    "\u004d",
    "\u004e",
    "\u004f"
]

def duplicateList(List):
    l = []
    for I in List:
        l.append(I)
    return l

def removeEmpty(List:list):
    """Removes the empty strings in a list."""
    Index = 0
    for i in List:
        if i == "":  List.pop(Index)
        Index += 1
    

class STRINGX:
    """A STRING class that handles the operations wth the Strings."""
    def __init__(self, Text:str="") -> None:
        self.Text = Text
        
    def getIndexes(self, Text:str="") -> list:
        """Returns a list of indexes like '    ' is the Text so, return [0, 1, 2, 3]"""
        Index = []
        if Text != "":
            for i in range(0, len(Text)):
                Index.append(i)
        else:
            for i in range(0, len(self.Text)):
                Index.append(i)
        return Index
        
    def listToStr(self, List:list=[], charInBetween=" ") -> str:
        """Converts a list of Strings to a string. charInBetween is the char used in between of two strings."""
        if List == []:
            if self.Text == []: return ""
            String = self.Text[0]
            Index = 0
            for iterate in self.Text:
                if Index == 0: continue
                String += charInBetween + iterate
                Index += 1
            return String
        elif List != []:
            String = List[0]
            Index = 0
            for iterate in List:
                if Index == 0: continue
                String += charInBetween + iterate
                Index += 1
            return String
        
    def after(self, Place:str | int, Text:str="", type=str, combination:str=" ", *stopPoints) -> str:
        """Returns what is after the place given in the string including it. You can give a index of a string using type=list, and giving the index in place. For lists, type=list and Place should have the index. combination is used in between two string of a list. Stop ponts will stop when it will get it only in lists. Not include ends."""
        if type == str:
            if Text!="":
                return Text[Text.find(Place)+len(Place):]
            else:
                return self.Text[self.Text.find(Place)+len(Place):]
        elif type == list or type == tuple:
            if Text != "":
                String = Text[Place]
                Index = 0
                for text in Text:
                    if text[0] in stopPoints: break
                    if Index > Place:
                          String += combination + text
                    Index += 1
            else:
                String = self.Text[Place]
                Index = 0
                for text in self.Text:
                    if text[0] in stopPoints: break
                    if Index > Place:
                          String += combination + text
                    Index += 1
                    
            return String

    def before(self, Place:str | int, Text:str="", type=str, combination:str=" ", *stopPoints) -> str:
        """Returns what is before the text given in the string including it. You can give a index of a string using type=list, and giving the index in place. For lists, type=list and Place should have the index. combination is used in between two string of a list. Stop ponts will stop when it will get it only in lists. Not include ends."""
        if type == str:
            if Text!="":
                return Text[:Text.find(String)]
            else:
                return self.Text[:self.Text.find(String)]
        elif type == list or type == tuple or type == dict:
            if Text != "":
                String = Text[Place]
                Index = 0
                for text in reversed(Text):
                    Index = 0; Indes = []
                    for t in text:
                        if t in stopPoints: Indes.append(Index); Index += 1
                    if Index > Place:
                        for t in Indes: ext = self.remove(t, Text=text)
                        String += combination + ext
                    Index += 1
            else:
                String = self.Text[Place]
                Index = 0
                for text in reversed(self.Text):
                    Index = 0; Indes = []
                    for t in text:
                        if t in stopPoints: Indes.append(Index); Index += 1
                    if Index > Place:
                        for t in Indes: ext = self.remove(t, Text=text)
                        String += combination + ext
                    Index += 1
                    
            return String
        
    def isTitleCase(self, Text:str="") -> bool:
        """Return true or false if the text is title case. Title case is a case like 'This'"""
        if Text != "":
            if Text[0] in ALPHABETS[1]: return True
            else: return False
        else:
            if self.Text == "": return 'emptyError'
            if self.Text[0] in ALPHABETS[1]: return True
            else: return False
        
    def isLowerCase(self, Text:str="") -> bool:
        """Return true or false if the text is lower case. Lower case is a case like 'this'"""
        if Text != "":
            if Text.lower() == Text: return True
            else: return False
        else:
            if self.Text.lower() == Text: return True
            else: return False
        
    def isUpperCase(self, Text:str="") -> bool:
        """Return true or false if the text is lower case. Lower case is a case like 'this'"""
        if Text != "":
            if Text.upper() == Text: return True
            else: return False
        else:
            if self.Text.upper() == Text: return True
            else: return False
        
    def toTitleCase(self, Text:str=""):
        """Convert to title case."""
        if Text != "":
            Text = Text.lower()
            Text[0] = Text[0].upper()
            return Text
        else:
            self.Text = self.Text.lower()
            self.Text[0] = self.Text[0].upper()
            return self.Text
        
    def notLetter(self, Text:str=""):
        """Returns a list of Boolean values that indicate whether the given char is a letter or not."""
        Bool = []
        if Text != "":
            for Char in self.getChars(Text):
                if Char in ALPHABETS[0] or Char in ALPHABETS[1]: Bool.append(True)
                else: Bool.append(False)
        else:
            for Char in self.getChars(self.Text):
                if not Char in ALPHABETS[0] or not Char in ALPHABETS[1]: Bool.append(True)
                else: Bool.append(False)
        return Bool
        
    def lastIndex(self, Text:str=""):
        """Returns the First last index of the text given or stored."""
        if Text == "": return len(self.Text)-1
        else: return len(Text)-1
        
    def secondLastIndex(self, Text:str=""):
        """Returns the Second last index of the text given or stored."""
        if Text == "": return len(self.Text)-2
        else: return len(Text)-2
        
    def thirdLastIndex(self, Text:str=""):
        """Returns the Third last index of the text given or stored."""
        if Text == "": return len(self.Text)-3
        else: return len(Text)-3
        
    def fromLastIndex(self, Text:str="", Index:int=0):
        """This returns the Index like 0 - 1 - 2 - 3 but counts from the last"""
        if Text == "": return len(self.Text)-1-Index
        else: return len(Text)-1-Index
        
    def lastChar(self, Text:str=""):
        """Returns the last character in the string given or stored."""
        if Text == "": return self.Text[self.lastIndex(Text)]
        else: return Text[self.lastIndex(Text)]
       
    def secondLastChar(self, Text:str=""):
        """Returns the second last character in the string given or stored.""" 
        if Text == "": return self.Text[self.secondLastIndex(Text)]
        else: return Text[self.secondLastIndex(Text)]
        
    def thirdLastChar(self, Text:str=""):
        """Returns the third last character in the string given or stored."""
        if Text == "": return self.Text[self.thirdLastIndex(Text)]
        else: return Text[self.thirdLastIndex(Text)]
        
    def fromLastChar(self, Text:str="", Index:int=0):
        """This returns the character like 0 - 1 - 2 - 3 but counts from the last."""
        if Text == "": return self.Text[self.fromLastIndex(Text, Index)]
        else: return Text[self.fromLastIndex(Text, Index)]
        
    def atLast(self, String:str, Text:str=""):
        """This returns boolean value indicating if the given string is at the last or not"""
        if Text == "":
            Index = len(self.Text)-1
            Bool = True
            for Letter in reversed(String):
                if self.Text[Index] == Letter: pass
                else: Bool = False; break
                Index -= 1
                
        else:
            Index = len(self.Text)-1
            Bool = True
            for Letter in reversed(String):
                if Text[Index] == Letter: pass
                else: Bool = False; break
                Index -= 1
            
        return Bool
    
    def remove(self, *Index, List=[], Text:str=""):
        if Text == "":
            if List != []:
                Index = List
            MyIndex = 0
            NewText = ""
            for Letter in self.Text:
                if MyIndex in Index:
                    MyIndex += 1          
                    continue
                NewText += Letter
                MyIndex += 1          
        else:
            MyIndex = 0
            NewText = ""
            for Letter in Text:
                if MyIndex in Index:
                    MyIndex += 1          
                    continue
                NewText += Letter
                MyIndex += 1
        return NewText       
            
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

    def getChars(self, Text:str="") -> list[str]:
        """Returns a list of characters."""
        Chars = []
        if Text == "":
            for Char in self.Text:
                Chars.append(Char)
        else:
            for Char in Text:
                Chars.append(Char)
        return Chars
    def getWords(self, Text:str="", *Ends, EliminateEnds:bool=True):
        """Returns a list of words. Ends are the characters on which a line will end."""
        Words = []
        Word = ""
        if Text == "":
            Chars = self.getChars(self.Text)
        else:
            Chars = self.getChars(Text)
        for Char in Chars:
            if Char == "\n" or Char == " " or Char in Ends:
                Words.append(Word)
                if not EliminateEnds:
                    Words.append(Char)
                Word = ""
                continue
            Word += Char
        Words.append(Word)
        return Words

    def getSentences(self, Text:str="", *Ends, EliminateEnds:bool=True) -> list[str]:
        """Returns a list of sentences. Ends are the characters on which a line will end. ExcludeEnds"""
        Words = []
        Word = ""
        if Text == "":
            Chars = self.getChars(self.Text)
        else:
            Chars = self.getChars(Text)
        for Char in Chars:
            if Char == "\n" or Char in Ends:
                Words.append(Word)
                if not EliminateEnds:
                    Words.append(Char)
                Word = ""
                continue
            Word += Char
        Words.append(Word)
        return Words
    
    def join(self, AdditionalText:str, Organize:list[str]=['M', 'A'], MainText:str=""):
        """Joins two strings. Organize should have two chars: A and M. A represents Additional Text, M represents the MainText given or stored. If A is at first, Additional Text will be at the left of the MainText."""
        if MainText == "":
            if Organize[0] == 'M':
                self.Text += AdditionalText
                MainText = self.Text
            elif Organize[0] == 'A':
                AdditionalText += self.Text
                MainText = AdditionalText
        else:
            if Organize[0] == 'M':
                MainText += AdditionalText
            elif Organize[0] == 'A':
                AdditionalText += MainText
        return MainText
def lastItem(Items): 
    """Returns the last item in the list, tuple or dictionary given or stored."""
    STRINGX(Items).lastChar()
def secondLastItem(Items):
    """Returns the second last item in the list, tuple or dictionary given or stored."""
    STRINGX(Items).secondLastChar()
def thirdLastItem(Items):
    """Returns the third last item in the list, tuple or dictionary given or stored."""
    STRINGX(Items).thirdLastChar()
def fromLastItem(Items):
    """This returns the items like 0 - 1 - 2 - 3 but counts from the last."""
    STRINGX(Items).fromLastChar()
    
def lastItemIndex(Items): 
    """Returns the last item in the list, tuple or dictionary given or stored."""
    STRINGX(Items).lastIndex()
def secondLastItemIndex(Items):
    """Returns the second last item in the list, tuple or dictionary given or stored."""
    STRINGX(Items).secondLastIndex()
def thirdLastItemIndex(Items):
    """Returns the third last item in the list, tuple or dictionary given or stored."""
    STRINGX(Items).thirdLastIndex()
def fromLastItemIndex(Items):
    """This returns the items like 0 - 1 - 2 - 3 but counts from the last."""
    STRINGX(Items).fromLastIndex()
    
class RecordingVideo:
    """A class that records video according to the information given."""
    def __init__(self, FilePath:str, FileName:str, QUIT:str, TOGGLE:str, FPS:float | int=30.0):
        """FPS means Frames per second. QUIT means the key name used to quit the program. TOGGLE means the key name used to start or stop the recording."""
        Cam = Camera.VideoCapture(0, Camera.CAP_DSHOW)
        Cam.set(Camera.CAP_PROP_FRAME_WIDTH, 1000)
        Cam.set(Camera.CAP_PROP_FRAME_HEIGHT, 1000)
        
        
        Bool = STRINGX(FileName).AtLast(".mp4")
        
        if Bool: File = FilePath + "\\" + FileName
        else: File = FilePath + "\\" + FileName + ".mp4"

        fourcc = Camera.VideoWriter_fourcc('m', 'p', '4 ', 'v')
        Writer = Camera.VideoWriter(File, fourcc, FPS, (1000, 1000))
        recording = False

        while True:
            ret, frame = Cam.read()
            
            if ret:
                Camera.imshow("Video", frame)
                if recording:
                    Writer.write(frame)
                    
            KeyPress = Camera.waitKey(1)
            if KeyPress == ord(QUIT):
                break
            if KeyPress == ord(TOGGLE):
                recording = not recording
            
        Cam.release()
        Writer.release()
        Camera.destroyAllWindows()        
    
class ScreenRecording:
    def __init__(self, Root:mmp.Tk):

        Root = mmp.Tk()
        Root.title("Recorder")
        BREAK = False

        # Set the screen size to record
        screen_size = (1920, 1080)

        # Define the codec and create VideoWriter object
        fourcc = Camera.VideoWriter_fourcc(*"XVID")
        out = Camera.VideoWriter(f"Output{open(".\\No", "r+").read()}.avi", fourcc, 20.0, screen_size)

        while True:
            # Capture the screen
            img = auto.screenshot()

            # Convert the screenshot to a numpy array
            frame = np.array(img)

            # Convert RGB to BGR
            frame = Camera.cvtColor(frame, Camera.COLOR_RGB2BGR)

            # Write the frame
            out.write(frame)

            # Display the recording in real-time
            # Camera.imshow("screenshot", frame)

            # Check for exit condition

            def Break():
                global BREAK
                BREAK = True
            
            if BREAK:
                Root.destroy()
                break
                
            Root.bind("<Button-1>", lambda event: Break)
            

        # Release resources
        out.release()
        Camera.destroyAllWindows()
        open("No", "w+").write(str(int(open(".\\No", "r").read())+1))
        Root.mainloop()
        
class Check:
    """Check the relation in variable and the value."""
    def __init__(self, Variable, Value):
        """Store the Variable and Value."""
        self.Variable = Variable
        self.Value = Value
        
    def Equals(self):
        """Checks if the Variable and Value are equal."""
        try:
            if self.Variable.get() == self.Value:
                return True
            else:
                return False
        except: 
            if self.Variable == self.Value:
                return True
            else:
                return False
        
    def NotEquals(self):
        """Checks if the Variable and Value aren't equal."""
        try:
            if self.Variable.get()!= self.Value:
                return True
            else:
                return False
        except: 
            if self.Variable != self.Value:
                return True
            else:
                return False
            
    def LessThan(self):
        """Checks if the Variable is less than the Value."""
        try:
            if self.Variable.get() < self.Value:
                return True
            else:
                return False
        except: 
            if self.Variable < self.Value:
                return True
            else:
                return False
            
    def GreaterThan(self):
        """Checks if the Variable is greater than the Value."""
        try:
            if self.Variable.get() > self.Value:
                return True
            else:
                return False
        except: 
            if self.Variable > self.Value:
                return True
            else:
                return False
            
    def LessThanOrEqual(self):
        """Check if the variable is less than or equal to the value."""
        try:
            if self.Variable.get() >= self.Value:
                return True
            else:
                return False
        except:
            if self.Variable >= self.Value:
                return True
            else:
                return False
            
    def GreaterThanOrEqual(self):
        """Check if the variable is greater than or equal to the given value."""
        try:
            if self.Variable.get() <= self.Value:
                return True
            else:
                return False
        except:
            if self.Variable <= self.Value:
                return True
            else:
                return False
            
    def In(self):
        """Check if the variable contains the given value."""
        try:
            if self.Variable.get() in self.Value:
                return True
            else:
                return False
        except:
            if self.Variable in self.Value:
                return True
            else:
                return False
            
    def NotIn(self):
        """Checks if the variable is not in the Value."""
        try:
            if self.Variable.get() not in self.Value:
                return True
            else:
                return False
        except:
            if self.Variable not in self.Value:
                return True
            else:
                return False
            
    def BothEmpty(self, Ignore=""):
        """Checks if the Variable and the Value are empty. Ignores the given value."""
        if Ignore == "":
            try:
                if self.Variable.get() == '' and self.Value == '':
                    return True
                else:
                    return False
            except:
                if self.Variable == '' and self.Value == '':
                    return True
                else:
                    return False
        elif Ignore != "":
            IgnoredVariable = self.Variable.replace(Ignore, "")
            IgnoredValue = self.Value.replace(Ignore, "")
            if IgnoredVariable == "" and IgnoredValue == "":
                return True
            else:
                return False

            
                
    def OneEmpty(self, Ignore=""):
        """Checks if one of them are empty. Ignores the given value."""
        if Ignore == "":
            try:
                if self.Variable.get() == '' or self.Value == '':
                    return True
                else:
                    return False
            except:
                if self.Variable == '' or self.Value == '':
                    return True
                else:
                    return False
        elif Ignore != "":
            IgnoredVariable = self.Variable.replace(Ignore, "")
            IgnoredValue = self.Value.replace(Ignore, "")
            if IgnoredVariable == "" or IgnoredValue == "":
                return True
            else:
                return False

        
    def NoneEmpty(self, Ignore=""):
        """Checks if None of them are empty."""
        if Ignore == "":
            try:
                if self.Variable.get() != '' and self.Value != '':
                    return True
                else:
                    return False
            except:
                if self.Variable != '' and self.Value != '':
                    return True
                else:
                    return False
        elif Ignore != "":
            IgnoredVariable = self.Variable.replace(Ignore, "")
            IgnoredValue = self.Value.replace(Ignore, "")
            if IgnoredVariable != "" and IgnoredValue != "":
                return True
            else:
                return False
            
class Server:
    """Create a online text server. No Code can be written after this until this closes."""
    def __init__(self, HOST:str="127.0.0.1", PORT:int=5050, Message:str="THE MESSAGE AT HOST:PORT/PATH", PATH:list[str]=[], ChangeMessage:list[str]=[], Commands:list=[]):
        """HOST should be a IPv4 address of a device. PORT can be any number from 0 to 65535.\n
        Link = http://HOST:PORT\n
        If the link is written normally then the Message given will be displayed.\n
        Updated Link = http://HOST:PORT/PATH\n
        If the Updated Link is written then the command given will run or the new message given will shown.\n
        Path and the Message or Commmand's index in the lists should be same.\n
        If you dont't want to add a command for th first one but for the second, write None in first.\n
        If you don't want to add any command just pass [] into the function\n
        And just same for the Change Message too.\n
        The Command should take a parameter in which the path enetered by user will be passed\n
        If it returns a Something then it will be considered as the new message.\n
        Else, there will be no message else nothing.\n
        Eg:\n
        def Command(Path):
            HOST = "localhost"
            return f"{HOST}:5555"
            
        Path = [\n
            "Updated",\n
            "Np"\n
        ]\n
        Commands = [\n
            None,\n
            Command\n
        ]\n
        ChangeMessage = [
            "None", 
            None
        ]
        server = Server("192.0.0.4", 5555, \n
                        Message, Path, \n
                        ChangeMessage, Commands)\n
        """
        
        global ServerUse
        ServerUse = [
            Message,
            PATH,
            ChangeMessage,
            Commands,
            str(HOST),
            int(PORT)
        ]
        self.ServerUse = ServerUse
    def start(self):
        self.Server = HTTPServer((self.ServerUse[4], self.ServerUse[5]), Handler)
        print(f"Server Running at http://{self.ServerUse[4]}:{self.ServerUse[5]}")
        print(f"Links: ")
        for i in self.link():
            print(f"    {i}")
        self.Server.serve_forever()
        
    def link(self):
        Links = []
        Yes = False
        for Path in self.ServerUse[1]:
            Links.append(f"http://{self.ServerUse[4]}:{self.ServerUse[5]}{Path}")
            Yes = True
        if not Yes: return [f"http://{self.ServerUse[4]}:{self.ServerUse[5]}/"]
        else: return Links
        
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global ServerUse
        Close = False
        self.send_response(200)
        Message = ServerUse[0]
        if self.path == "/":
            Message = ServerUse[0]
        else:
            Collected = []
            for UpdateMessage in ServerUse[2]:
                if UpdateMessage == None:
                    continue
                
                Collected.append(UpdateMessage)
                
            for UpdateCommand in ServerUse[3]:
                if UpdateCommand == None:
                    continue
                
                Collected.append(UpdateCommand)
                
            Index = 0
            for PATH in ServerUse[1]:
                try:
                    Something = Collected[Index](PATH)
                    if Something != None:
                        Message = Something
                    elif Something:
                        Close = True
                    else:
                        Message = ""
                except:
                    Message = Collected[Index]
                    
                    
                Index += 1
        
        if Close: self.send_header("Content-type", "text/html"); Message = "<html><body><h1>CLOSED</h1></body></html>"; print(Message)
        else: self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(Message, "utf-8"))
        if Close: ServerUse[6]()
            
        
def getText(Url):
    """Returns the Text got from url."""
    return get(Url).text

GetUrlText = getText

from subprocess import run

def termCmd(Command:str):
    Run = run(Command, shell=True, capture_output=True, text=True)
    return [Run, Run.stdout, Run.stderr]

def isString(String:str):
    if type(String) == type(""): return True
    else: return False
    
def isInteger(Integer:int):
    if type(Integer) == type(2): return True
    else: return False
    
def isFloat(Float:float):
    if type(Float) == type(0.2): return True
    else: return False
    
def isBoolean(Boolean:bool):
    if type(Boolean) == type(True): return True
    else: return False
    
def isTuple(Tuple:list):
    if type(Tuple) == type((0, 2)): return True
    else: return False