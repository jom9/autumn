import numpy as np
from Card import Card
from Hand import Hand
from Deck import Deck
from Stack import Stack
from Player import Player
defaultDeckSize= 60
defaultLifeTotal = 20
defaultStartHandSize = 7
maxHandSize =7
class BoardState():

    def __init__(self):
        self.player = Player('Player',defaultLifeTotal)
        self.op = Player('OP',defaultLifeTotal)
        self.stack= Stack()
        self.turnNum = 0


        self.turns = ['player','op']
        self.phases = [ 'Untap','Upkeep','Draw','PreMain','Begin Combat','Declare Attackers','Declare Blockers',
        'Combat Damage','End of Combat','Post Combat','End','Cleanup']
        self.currentPhase = phases[0]
        self.priority = ''
    def setDecks(self,filename):
        self.player.deck.getDeckList(filename)
        for i in range(defaultDeckSize):
            self.op.deck.mainboard.append( (Card(),-1) ) # the -1 is denote the number of copies is unknown

    def startMatch(self,startingPlayers):
        self.turns = startingPlayers
        self.priority = turns
        self.player.deck.shuffle()
        for i in range(defaultStartHandSize):

            self.player.hand.addCard(self.player.deck.draw())
            self.op.hand.addCard( self.op.deck.draw() )

    def nextPhase(self):
        self.manaPool = self.startmanaPool
        i=-1*len(self.phases)+1
        for phase in self.phases:
            if self.currentPhase= phase:
                break
            i+=1

        if self.currentPhase == 'Draw':
            if self.turns == 'player':
                self.player.hand.addCard(self.player.deck.draw())
            elif self.turns == 'op':
                self.op.hand.addCard(self.op.deck.draw())
        elif self.currentPhase =='Untap':
            if self.turns == 'player':
                for permanent in player.permanents:
                    permanent.untap()
            elif self.turns == 'op':
                for permanent in op.permanents:
                    permanent.untap()
        self.currentPhase = self.phases[i]
