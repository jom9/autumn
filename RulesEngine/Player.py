from Hand import Hand
from Deck import Deck
class Player():
    def __init__(self,nme: str,lt: int):
        self.deck = Deck()
        self.hand = Hand()
        self.manaPool = [0,0,0,0,0,0] #wubrg
        self.name = nme
        self.lifetotal = lt
        self.graveyard = []
        self.exile = []
        self.permanents = []
    def draw(self):
        self.hand.addCard(self.deck.draw())
    def showHand(self):
        self.hand.showHand()
    def tutor(self,name):
        self.hand.addCard(self.deck.tutor(name))
