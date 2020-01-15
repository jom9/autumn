import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from RulesEngine.BoardState import BoardState
from RulesEngine.Card import Card


def main():
    passed = True
    try:
        B = BoardState()
        B.setDecks('testList.txt')
        B.startMatch('player')
        B.player.showHand()
        B.op.showHand()
        B.player.draw()
        B.player.showHand()
        for phase in B.phases:
            print(phase)
            if B.turns != 'player':
                ValueError('incorrect priority:player')
            B.nextPhase()

        for phase in B.phases:
            print(phase)
            if B.turns != 'op':
                ValueError('incorrect priority:op')
            B.nextPhase()

    except ValueError as err:
        print(err.args)
        passed = False
    if passed:
        print('All Test Passed')
    else:
        print('Test Failed')

main()
