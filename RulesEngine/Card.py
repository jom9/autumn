import requests
import time
import sys
from os import path
sys.path.append( path.dirname (path.dirname( path.abspath(__file__) ) ) )
class Card():
    def __init__(self,*argv):
        if len(argv)== 0:
            self.cardName = 'unknown'
            self.cardText = 'unknown'
            self.manaCost = 'unknown'
            self.colors = []
            self.type ='unknown'
            self.imagepath = path.dirname (path.dirname( path.abspath(__file__) ) )+'/imgs/cardback.jpeg'
        else:
            cdname = argv[0]
            cdtext = argv[1]
            mncost = argv[2]
            clr = argv[3]
            ty = argv[4]
            self.setValues(cdname,cdtext,mncost,clr,ty)
        self.abilities = []

    def setValues(self,cdname,cdtext,mncost,clr,ty):
        self.cardName = cdname
        self.cardText = cdtext
        self.manaCost = mncost
        self.colors = clr
        self.type = ty
    def toString(self):
        S = 'Card Name:'+self.cardName+',Card Text:'+self.cardText+',Mana Cost:'+self.manaCost
        return S
    def getImage(self):
        if self.cardName != 'unknown':
            p =  path.dirname( path.abspath(__file__) )
            self.imagepath = p+'/Cached Cards/Card Images/'+self.cardName+'.jpg'
        return self.imagepath
    def getCard(self,name):
        #print('Importing:'+name)
        if self.isCached(name):
            #print('Cached:',name)
            return True
        else:
            #print('Caching:',name)
            delay = .2
            time.sleep(delay)
            cachednamefile = open(path.dirname( path.abspath(__file__) ) +'/Cached Cards/CachedCards.txt','a'   )
            cachednamefile.write(name)
            cachednamefile.close()
            cache = open(path.dirname( path.abspath(__file__) ) +'/Cached Cards/CardInfo.txt','a')
            cache.write('////\n')
            self.cardName = name
            apiURL = 'https://api.scryfall.com/cards/named'
            p = {'exact':name}
            r = requests.get(url=apiURL,params=p)
            data = r.json()
            self.cardName =name[:-1]
            self.cardText = data['oracle_text'].replace(':',' :')
            self.cardText = self.cardText.replace('(','')
            self.cardText = self.cardText.replace(')','')
            self.type= data['type_line']
            self.manaCost = data['mana_cost']
            self.colors = []
            for color in data['colors']:
                self.colors+=[color]


            cache.write('$$$$'+self.cardText+'$$$$\n')
            cache.write('$$$$'+self.type+'$$$$\n')
            cache.write('$$$$'+self.manaCost+'$$$$\n')
            cache.write('$$$$'+'-'.join(self.colors)+'$$$$\n')

            cache.write('////\n')

            self.imageurl = data['image_uris']['small']

            r2 = requests.get(url=self.imageurl)
            with open(path.dirname( path.abspath(__file__) ) +'/Cached Cards/Card Images/'+name[:-1]+'.jpg','wb+') as f:
                f.write(r2.content)
                f.close()

            cache.close()
    def isCached(self,name):
        i = 0
        for card in open(path.dirname( path.abspath(__file__) ) +'/Cached Cards/CachedCards.txt','r').readlines():
            #print(name[-1],card[:-1],name[:] == card[:-1])
            if name[:-1] == card[:-1]:
                cachedCard = open(path.dirname( path.abspath(__file__) ) +'/Cached Cards/CardInfo.txt','r').read().split('////\n')[i]
                notskipped =0
                self.cardName=name[:-1]
                for line in cachedCard.split('$$$$'):
                    if line.isspace():
                        if notskipped==0:
                            self.cardText=line
                        elif notskipped==1:
                            self.type = line
                        elif notskipped==2:
                            self.manaCost = line
                        elif notskipped == 3:
                            self.colors = line.split('-')


                        notskipped+=1
                    else:
                        continue
                return True
            i+=1
        return False
