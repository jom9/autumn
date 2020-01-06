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
        self.startmanaPool = [0,0,0,0,0,0]
        self.manaPool = self.startmanaPool# mana currently in the mana pool in wubrg wingding order

        self.stormCount = 0 #number of spells played this turn
        self.playersHand = Hand()
        self.opponentsHand = Hand()
        self.playersDeck = Deck()
        self.opponentsDeck = Deck()
        self.cardsInDeck = defaultDeckSize

        self.playersGraveyard =[]
        self.opponentsGraveyard = []

        self.playersExile = []
        self.opponentsExile = []

        self.playerLifeTotal = defaultLifeTotal
        self.opponetsLifeTotal = defaultLifeTotal

        self.stack= Stack()
        self.turnNum = 0

        self.playersLands = []
        self.playersCreatures = []

        self.opponentsLands = []
        self.opponentsCreatures = []
        self.turns = ['player','op']
        self.phases = [ 'Untap','Upkeep','Draw','PreMain','Begin Combat','Declare Attackers','Declare Blockers',
        'Combat Damage','End of Combat','Post Combat','End','Cleanup']
        self.currentPhase = phases[0]
        self.priority = ''
    def setDecks(self,filename):
        self.playersDeck.getDeckList(filename)
        for i in range(defaultDeckSize):
            self.opponentsDeck.mainboard.append( (Card(),-1) ) # the -1 is denote the number of copies is unknown

    def startMatch(self,startingPlayers):
        self.turns = startingPlayers
        self.priority = turns
        self.playersDeck.shuffle()
        for i in range(defaultStartHandSize):

            self.playersHand.addCard(self.playersDeck.draw())

            self.opponentsHand.addCard( self.opponentsDeck.draw() )
    def nextPhase(self):
        self.manaPool = self.startmanaPool
        i=-1*len(self.phases)+1
        for phase in self.phases:
            if self.currentPhase= phase:
                break
            i+=1

        if self.currentPhase == 'Draw':
            if self.turns == 'player':
                self.playersHand.addCard(self.playersDeck.draw())
            elif self.turns == 'op':
                self.opponentsHand.addCard(self.opponentsDeck.draw())
        elif self.currentPhase =='Untap':
            if self.turns == 'player':
                for land in self.opponentsLands:
                    land.untap()
                for creature in self.opponentsCreatures:
                    creature.untap()
            elif self.turns == 'op':
                for land in self.playersLands:
                    land.untap()
                for creature in self.playersCreatures:
                    creature.untap()
        self.currentPhase = self.phases[i]


    def showHands(self):
        print('Your Hand:')
        self.playersHand.showHand()
        print('OP Hand:')
        self.opponentsHand.showHand()
    def showManaPool(self):
        print("Mana Pool:",'w',self.manaPool[0],'u',self.manaPool[1],'b',self.manaPool[2],'r',self.manaPool[3],'g',self.manaPool[4],self.manaPool[5])
    def showCreatures(self):
        print('Your Creatues:')
        for creature in self.players
