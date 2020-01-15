from tkinter import font
import tkinter as tk
from PIL import Image,ImageTk
from RulesEngine.BoardState import BoardState

class MainMenu(tk.Frame):
    def __init__(self, master=None):
        self.matchnum = 0
        tk.Frame.__init__(self, master,bg='#5A733A')

        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()
    def createWidgets(self):

        bgcolor = '#5A733A'
        bgcolor2nd = '#C6C8B3'
        top=self.winfo_toplevel()
        self.bg = bgcolor
        top.rowconfigure(0, weight=2)
        top.title('Autumn')

        top.columnconfigure(0, weight=2)
        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=2)
        titleFont = font.Font(family = 'Helvetica',size=72,slant='italic')

        #self.title = tk.Label(self,justify=tk.LEFT,padx=0,bg = bgcolor, height =2, width = 400,text ='Autumn',font=titleFont,bd=6,relief=tk.GROOVE)
        #self.title.grid(column = 0, row = 0, columnspan = 4,sticky=tk.N+tk.S+tk.E+tk.W)

        textFont = font.Font(family = 'Helvetica',size=14,slant='roman')
        textDesc = ("This is a rules engine for the trading card game Magic The Gathering, created by Richard Garfield, owned by Wizards of The Coast.\n"
        "Created by Jonathan Martinez, Computer Science and Applied Physics student at NJIT\n"
        "Source at https://gitlab.com/jonathanma/autumn")
        self.textMess = tk.Message(self,bg = '#C5C5A1',font= textFont,width=1500,text=textDesc,bd=16, relief = tk.GROOVE)
        self.textMess.grid(column=0,columnspan =5,row=10,sticky=tk.N+tk.S+tk.E+tk.W)



        self.banner = tk.Canvas(self,bg=bgcolor,height=400,width=1500,bd=0)
        self.banner.grid(column=0,row=0,columnspan=6)
        self.pilImage = Image.open("imgs/banner.jpg").resize((400,400))
        self.Pimage = ImageTk.PhotoImage(self.pilImage)
        self.imagesprite = self.banner.create_image(1000,0,image=self.Pimage,state=tk.NORMAL,anchor=tk.NW)
        self.title = self.banner.create_text(0,0,width = 400,text ='Autumn',font=titleFont,anchor=tk.NW)



        self.dklistLabel =tk.Label(self,bg = '#C5C5A1',font= textFont,text="Enter the file path to your decklist:",width=100,bd =8 )
        self.dklistEntry = tk.Entry(self,font= textFont,width= 100)
        self.confirmButton = tk.Button(self,bg = '#B4E8B5', font = textFont,text= 'Enter',command=self.on_button,width=100,relief='raised')
        self.dklistLabel.grid(column=0,row=1,columnspan = 1,sticky=tk.N+tk.S+tk.E+tk.W)
        self.dklistEntry.grid(column=1, row=1,columnspan = 6,sticky=tk.N+tk.S+tk.E+tk.W)
        self.confirmButton.grid(column=1,row=2,columnspan = 6,sticky=tk.N+tk.S+tk.E+tk.W)
        self.errortxt = tk.StringVar()
        self.errorLabel = tk.Label(self,bg = bgcolor,font= textFont, textvariable=self.errortxt,fg='#ff0000')
        self.errorLabel.grid(row=2,column=0)
        self.startMatchButton =tk.Button(self,bg = '#B4E8B5', font = textFont ,text= 'Begin',command=self.start,width=100,relief='raised')
        self.startMatchButton.grid(column=1,row=3,sticky=tk.N+tk.S+tk.E+tk.W)
    def on_button(self):
        self.filename = self.dklistEntry.get()
        print(self.filename)

    def start(self):
        try:
            self.errorLabel.configure(fg="#00ff00")
            self.errortxt.set('Confirmed')
            print('Starting Match')
            newwin = tk.Toplevel(root)

            self.matchnum+=1

            newwin.title('Match:'+str(self.matchnum))
            B = BoardState()
            B.setDecks(self.filename)
            Match(newwin,B)
        except IOError:

            print('File Not Found')
            self.errorLabel.configure(fg="#ff0000")
            self.errortxt.set('File Not Found')
class Match(tk.Frame):
    def __init__(self,master,brd):
        self.board = brd
        self.board.startMatch('player')
        tk.Frame.__init__(self, master,bg='#000000')
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()
    def createWidgets(self):
        topm=self.winfo_toplevel()
        topm.rowconfigure(0, weight=1)
        topm.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.ophandCan = tk.Canvas(self,height=150,width=1000,bg='#C6C8B3')
        self.opboardCan = tk.Canvas(self,height=150,width=1000,bg='#5A733A')
        self.opboardCan.grid(row=1,rowspan=1,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
        self.ophandCan.grid(row=0,rowspan=1,column=0,sticky=tk.N+tk.S+tk.E+tk.W)

        self.playerboardCan = tk.Canvas(self,height=150,width=1000,bg='#5A733A')
        self.playerhandCan = tk.Canvas(self,height=150,width=1000,bg='#C6C8B3')
        self.playerboardCan.grid(row=2,rowspan=1,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
        self.playerhandCan.grid(row=3,rowspan=1,column=0,sticky=tk.N+tk.S+tk.E+tk.W)

        i=0
        '''
        card = self.board.player.hand.cards[0]
        print(card[0].getImage())
        #.resize((300,100)
        self.im =Image.open(card[0].getImage())
        self.im.show()
        self.Pimage = ImageTk.PhotoImage(self.im)
        self.cardImagesSprites.append(self.opboardCan.create_image(10,0,image=self.Pimage,state=tk.NORMAL,anchor=tk.NW))
        '''
        self.playercardImages = []
        self.playerPimages =[]
        self.playercardImagesSprites = []

        for card in self.board.player.hand.cards:

            print(card[0].getImage())
            self.playercardImages.append( Image.open(card[0].getImage()) )#.resize((150,100))
            #im.show()
            self.playerPimages.append(ImageTk.PhotoImage(self.playercardImages[-1])  )
            self.playercardImagesSprites.append(self.playerhandCan.create_image(i*100,0,image=self.playerPimages[-1],state=tk.NORMAL,anchor=tk.NW))
            i+=1

        self.opcardImages = []
        self.opPimages =[]
        self.opcardImagesSprites = []
        i=0
        for card in self.board.op.hand.cards:

            print(card[0].getImage())
            self.opcardImages.append( Image.open(card[0].getImage()).resize((146,204)))
            self.opPimages.append(ImageTk.PhotoImage(self.opcardImages[-1])  )
            self.opcardImagesSprites.append(self.ophandCan.create_image(i*100,0,image=self.opPimages[-1],state=tk.NORMAL,anchor=tk.NW))
            i+=1


root = tk.Tk()

app = MainMenu(master=root)

app.mainloop()
