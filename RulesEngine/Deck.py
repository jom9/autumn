from Card import Card
import requests
import time
import random
class Deck():
    def __init__(self):
        self.mainboard= []
        self.sideboard = []

    def getDeckList(self,filename):
        #gets deck list from txt file
        file = open(filename,'r')
        mainBool = True

        for line in file.readlines():
            if line.isspace():
                mainBool = False

                continue
            numOfCpys = line[0]
            name = line[2:]
            c = Card()
            c.getCard(name)
            '''
            apiURL = 'https://api.scryfall.com/cards/named'
            p = {'exact':name}
            r = requests.get(url=apiURL,params=p)
            data = r.json()
            text = data['oracle_text']
            type = data['type_line']
            manaCost = data['mana_cost']
            colors = []
            for color in data['colors']:
                colors+=[color]
            '''

            for i in range( int(numOfCpys) ):
                card = (c,i)
                if mainBool:
                    self.mainboard.append(card)
                else:
                    self.sideboard.append(card)
            delay = .2
            time.sleep(delay)
    def printDeck(self):
        print(  'MainBoard:')
        for card in self.mainboard:
            print(card[0].toString())
        print('SideBoard:')
        for card in self.sideboard:
            print(card[0].toString())

    def shuffle(self):
        random.shuffle(self.mainboard)
        return self.mainboard
    def seeTop(self):
        return self.mainboard[0]
    def draw(self):
        return self.mainboard.pop(0)
    def tutor(self,name):
        i=0
        for card in self.mainboard:
            if name == card[0].cardName:
                self.mainboard.pop(i)
                break
            i+=1
        self.shuffle()
        return self.mainboard[i]
