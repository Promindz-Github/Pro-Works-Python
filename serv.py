from http.server import BaseHTTPRequestHandler as Request, HTTPServer as starter
from os import remove, removedirs, makedirs

def Undo(File):
    if 'TEMP' in File or 'HOME' in File: 
        remove("TEMP\\Home.html")
    if 'TEMP' in File:
        removedirs('TEMP')
    if 'STATIC' in File:
        removedirs('STATIC')

def Redo():
    tryToDo(lambda: makedirs("TEMP")) 
    tryToDo(lambda: makedirs("STATIC"))
    open("TEMP\\Home.html", "w+").close()

undo = False
class server:
    Paths = []
    Commands = []
    def __init__(self, PORT:int=5000, HOST:str="127.0.0.1", **kwargs):
        global undo
        self.PORT = int(PORT)
        self.HOST = str(HOST)
        
    def to(self, PATH):
        def fnc(FUNC):
            def main():
                self.Paths.append(PATH)
                self.Commands.append(FUNC)
            main()
            return main
        return fnc
    
    def start(self, ask=True):
        Paths = self.Paths
        Commands = self.Commands
        
        class Handler(Request):
            def do_GET(self):
                for i in range(len(Paths)):
                    if Paths[i] == self.path:
                        self.send_response(200)
                        try: I = Commands[i](self.path)
                        except: I = Commands[i]()
                        if I == "/" and self.path == "":
                            self.path = "/"
                        try:
                            c = I[1]; del c
                            self.send_header("Content-Type", "text/plain")
                            self.end_headers()
                            self.wfile.write(bytes(I, "utf-8"))
                        except:
                            self.send_header("Content-Type", "text/html")
                            self.end_headers()
                            self.wfile.write(bytes(I[0], "utf-8"))
                        return
                self.send_response(404)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes("404", "utf-8"))
                return
        print(f"Running the server at http://{self.HOST}:{self.PORT}")
        if ask:
            i = input("Type something to not open the server: ")
            if i == "":
                from webbrowser import open
                open(f"http://{self.HOST}:{self.PORT}")
        start = starter((self.HOST, self.PORT), Handler).serve_forever()

def tryToDo(Func):
    try: Func(); return True
    except: return False

tryToDo(lambda: makedirs("TEMP")) 
tryToDo(lambda: makedirs("STATIC"))

try: open("TEMP\\Home.html", "r").close()
except: open("TEMP\\Home.html", "w+").close()
def Temp(Name:str):
    if not Name.endswith(".html"):
        Name += ".html"
    return [open(f"TEMP\\{Name}", "r").read()]