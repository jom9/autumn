

class Card():
    def __init__(self,*argv):
        if len(argv)== 0:
            self.cardName = 'unknown'
            self.cardText = 'unknown'
            self.manaCost = 'unknown'
            self.color = ' unknown'
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
        self.color = clr
        self.type = ty
    def toString(self):
        S = 'Card Name:'+self.cardName+',Card Text:'+self.cardText+',Mana Cost:'+self.manaCost.join(' ')
        return S
