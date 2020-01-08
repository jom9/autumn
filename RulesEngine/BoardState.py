import numpy as np
import sys
from os import path
sys.path.append( path.dirname( path.abspath(__file__) )  )
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
        self.startingManaPool = [0,0,0,0,0,0]

        self.turns = ['player','op']
        self.phases = [ 'Untap','Upkeep','Draw','PreMain','Begin Combat','Declare Attackers','Declare Blockers',
        'Combat Damage','End of Combat','Post Combat','End','Cleanup']
        self.currentPhase = self.phases[0]
        self.priority = ''
    def setDecks(self,filename):
        self.player.deck.getDeckList(filename)
        for i in range(defaultDeckSize):
            self.op.deck.mainboard.append( (Card(),-1) ) # the -1 is denote the number of copies is unknown

    def startMatch(self,startingPlayer):
        self.turns = startingPlayer
        self.priority = self.turns
        self.player.deck.shuffle()
        for i in range(defaultStartHandSize):

            self.player.hand.addCard(self.player.deck.draw())
            self.op.hand.addCard( self.op.deck.draw() )

    def nextPhase(self):
        self.player.manaPool = self.startingManaPool
        self.op.manaPool = self.startingManaPool
        i=-1*len(self.phases)+1
        for phase in self.phases:
            if self.currentPhase== phase:
                break
            i+=1

        if self.currentPhase == 'Draw':
            if self.turns == 'player':
                self.player.hand.addCard(self.player.draw())
            elif self.turns == 'op':
                self.op.hand.addCard(self.op.draw())
        elif self.currentPhase =='Untap':
            if self.turns == 'player':
                for permanent in self.player.permanents:
                    permanent.untap()
            elif self.turns == 'op':
                for permanent in self.op.permanents:
                    permanent.untap()
        self.currentPhase = self.phases[i]
