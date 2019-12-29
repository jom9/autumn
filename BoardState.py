import numpy as np
from Card import Card
from Hand import Hand
from Deck import Deck
from Stack import Stack
defaultDeckSize= 60
defaultLifeTotal = 20
defaultStartHandSize = 7
maxHandSize =7
class BoardState():

    def __init__(self):
        self.manaPool = [0,0,0,0,0,0]# mana currently in the mana pool in wubrg wingding order
        self.stormCount = 0 #number of spells played this turn
        self.playersHand = Hand()
        self.opponentsHand = Hand()
        self.playersDeck = Deck()
        self.opponentsDeck = Deck()
        self.cardsInDeck = defaultDeckSize

        self.playerLifeTotal = defaultLifeTotal
        self.opLifeTotal = defaultLifeTotal
        self.stack= Stack()
        self.turnNum = 0

        self.playersLands = []
        self.playersCreatures = []

        self.opLands = []
        self.opCreatures = []

        
    def setDecks(self,filename):
        self.playersDeck.getDeckList(filename)
        for i in range(defaultDeckSize):
            self.opponentsDeck.mainboard.append( (Card(),-1) ) # the -1 is denote the number of copies is unknown

    def startMatch(self):
        self.playersDeck.shuffle()
        for i in range(defaultStartHandSize):

            self.playersHand.addCard(self.playersDeck.draw())

            self.opponentsHand.addCard( self.opponentsDeck.draw() )
    def takeTurn(self):
        self.playersHand.addCard( self.playersDeck.draw() )
        self.turnNum+=1
    def showHands(self):
        print('Your Hand:')
        self.playersHand.showHand()
        print('OP Hand:')
        self.opponentsHand.showHand()
