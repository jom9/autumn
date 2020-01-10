import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from RulesEngine.Card import Card

C = Card()

C.getCard('Underground Sea')

C.getCard('Underground Sea')
print(C.toString())
C.getCard('Mana Leak')
C.getCard('Mana Leak')
print(C.toString())
