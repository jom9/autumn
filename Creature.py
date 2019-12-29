
class Creature(Permanent):
    def __init__(self,cdname,cdtext,mncost,clr,tough,power,kywrds):
        super().__init__(self,cdname,cdtext,mncost,clr)
        self.toughness = tough
        self.power = power
        self.keywords =kywrds #list of abilities such as flying,vigilence etc
    
