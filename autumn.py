from tkinter import font
import tkinter as tk
from PIL import Image,ImageTk
'''
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
'''
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
class MainMenu(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master,bg='#5A733A')

        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()
    def createWidgets(self):
        '''
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.quit = tk.Button(self, text='Quit', command=self.quit)
        self.quit.grid(row=0, column=0,
            sticky=tk.N+tk.S+tk.E+tk.W)
        '''
        bgcolor = '#5A733A'
        bgcolor2nd = '#C6C8B3'
        top=self.winfo_toplevel()
        self.bg = bgcolor
        top.rowconfigure(0, weight=2)
        top.title('Autumn')

        top.columnconfigure(0, weight=2)
        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=2)
        titleFont = font.Font(family = 'Helvetica',size=36,slant='italic')

        #self.title = tk.Label(self,justify=tk.LEFT,padx=0,bg = bgcolor, height =2, width = 400,text ='Autumn',font=titleFont,bd=6,relief=tk.GROOVE)
        #self.title.grid(column = 0, row = 0, columnspan = 4,sticky=tk.N+tk.S+tk.E+tk.W)

        textFont = font.Font(family = 'Helvetica',size=14,slant='roman')
        textDesc = ("This is a rules engine for the trading card game Magic The Gathering, created by Richard Garfield, owned by Wizards of The Coast.\n"
        "Created by Jonathan Martinez, Computer Science and Applied Physics student at NJIT\n"
        "Source at https://gitlab.com/jonathanma/autumn")
        self.textMess = tk.Message(self,bg = '#C5C5A1',font= textFont,width=1500,text=textDesc,bd=16, relief = tk.GROOVE)
        self.textMess.grid(column=0,columnspan =5,row=10,sticky=tk.N+tk.S+tk.E+tk.W)



        self.banner = tk.Canvas(self,bg=bgcolor,height=400,width=800,bd=0)
        self.banner.grid(column=0,row=0,columnspan=6)
        self.pilImage = Image.open("imgs/banner.jpg").resize((400,400))
        #pilImage.show()
        self.Pimage = ImageTk.PhotoImage(self.pilImage)
        self.imagesprite = self.banner.create_image(400,0,image=self.Pimage,state=tk.NORMAL,anchor=tk.NW)
        self.title = self.banner.create_text(0,0,width = 400,text ='Autumn',font=titleFont,anchor=tk.NW)
        #self.banner.grid(column=5,row=0,sticky=tk.N+tk.S+tk.E+tk.W)

        self.filename = tk.StringVar()
        self.dklistLabel =tk.Label(self,bg = '#C5C5A1',font= textFont,text="Enter the file path to your decklist:",width=100,bd =8 )
        self.dklistEntry = tk.Entry(self,font= textFont,width= 100)
        self.confirmButton = tk.Button(self,bg = '#B4E8B5', font = textFont,text= 'Enter',command=self.on_button,width=100,relief='raised')
        self.dklistLabel.grid(column=0,row=1,columnspan = 1,sticky=tk.N+tk.S+tk.E+tk.W)
        self.dklistEntry.grid(column=1, row=1,columnspan = 6,sticky=tk.N+tk.S+tk.E+tk.W)
        self.confirmButton.grid(column=1,row=2,columnspan = 6,sticky=tk.N+tk.S+tk.E+tk.W)

        self.startMatchButton =tk.Button(self,bg = '#B4E8B5', font = textFont,text= 'Begin',command=self.start,width=100,relief='raised')
        self.startMatchButton.grid(column=1,row=3,sticky=tk.N+tk.S+tk.E+tk.W)
    def on_button(self):

        print(self.dklistEntry.get())

    def start(self):
        print('Starting Match')
        pass
root = tk.Tk()

app = MainMenu(master=root)

app.mainloop()
