import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from RulesEngine.Card import Card
from PIL import Image,ImageTk

C = Card()

C.getCard('Underground Sea')

C.getCard('Underground Sea')
Image.open(C.getImage()).show()
print(C.toString())
C.getCard('Mana Leak')
C.getCard('Mana Leak')


print(C.toString())
