
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
    def isLegal(self):
        return False
class Cost(Ability):
    def getTypes(self):
        pass
    def isPayable(self):
        pass

class ActivatedAbility(Ability):
    def __init__(self):
        self.costs = []
        self.effects = []
    def addCost(self,cost):
        self.costs.append(cost)
    def addEffect(self,effect):
        self.effects.apppend(effect)
    def getTypes(self):
        types = []
        for cost in self.costs:
            types+=[cost.getTypes()]
        return types
    def isLegal(self,inputs):
        for cost,input in zip(self.costs,inputs):
            if not cost.resolve(*input):
                return False
        return True
    def resolve(self,inputs):
        for cost,input in zip(self.costs,inputs):
            cost.resolve(*input)
        for effect in self.effects:
            effect.resolve()

class TriggerAbility(Ability):
    def __init__(self):
        self.conditions = []
        self.effects = []
class Tap(Cost):
    def getTypes(self):
        return [type( Permanent )]
    def isPayable(self,P : Permanent):
        if P.tapped == False:
            return True
        return False
    def resolve(self,P : Permanent):
        P.tap()
