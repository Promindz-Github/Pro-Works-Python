"""If two Python Files use this library, their files get connected. If one of these files just gives command to close(None) then it will close others' all files too.
And If mistakenly using try : except:; They try to delete the file like data that is of other, it will be deleted."""

Texts = [None, None, None, None, None, None, None, None, None, None, None]
Text = ['upper', 'lower', '.', '/', ',', ':', ';', '\\', '*', '-', '+']
def idPattern(**kwargs):
    """Set different values for different chars. Parameters taking a value are:
    \"upper\", \"lower\", \"Point\", \"forward_slash\", \"comma\", \"colon\", \"semicolon\", \"backslash\", \"asterisk\", \"minus\", \"plus\""""
    Items = kwargs.items()
    Args = ["upper", "lower", "Point", "forward_slash", "comma", "colon", "semicolon", "backslash", "asterisk", "minus", "plus"]
    for I in Items:
        if I[0] in Args:
            Texts[Args.index(I[0])] = I[1]

def id(String:str, Pattern=Texts):
    """Get the id of a string with a idPattern()."""
    Write = ''
    for I in String:
        if I not in Text:
            if I == I.upper():
                Write += str(Pattern[0])
                Write += I
            if I == I.lower():
                Write += str(Pattern[1])
                Write += I
        else:
            try:
                Write += str(Pattern[Text.index(I)])
            except: Write += "..."
    return Write

Files = []
import os
try: os.makedirs("DataBase")
except:pass
try: 
    File = open("DataBase\\Files.txt", "r")
    Files = File.readlines()
    for I in Files:
        if I.endswith("\n"):
            Files[Files.index(I)] = I[:-1]
    File.close()
except: open("DataBase\\Files.txt", "w+").close()
def start(Name="DataBase"):
    """Create new data files. Same var names can be in different files."""
    if Texts[0] == None:
        idPattern(**{"upper":"0", "lower":"1", "Point":"2", "forward_slash":"3", "comma":"4", "colon":"5", "semicolon":"6", "backslash":"7", "asterisk":"8", "minus":"9", "plus":" "})
    open(f"DataBase\\{Name}.dat", "w+").write(f"{id("Manager")} =:= {__name__}")
    if Name not in Files:
        Files.append(Name)
    with open("DataBase\\Files.txt", "r") as Saved:
        Saved = Saved.readlines()
    for I in Saved:
        if I[-1] == "\n":
            Saved[Saved.index(I)] = I[:-1]
    for I in Files:
        if not I in Saved:
            with open("DataBase\\Files.txt", "a+") as F:
                F.write(f"{I}\n")


def check(Name="DataBase"):
    """Create a file if not created. Doesn't rerite any existing file."""
    if Texts[0] == None:
        idPattern(**{"upper":"0", "lower":"1", "Point":"2", "forward_slash":"3", "comma":"4", "colon":"5", "semicolon":"6", "backslash":"7", "asterisk":"8", "minus":"9", "plus":" "})
    try: open(f"DataBase\\{Name}.dat", "r").close()
    except: 
        C = open(f"DataBase\\{Name}.dat", "w+")
        C.write(f"{id("Manager")} =:= {__name__}")
        C.close()
    if Name not in Files:
        Files.append(Name)
    with open("DataBase\\Files.txt", "r") as Saved:
        Saved = Saved.readlines()
    for I in Saved:
        if I[-1] == "\n":
            Saved[Saved.index(I)] = I[:-1]
    for I in Files:
        if not I in Saved:
            with open("DataBase\\Files.txt", "a+") as F:
                F.write(f"{I}\n")
    
def close(Name="DataBase"):
    """Close everything and start from beginning if None is given. Any Other String Fill be taken as a FileName and will be deleted."""
    if Name != None:
        os.remove(f"DataBase\\{Name}.dat")
    elif Name == None:
        for I in Files:
            os.remove(f"DataBase\\{I}.dat")
            Files.pop(Files.index(I))
        os.remove("DataBase\\Files.txt")
        os.removedirs("DataBase")
    
def store(VarName:str, Value:str, Name="DataBase", id_value:bool=False, Pattern:list=Texts):
    global Texts
    """Store a Value in the DataBase. if id_value is True, then you will lock the value using id. Can't be unlocked without a pattern. Pattern is the pattern saved by idPattern.
    Needs a pattern. Take refernce from Nums and Text."""
    if not id_value: 
        C = open(f"DataBase\\{Name}.dat", "a")
        C.write(f"\n{id(VarName)} =:= {Value}")
        C.close()
    else:
        C = open(f"DataBase\\{Name}.dat", "a")
        C.write(f"\n{id(VarName)} =:= {id(Value, Pattern)}")
        C.close()
    
def get(VarName="Manager", Name="DataBase"):
    """Get values."""
    VarName = id(VarName)
    C = open(f"DataBase\\{Name}.dat", "r")
    for I in C.readlines():
        if VarName in I:
            I = I.split(" =:= ")
            if I[0] == VarName:
                return I[1]
    C.close()
            
def UnId(String:str, Pattern:list=Texts):
    Index = 1
    string = ""
    for I in String:
        if I in Pattern:
            if Text[Pattern.index(I)] not in ["upper", "lower"]:
                string += Text[Pattern.index(I)]
            elif Text[Pattern.index(I)] == "upper":
                string += String[Index].upper()
            elif Text[Pattern.index(I)] == "lower":
                string += String[Index].lower()
        Index += 1
    return string
            
def getUnlocked(VarName="Manager", Name="DataBase", Pattern:list=Texts):
    """Get values using a certain pattern. The pattern should be the same as when it was stored. If you interchange the first two values, The Case gets opposite."""
    VarName = id(VarName)
    C = open(f"DataBase\\{Name}.dat", "r")
    for I in C.readlines():
        if VarName in I:
            I = I.split(" =:= ")
            if I[0] == VarName:
                STRING = I[1]
    C.close()
    return UnId(STRING, Pattern)