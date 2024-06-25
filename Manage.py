from argparse import ArgumentParser
from subprocess import run
from pyEasy.autoControl import *
import os

def main():
    if Args.work == None:
        print("Work Completed !")
    elif Args.work == "":
        print("Work Completed !")
    elif Args.work == "Work":
        Input = input("What One: ")
        Args.work = Input
        main()
    elif Args.work.startswith("+"):
        Args.work = Args.work[1:]
        Args.work = Args.work.split("==")
        for I in range(0, int(Args.work[1])):
            print(Args.work[0])
    elif Args.work == "del>>file":
        Input = input("Path (Including Name): ")
        os.remove(Input)
    elif Args.work == "del>>dir":
        Input = input("Path (Including Name): ")
        try:
            os.removedirs(Input)
        except:
            print("Check if the directory is empty or not.")
    elif Args.work == "del>>folder":
        Input = input("Path (Including Name): ")
        try:
            os.removedirs(Input)
        except:
            print("Check if the directory is empty or not.")
    elif Args.work == "create>>file":
        Name = input("Name: ")
        open(Name, "w+").close()
    elif Args.work == "create>>folder":
        Name = input("Name: ")
        os.makedirs(Name)
    elif Args.work == "create>>dir":
        Name = input("Name: ")
        os.makedirs(Name)
    elif Args.work == "Python>>pyEasy.serv>>undo--STATIC:TEMP":
        os.remove("TEMP\\Home.html")
        os.removedirs("TEMP")
        os.removedirs("STATIC")
    elif Args.work == "Python>>pyEasy.serv>>redo--STATIC:TEMP":
        os.makedirs("TEMP")
        open("TEMP\\Home.html", "w+").close()
        os.makedirs("STATIC")
    elif Args.work == "Python>>py":
        presskey(P, Y, ENTER)
    elif Args.work.startswith("Python>>py"):
        work = Args.work.replace("Python>>py>")
        presskey(P, Y, ENTER)
        presskey(work)
    elif Args.work == "Python":
        print("Creating Project...")
        Name = input("Name: ")
        Extension = input("Console (Y/N): ")
        if Extension.lower().startswith("n"):
            Extension = ".pyw"
        else:
            Extension = ".py"
        FileName = Name + Extension
        FilePath = input("Path (Excluding FileName): ")
        if not FilePath.endswith("\\"):
            FilePath += "\\"
        File = FilePath + FileName
        Write = ""
        Imports = int(input("How many Imports: "))
        imports = []
        for I in range(1, Imports+1):
            Import = input(f"Import {I}: ")
            imports.append(Import)
        for I in imports:
            Write += f"import {I}\n"
        if imports.__len__() != 0:
            Write += "\n"
        Write = PythonFile(Write, imports, FilePath+FileName)
        with open(File, "w+") as File:
            File.write(Write)
    
    try:
        for I in range(0, Args.works):
            Args.work = input("--work: ")
            if Args.work == None:
                print("Work Completed !")
            elif Args.work == "":
                print("Work Completed !")
            elif Args.work == "Work":
                Input = input("What One: ")
                Args.work = Input
                main()
            elif Args.work.startswith("+"):
                Args.work = Args.work[1:]
                Args.work = Args.work.split("==")
                for I in range(0, int(Args.work[1])):
                    print(Args.work[0])
            elif Args.work == "del>>file":
                Input = input("Path (Including Name): ")
                os.remove(Input)
            elif Args.work == "del>>dir":
                Input = input("Path (Including Name): ")
                try:
                    os.removedirs(Input)
                except:
                    print("Check if the directory is empty or not.")
            elif Args.work == "del>>folder":
                Input = input("Path (Including Name): ")
                try:
                    os.removedirs(Input)
                except:
                    print("Check if the directory is empty or not.")
            elif Args.work == "create>>file":
                Name = input("Name: ")
                open(Name, "w+").close()
            elif Args.work == "create>>folder":
                Name = input("Name: ")
                os.makedirs(Name)
            elif Args.work == "create>>dir":
                Name = input("Name: ")
                os.makedirs(Name)
            elif Args.work == "Python>>pyEasy.serv>>undo--STATIC:TEMP":
                os.remove("TEMP\\Home.html")
                os.removedirs("TEMP")
                os.removedirs("STATIC")
            elif Args.work == "Python>>pyEasy.serv>>redo--STATIC:TEMP":
                os.makedirs("TEMP")
                open("TEMP\\Home.html", "w+").close()
                os.makedirs("STATIC")
            elif Args.work == "Python>>py":
                presskey(P, Y, ENTER)
            elif Args.work == "Python":
                print("Creating Project...")
                Name = input("Name: ")
                Extension = input("Console (Y/N): ")
                if Extension.lower().startswith("n"):
                    Extension = ".pyw"
                else:
                    Extension = ".py"
                FileName = Name + Extension
                FilePath = input("Path (Excluding FileName): ")
                if not FilePath.endswith("\\"):
                    FilePath += "\\"
                File = FilePath + FileName
                Write = ""
                Imports = int(input("How many Imports: "))
                imports = []
                for I in range(1, Imports+1):
                    Import = input(f"Import {I}: ")
                    imports.append(Import)
                for I in imports:
                    Write += f"import {I}\n"
                if imports.__len__() != 0:
                    Write += "\n"
                Write = PythonFile(Write, imports, FilePath+FileName)
                with open(File, "w+") as File:
                    File.write(Write)
    except:pass    
            
            
def PythonFile(Write:str, imports:list[str], Path):
    while True:
        Line = input("Line: ")
        if Line == "ursina.Ursina":
            Write += "Win = ursina.Ursina()\n"
        if Line == "ursina.run":
            Write += "Win.run()\n"
        if Line == "autoControl.press":
            Key = input("Key: ")
            Write += f"pyEasy.autoControl.presskey(pyEasy.autoControl.{Key.upper()})\n"
        if Line == "run-end":
            from subprocess import run
            Run = run(f"python -u {Path}", shell=True, capture_output=True, text=True)
            print("Output:\n", Run.stdout)
            print("Errors:\n", Run.stderr)
            break
        if Line == "save":
            with open(File, "w+") as File:
                File.write(Write)
        if Line == "run":
            from subprocess import run
            Run = run(f"python -u {Path}", shell=True, capture_output=True, text=True)
            print("Output:\n", Run.stdout)
            print("Errors:\n", Run.stderr)
        if Line == "end":
            break
    return Write

PSR = ArgumentParser()
PSR.add_argument("--work", "-w", help="Work To Do", required=False)
PSR.add_argument("--works", "-ws", help="Work To Do", required=False, type=int)
Args = PSR.parse_args()


if __name__ == '__main__':
    main()
