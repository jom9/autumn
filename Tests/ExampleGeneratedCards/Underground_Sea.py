import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from RulesEngine.BoardState import BoardState
from RulesEngine.Card import Card

class Underground_Sea(Land):
    def __init__(self):
        cdname= 'Underground Sea'
        cdtext ='{T} : Add {U} or {B}."'
        mncost = ''
        clr = ''
        super().__init__(self,cdname,cdtext,mncost,clr)
    def addU(self,board):
        self.tap()
        board.manaPool[1]+=1
    def addB(self,board)
        self.tap()
        board.manaPool[2]+=1
