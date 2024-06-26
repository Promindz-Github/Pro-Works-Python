from pyEasy.gui import *
import pyEasy as PE

def link():
    Textarea.deleteAllText()
    address = Address.get()
    if address.startswith("http"):
        OpenUrl(address)
    elif address.startswith("add:"):
        try:
            address = address.replace("add:", "")
            a = address.split(':')
            if a[0].startswith("0") or a[0].startswith("1") or a[0].startswith("2"):
                a[0] = idToPlace(a[0])
            if a[1].startswith("0") or a[1].startswith("1") or a[1].startswith("2"):
                a[1] = idToPlace(a[1])
            Textarea.insertAtLast(OpenFileRead(f"{a[0]}\\{a[1]}"))
        except:
            Textarea.insertAtLast(PE.surround(PE.Error('Not Found', 'address'), "\n\n\n\n", "\n\n\n\n", "\t\t\t\t", "                                                                               "))
            Textarea.colorWordBg("\t\t\t\t"+PE.Error('Not Found', 'address')+"                                                                               ", "#0000ff", True)
            Textarea.colorWordFg(PE.Error('Not Found', 'address'), "#00ffff", True)
    else:
        Textarea.insertAtLast(PE.surround(PE.Error('Not Found', 'address'), "\n\n\n\n", "\n\n\n\n", "\t\t\t\t", "                                                                               "))
        Textarea.colorWordBg("\t\t\t\t"+PE.Error('Not Found', 'address')+"                                                                               ", "#ff0000", True)
        Textarea.colorWordFg(PE.Error('Not Found', 'address'), "#00ffff", True)

def idToPlace(Id:str):
    Next = Low = Up = False
    Write = ""
    if not Id.startswith(":") and not Id.endswith(":"):
        return "ERROR"
    Id = Id[1:]
    Id = Id[:-1]
    for I in Id:
        if not Next:
            if int(I) == 0:
                Low = True
                Next = True
            if int(I) == 1:
                Up = True
                Next = True
            if int(I) == 2:
                Write += "\\"
        elif Next:
            if Up:
                Write += I.upper()
            elif Low:
                Write += I.lower()
            Next = Low = Up = False
    return Write

def placeToId(Place:str):
    id = ":"
    for I in Place:
        if I == "\\":
            id += "2"
        elif I == I.lower():
            id += f"0{I}"
        elif I == I.upper():
            id += f"1{I}"
    id += ":"
    return id

def main():
    global Win, Address, Textarea, full
    Win = Window('ProNetwork - NewTab')
    Win.setSize(600, 600)
    Address = Widgets.Entry(
        Win.get(), font=("Arial", 20, 'bold')
    )
    Address.insert('end', "add:Main:Intro")
    Address.pack(side="top", fill='x')
    Win.addShortcutKey(getShortcut(ENTER), link)
    Textarea = TextArea(PackInitially=True, PackFullWindow=True, bg='#1a1a1a', fg="#ffffff")
    Textarea.font(Font("comicsansms", 20, True))
    full = Win.usable(FullScreen)
    Win.addShortcutKey(getShortcut(FUNCTION11), full.Toggle)
    Win.finishCode()
    
if __name__ == '__main__':
    main()
else:
    __doc__ = f"{__name__} is importing the file for the browser"
