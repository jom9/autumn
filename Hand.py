

class Hand():
    def __init__(self):
        self.cards = []
        self.revealedCards = []

    def showHand(self):
        print("Current Hand is:")
        for card in self.cards:
            print(card[0].cardName, end=' ')
        print('')
    def addCard(self,card):
        self.cards.append(card)
        return self.cards
    def removeCard(self,i):
        c = self.cards.pop(i)
        return c
