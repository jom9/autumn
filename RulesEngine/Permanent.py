from Card import Card
class Permanent(Card):
    def __init__(self,cdname,cdtext,mncost,clr,type,card=Card()):
        if card == Card():
            super().__init__(cdname,cdtext,mncost,clr,type)
        else:
            makePermanent(card)
        self.tapped  = False
    def makePermanent(self,card):
        self.cardName = card.cardName
        self.cardText = card.cardText
        self.manaCost = card.manaCost
        self.colors = card.colors
        self.type = card.type
    def tap(self):
        if self.tapped == False:
            self.tapped = True
            return True
        else:
            self.tapped = True
            return False
    def untap(self):
        if self.tapped == True:
            self.tapped = False
            return True
        else:
            self.tapped = False
            return False
