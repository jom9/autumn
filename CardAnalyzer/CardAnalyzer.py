import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from RulesEngine.BoardState import BoardState
from RulesEngine.Card import Card


#headerdemarker


def main(card):
    thisfile = open(sys.argv[0],'r')
    className = card.cardName.replace(' ','_')
    file = open(className+'.py','w')

    for line in thisfile.readlines():
        if line=='#headerdemarker':
            break
        file.write(line+'\r\n')

    file.write('class '+className+())
def test(cardName):
    card = Card()
    card.getCard(cardName)
    return main(card)


if len(sys.argv)>1:
    cardName = sys.argv[1]
    card = Card()
    card.getCard(cardName)
    main(card)
