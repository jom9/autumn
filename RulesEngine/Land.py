
from Card import Card
from Permanent import Permanent
class Land(Permanent):
    def __init__(self,cdname,cdtext,mncost,clr,tough,power,kywrds):
        super().__init__(self,cdname,cdtext,mncost,clr)
