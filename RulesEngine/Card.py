import requests
import time

class Card():
    def __init__(self,*argv):
        if len(argv)== 0:
            self.cardName = 'unknown'
            self.cardText = 'unknown'
            self.manaCost = 'unknown'
            self.colors = []
            self.type ='unknown'
        else:
            cdname = argv[0]
            cdtext = argv[1]
            mncost = argv[2]
            clr = argv[3]
            ty = argv[4]
            self.setValues(cdname,cdtext,mncost,clr,ty)

    def setValues(self,cdname,cdtext,mncost,clr,ty):
        self.cardName = cdname
        self.cardText = cdtext
        self.manaCost = mncost
        self.colors = clr
        self.type = ty
    def toString(self):
        S = 'Card Name:'+self.cardName+',Card Text:'+self.cardText+',Mana Cost:'+self.manaCost.join(' ')
        return S
    def getCard(self,name):
        delay = .2
        time.sleep(delay)
        self.cardName = name
        apiURL = 'https://api.scryfall.com/cards/named'
        p = {'exact':name}
        r = requests.get(url=apiURL,params=p)
        data = r.json()
        self.cardText = data['oracle_text'].replace(':',' :')
        self.cardText = self.cardText.replace('(','')
        self.cardText = self.cardText.replace(')','')
        self.type= data['type_line']
        self.manaCost = data['mana_cost']
        self.colors = []
        for color in data['colors']:
            self.colors+=[color]
