'''
Created on 28.3.2016

@author: Joni
'''
from player import *
from card import *
from deck import *
from table import *


class Player:
    
    """Represents a player of the game.
    
    Attributes:
      name: name of the player
      holeCards: hand cards of the player
      points: points of the player
      capturedCards: captured cards of the player
    """

    def __init__(self, name, holeCards, points, capturedCards):
        self.name = name
        self.holeCards = []
        self.points = [0,0]
        self.capturedCards = []
        
    def countPoints(self): 
        """Counts the points of the player"""
        points = self.points[1]
        for card in self.capturedCards:
            points += card.getPoints()
        self.points[0] = points  
                   
    def countCards(self):
        """Counts the amount of cards captured"""
        return len(self.capturedCards)
    
    def countSpades(self):
        """Counts the amount of spades captured"""
        summ = 0
        for card in self.capturedCards:
            if card.suitName() =="s":
                summ += 1
        return summ    
    
    def nextTurn(self, table, deck):
        """Turn of a playear"""
        if len(self.holeCards)==0:
            print("Käsikorttisi ovat loppuneet. Vuoro annetaan seuraavalle.")
            return
        alku = (input("Valmistaudu vuoroosi " + self.name + ". Paina ENTER jatkaaksesi. "))
        while (True):
            if (alku ==""):
                break
            else:
                alku = (input("Paina ENTER jatkaaksesi."))
        
        while(True):
            print("On vuorosi " + self.name + ". Käsikorttisi ovat: ") 
            for card in self.holeCards:
                print(card) 
        
            print("Pöytäkortit ovat: ") 
            for card in table.tableCards:
                print(card) 
            turn = (input("Mitä teet? (h = hylkää, k = kaappaa, a = auta, s = säännöt) "))
            
            if turn == "a":
                self.help_()
            elif turn == "s":
                self.rules()
            elif turn == "h":
                self.discard(table, deck)
                k = False
                break
            elif turn == "k":
                if len(table.tableCards) == 0:
                    print("Et voi kaapata kortteja, koska pöytä on tyhjä!")
                    self.discard(table, deck)
                    break
                if self.capture(table, deck)==True:               
                    k = True
                    break
            
            else:
                print("Et antanut oikeaa komentoa.")
        return k        
        
    def capture(self, table, deck):
        """Captures cards from the table with a hole card""" 
        lista = []
        
        while(True):
            kortti1 = str(input("Anna käsikorteistasi kaappaava kortti.(esim. As) "))
            for card in self.holeCards:
                if kortti1 == str(card):          
                    lista.append(card)        
            if len(lista)==1:
                break        
        while (True):            
            while (True):
                k = (input("Anna kaapattavat kortit yksi kerrallaan.(esim. As) Paina ENTER lopettaaksesi. "))
                if (k ==""):
                    break
                for card in table.tableCards:                
                    if k == str(card):          
                        lista.append(card) 
            if len(lista)>=2:
                break        
        print("Koitetaan kaapata annetuilla käsi- ja pöytäkorteilla.")    
        
        koko = len(lista)
        sumTableValue = 0
        while(koko>1):           
            sumTableValue += lista[koko-1].getTableValue() 
            koko -=1
            
        koko1 = len(lista)
        koko2 = len(lista)    
        if sumTableValue % (lista[0].getHandValue())==0:
            for card in lista:
                print(card)
            while (koko1>=1):
                self.capturedCards.append(lista[koko1-1])
                koko1 -=1
            self.holeCards.remove(lista[0])
            while (koko2>=2):     
                table.tableCards.remove(lista[koko2-1])
                koko2 -=1
            while len(self.holeCards)<4:
                if len(deck)> 0:
                    self.holeCards.append(deck.pop())
                else:
                    break
            print("Kortit kaapattu onnistuneesti!")
            last = self
            if len(table.tableCards)==0:
                print("Mökki. Sait yhden pisteen.")
                self.points[1] += 1
            while (True):
                k = (input("Vuorosi päättyy " + self.name + ". Paina ENTER tyhjentääksesi ruudun. "))
                if (k ==""):
                    print("\n" * 200)
                    return True
            return True
        else:
            print("Virhe kaappauksessa. Käsikortin käsiarvo ei vastaa pöytäkortin pöytäarvoa.")   
            return False
      
    def discard(self, table, deck):
        """Discards a card from hole card to table card"""
        lista = []
        while(True):
            kortti1 = str(input("Anna käsikorteistasi pöydälle hylättävä kortti.(esim. As) "))
            for card in self.holeCards:
                if kortti1 == str(card):          
                    card1 = card 
                    lista.append(card1)
            if len(lista) ==1:
                break       
        table.tableCards.append(card1)
        self.holeCards.remove(card1)
        if len(deck)> 0:
            self.holeCards.append(deck.pop())
        while (True):
            k = (input("Vuorosi päättyy " + self.name + ". Paina ENTER tyhjentääksesi ruudun. "))
            if (k ==""):
                print("\n" * 200)
                break    

    def help_(self):
        print(" Omalla pelivuorollaan pelaajalla on vuorollaan käytettävänä neljä komentoa. Komennot \n ovat h, k, a ja s, jotka viittaavat seuraaviin sanoihin h = hylkää, k = kaappaa a = auta ja s \n = säännöt. Jos pelaaja valitsee h (h = hylkää), tulee hänen valita seuraavaksi \n käsikorteistaan pöydälle hylättävä kortti niin että ensiksi annetaan kortin arvo isolla \n kirjoitettuna ja kortin maa pienellä yhteen kirjoitettuna (esim. Ad tai 3h). Komennon k \n (k = kaappaa) jälkeen pelaajan tulee antaa yksi käsikortti edellä mainitussa muodossa, \n jolla hän voi kaapata pöytäkortteja. Pöytäkortit tulee antaa ohjelmalle yksittäin. Pelkän \n enterin painaminen annettujen korttien jälkeen tarkoittaa, että ei haluta enää syöttää \n kaapattavia kortteja.")
    def rules(self):
        print(" Pelissä kerätään pisteitä, jotka lasketaan aina jokaisen pelikierroksen lopussa. Peli \n jatkuu kunnes joku pelaajista saavuttaa 16 pistettä. Jokaisen pelikierroksen alussa pakka \n sekoitetaan ja jakaja jakaa jokaiselle pelaajalle 4 korttia, jotka eivät näy muille \n sekä 4 korttia pöytään, jotka näkyvät kaikille. Loput kortit jätetään pöydälle pinoon \n ylösalaisin. Jakajasta seuraava aloittaa pelaamisen. Seuraavalla pelikierroksella \n hän on jakaja. Omalla vuorollaan pelaaja voi kerrallaan käyttää jonkin kädessään olevista \n korteista: joko ottaa sillä pöydästä kortteja tai laittaa kortin pöytään. Jos pelaaja \n ei voi ottaa mitään pöydästä täytyy hänen laittaa jokin korteistaan pöytään. Jos pelaaja \n ottaa pöydästä kortteja hän kerää ne itselle pinoon. Pinon sisällöstä lasketaan korttien \n loputtua pisteet. Pöydässä olevien korttien määrä voi vaihdella vapaasti. Jos joku \n vaikkapa ottaa kaikki kortit, täytyy seuraavan laittaa jokin korteistaan tyhjään pöytään. \n Aina käytettyään kortin, pelaaja ottaa käteensä pakasta uuden, niin että kädessä on \n aina 4 korttia. Kun pöydällä oleva pakka loppuu, ei oteta enää lisää vaan pelataan \n niin kauan kuin kenelläkään on kortteja kädessä. Tällöin siis tietenkin alle 4 \n korttia on mahdollinen tilanne.")
        print()
        print(" Kortilla voi ottaa pöydästä yhden tai useampia samanarvoisia kortteja ja kortteja, joiden \n summa on yhtä suuri, kuin kortin jolla otetaan. Jos joku saa kerralla pöydästä kaikki \n kortit kerralla, hän saa ns. mökin, joka merkitään muistiin. Pelissä on muutama kortti, \n joiden arvo kädessä on arvokkaampi kuin pöydässä, Ässät: kädessä 14, pöydässä 1; \n Ruutu-10: kädessä 16, pöydässä 10; Pata-2: kädessä 15, pöydässä 2. Kun kaikilta loppuvat \n kädestä kortit, saa viimeksi pöydästä kortteja ottanut loput pöydässä olevat kortit. \n Tämän jälkeen lasketaan pisteet ja lisätään ne entisiin pisteisiin. Seuraavista asioista \n saa pisteitä: Jokaisesta mökistä saa yhden pisteen. Jokaisesta ässästä saa yhden pisteen. \n Eniten kortteja saanut saa yhden pisteen. Eniten patoja saanut saa 2 pistettä. \n Ruutu-10 kortin omistaja saa 2 pistettä sekä lisäksi Pata-2 kortin omistaja saa pisteen.")
        
        
