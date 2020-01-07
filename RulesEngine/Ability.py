
from BoardState import BoardState
from Permanent import Permanent
from Land import Land
class Ability():
    def __init__(self):
        pass
    def resolve(self):
        pass
    def undo(self):
        pass
class ActivatedAbility(Ability):
    def __init__(self):
        self.costs = []
        self.effects = []
    def addCost(self,cost):
        self.costs.append(cost)
    def addEffect(self,effect):
        self.effects.apppend(effect)
    def resolve(self):
        for cost in self.costs:
            cost.resolve()
        for effect in self.effects:
            effect.resolve

class TriggerAbility(Ability):
    def __init__(self):
        self.conditions = []
        self.effects = []
class Draw(Ability):
    def __init__(self,brd,tgt):
        super().__init__(self)
        self.board = brd
        self.target =tgt
    def resolve():
        if self.target=='player':
            self.board.playersHand.addCard(self.playersDeck.draw())
        elif target == 'op':
            self.board.opponentsHand.addCard(self.opponentsDeck.draw())
class addMana(Ability):
    def __init__(self,brd,clr):
        super().__init__(self)
        self.board = brd
        self.color =clr
    def resolve():
        manatypes = ['w','u','b','r','g','c']
        i= 0
        for manatype in manatypes:
            if self.color== manatype:
                self.board.manaPool[i]+=1
            i+=1

class tap(Ability):
    def __init__(self,target)
    def resolve(self,target):
        target.tap()
    def undo(self,target):
        target.untap()
