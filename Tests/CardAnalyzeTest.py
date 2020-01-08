import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from RulesEngine.BoardState import BoardState
from RulesEngine.Ability import *
from RulesEngine.Permanent import Permanent
from RulesEngine.Player import Player
from RulesEngine.Land import Land
from CardAnalyzer.CardAnalyzer


def TestIsland(board):
    return False
def TestUndergroundSea(board)):
    return False
def TestScaldingTarn(board)):
    return False
def TestWastland(board)):
    return False
def TestBazer(board)):
    return False

def main():
    passed = True
    B = BoardState()
    B.setDecks('testList.txt')
    B.startMatch()
    try:
        if TestIsland(B):
            print("Passed Island Test")
        else:
            print("Failed Island Test")
            passed = False
    except:
        print("Failed Island Test,crash")
        passed = False
    try:
        if TestUndergroundSea(B):
            print('Passed Underground Sea Test')
        else:
            print('Failed Underground Sea Test')
            passed = False
    except:
        print('Failed Underground Sea Test,crash')
        passed = False
    try:
        if TestScaldingTarn(B):
            print('Passed Test Scalding Tarn Test')
        else:
            print('Failed Scalding Tarn Test')
            passed = False
    except:
        print('Failed Scalding Tarn Test,crash')
        passed = False
    try:
        if TestWastland(B):
            print('Passed Wasteland Test')
        else:
            print('Failed Wasteland Test')
            passed = False
    except:
        print('Failed Wasteland Test,crash')
        passed = False
    try:
        if TestBazer(B):
            print('Passed Bazer Test')
        else:
            print('Failed Bazer Test')
            passed = False
    except:
        print('Failed Bazer Test,crash')
        passed = False
    if passed:
        return "All tests are passed"
    else:
        return "Failed A Test"
print(main())
