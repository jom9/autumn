from Card import Card
class Permanent(Card):
    def __init__(self,cdname,cdtext,mncost,clr,type):
        super().__init__(cdname,cdtext,mncost,clr,type)
        self.tapped  = False
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
