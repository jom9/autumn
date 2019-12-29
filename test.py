from Deck import Deck
from BoardState import BoardState


B = BoardState()
B.setDecks('testList.txt')

B.startMatch()
while True:
    userin= input('What to do?')
    if userin == 'draw':
        B.takeTurn()
    elif userin =='show hand':
        B.showHands()
    elif userin=='stop':
        print('done!')
        break
    else:
        print('unknown input')
        break
