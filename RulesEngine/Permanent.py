
class Permanent(Card):
    def __init__(self,cdname,cdtext,mncost,clr):
        super().__init__(cdname,cdtext,mncost,clr)
        self.tapped  = False
    def tap(self):
        self.tapped = True
    def untap(self):
        self.tapped = False
    
