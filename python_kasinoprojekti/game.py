'''
Created on 12.2.2016

@author: Joni
'''
from random import shuffle
from player import *
from card import *
from deck import *
from table import *

class Game():
    """Represents a game."""       
    def gameplay(self):
        '''
        komento = (input("Aloitetaanko uusi peli (u) vai ladataanko tallennettu peli (l)? "))
        while (True):
            if (komento =="uusi"):
                break
            else:
                komento = (input("Kirjoita tekstikenttään joko u tai l. "))
        '''        
            
        pelaajaMaara = (input("Kuinka monta pelaajaa peliin osallistuu (2-4)? ")) 
        """User gives the amount of players"""
        pelaajaLista = []
        li = [0,0]
        voitto = False
        while (True):
            
            if (pelaajaMaara =="2"):
                pelaajaMaara = int(pelaajaMaara)
                while(True):
                    nimi1 = (input("Anna pelaajan 1 nimi. "))
                    """User gives the name of a player"""
                    if nimi1!="":
                        break
                pelaaja1 = Player(nimi1,0,li,0)
                """Creates a new player"""
                while(True):
                    nimi2 = (input("Anna pelaajan 2 nimi. "))
                    if ((nimi2!="") & (nimi1!=nimi2)):
                        break
                    else:
                        print("Nimi ei voi olla tyhjä, eikä sama kuin muilla pelaajilla")
                pelaaja2 = Player(nimi2,0,li,0)
                pelaajaLista.append(pelaaja1)
                pelaajaLista.append(pelaaja2)
                break
            elif (pelaajaMaara =="3"):
                pelaajaMaara = int(pelaajaMaara)
                while(True):
                    nimi1 = (input("Anna pelaajan 1 nimi. "))
                    if nimi1!="":
                        break
                pelaaja1 = Player(nimi1,0,li,0)
                while(True):
                    nimi2 = (input("Anna pelaajan 2 nimi. "))
                    if ((nimi2!="") & (nimi1!=nimi2)):
                        break
                    else:
                        print("Nimi ei voi olla tyhjä, eikä sama kuin muilla pelaajilla.")
                pelaaja2 = Player(nimi2,0,li,0)
                while(True):
                    nimi3 = (input("Anna pelaajan 3 nimi. "))
                    if ((nimi3!="") & (nimi3!=nimi2) & (nimi3!=nimi1)):
                        break
                    else:
                        print("Nimi ei voi olla tyhjä, eikä sama kuin muilla pelaajilla.")
                pelaaja3 = Player(nimi3,0,li,0)
                pelaajaLista.append(pelaaja1)
                pelaajaLista.append(pelaaja2)
                pelaajaLista.append(pelaaja3)
                break  
            elif (pelaajaMaara =="4"):
                pelaajaMaara = int(pelaajaMaara)
                while(True):
                    nimi1 = (input("Anna pelaajan 1 nimi. "))
                    if nimi1!="":
                        break
                pelaaja1 = Player(nimi1,0,li,0)
                while(True):
                    nimi2 = (input("Anna pelaajan 2 nimi. "))
                    if ((nimi2!="") & (nimi2!=nimi1)):
                        break
                    else:
                        print("Nimi ei voi olla tyhjä, eikä sama kuin muilla pelaajilla.")
                pelaaja2 = Player(nimi2,0,li,0)
                while(True):
                    nimi3 = (input("Anna pelaajan 3 nimi. "))
                    if ((nimi3!="") & (nimi3!=nimi2) & (nimi3!=nimi1)):
                        break
                    else:
                        print("Nimi ei voi olla tyhjä, eikä sama kuin muilla pelaajilla.")
                pelaaja3 = Player(nimi3,0,li,0)
                while(True):
                    nimi4 = (input("Anna pelaajan 4 nimi. "))
                    if ((nimi4!="") & (nimi4!=nimi2) & (nimi4!=nimi1) & (nimi4!=nimi3)) :
                        break
                    else:
                        print("Nimi ei voi olla tyhjä, eikä sama kuin muilla pelaajilla.")
                pelaaja4 = Player(nimi4,0,li,0)
                pelaajaLista.append(pelaaja1)
                pelaajaLista.append(pelaaja2)
                pelaajaLista.append(pelaaja3)
                pelaajaLista.append(pelaaja4)
                break
            else:       
                pelaajaMaara = (input("Kirjoita tekstikenttään pelaajien määrä 2, 3 tai 4. "))          
        
        print("Peli alkaa.")    
        deck = Deck.new_Deck(Deck)
        """Creates a new deck"""
        random.shuffle(deck)
        """First shuffle of the deck"""
        table = Table(0)
        """Creates a new table"""
        Pelaaja = pelaaja1
        while len(table.tableCards)<4:
            table.tableCards.append(deck.pop())
            """Deals 4 cards to the table"""
        if pelaajaMaara==2:
            while len(pelaaja1.holeCards)<4:
                pelaaja1.holeCards.append(deck.pop())
                """Deals 4 cards to the player"""
            while len(pelaaja2.holeCards)<4:
                pelaaja2.holeCards.append(deck.pop())
        elif pelaajaMaara==3:
            while len(pelaaja1.holeCards)<4:
                pelaaja1.holeCards.append(deck.pop())
            while len(pelaaja2.holeCards)<4:
                pelaaja2.holeCards.append(deck.pop())
            while len(pelaaja3.holeCards)<4:
                pelaaja3.holeCards.append(deck.pop())    
        elif pelaajaMaara==4:
            while len(pelaaja1.holeCards)<4:
                pelaaja1.holeCards.append(deck.pop())
            while len(pelaaja2.holeCards)<4:
                pelaaja2.holeCards.append(deck.pop())
            while len(pelaaja3.holeCards)<4:
                pelaaja3.holeCards.append(deck.pop())
            while len(pelaaja4.holeCards)<4:
                pelaaja4.holeCards.append(deck.pop())
        vuoro = 0
        
        while(True):
            Pelaaja = pelaajaLista[vuoro%pelaajaMaara]
            """Defines who's turn is it"""
            if (Pelaaja.nextTurn(table, deck)) == True:
                """Starts a turn"""
                last = Pelaaja
                """Last player who captured cards"""
            Pelaaja.countPoints()
            """Counts the players's points"""
            vuoro +=1
            """Add 1 to turn counnter"""
            if (((vuoro)%pelaajaMaara==0) & (vuoro!=0)):
                """Defines when round changes"""
                print("Seuraava kierros. Kierroksen aloittaja vaihtuu.")
                if len(deck)> 0:
                    print("Sekoitetaan pakka.")
                    random.shuffle(deck)
                    """shuffles the deck in the beginning of round"""
                i = 0
                while(i < 4):
                    if len(deck)> 0:
                        table.tableCards.append(deck.pop())
                        """Deals 4 cards from deck to table"""
                        i += 1
                    else:
                        break
                print("Pakassa kortteja jäljellä: " + str(len(deck)))
                """Prints how many cards in the deck"""
                if pelaajaMaara ==2:
                    print("Pelaajien pisteet: " + pelaaja1.name + " " + str(pelaaja1.points[0]) + " pistettä, " + pelaaja2.name + " " + str(pelaaja2.points[0]) + " pistettä")   
                    """Prints players's points"""
                    a = pelaajaLista[0]
                    b = pelaajaLista[1]
                    pelaajaLista = [b, a]
                    """Changes the beginner of the round"""
                if pelaajaMaara ==3:
                    print("Pelaajien pisteet: " + pelaaja1.name + " " + str(pelaaja1.points[0]) + " pistettä, " + pelaaja2.name + " " + str(pelaaja2.points[0]) + " pistettä, " + pelaaja3.name + " " + str(pelaaja3.points[0]) + " pistettä" )
                    a = pelaajaLista[0]
                    b = pelaajaLista[1]
                    c = pelaajaLista[2]
                    pelaajaLista = [b, c, a]
                if pelaajaMaara== 4:
                    print("Pelaajien pisteet: " + pelaaja1.name + " " + str(pelaaja1.points[0]) + " pistettä, " + pelaaja2.name + " " + str(pelaaja2.points[0]) + " pistettä, " + pelaaja3.name + " " + str(pelaaja3.points[0]) + " pistettä, " + pelaaja4.name + " " + str(pelaaja4.points[0]) + " pistettä")
                    a = pelaajaLista[0]
                    b = pelaajaLista[1]
                    c = pelaajaLista[2]
                    d = pelaajaLista[3]
                    pelaajaLista = [b, c, d, a]
            if ((Pelaaja.points[0]) >= 16):
                voitto = True
                """Player wins if 16 point is gained"""
                print("Onnea " + Pelaaja.name + "! Voitit pelin!")
                break
            
            if pelaajaMaara ==2:
                if ((len(deck)==0) & (len(pelaaja1.holeCards)==0) & (len(pelaaja2.holeCards)==0)):
                    if len(table.tableCards)> 0: 
                        """Game stops if all the hole cards are used""" 
                        print("Kortit loppuivat pelaajilta.")    
                        print(last.name + " saa loput pöytäkortit.")
                        while(len(table.tableCards) > 0):
                            last.holeCards.append(table.tableCards.pop()) 
                            """Adds the last table cards to player who captured cards last"""                   
                    break
            if pelaajaMaara ==3:
                if ((len(deck)==0) & (len(pelaaja1.holeCards)==0) & (len(pelaaja2.holeCards)==0) & (len(pelaaja3.holeCards)==0)):
                    if len(table.tableCards)> 0:     
                        print(last.name + " saa loput pöytäkortit.")
                        while (len(table.tableCards) > 0):
                            last.holeCards.append(table.tableCards.pop())                    
                    break  
            if pelaajaMaara ==4:
                if ((len(deck)==0) & (len(pelaaja1.holeCards)==0) & (len(pelaaja2.holeCards)==0) & (len(pelaaja3.holeCards)==0) & (len(pelaaja3.holeCards)==0)):
                    if len(table.tableCards)> 0:     
                        print(last.name + " saa loput pöytäkortit.")
                        while(len(table.tableCards) > 0):
                            last.holeCards.append(table.tableCards.pop())                    
                    break
                
        if voitto == False:
            if pelaajaMaara ==2:
                if ((pelaaja1.countCards()) >= (pelaaja2.countCards())):
                    pelaaja1.points[1] += 1
                if ((pelaaja1.countCards()) <= (pelaaja2.countCards())):
                    pelaaja2.points[1] += 1
                if ((pelaaja1.countSpades()) >= (pelaaja2.countSpades())):
                    pelaaja1.points[1] += 2  
                if ((pelaaja1.countSpades()) <= (pelaaja2.countSpades())):
                    pelaaja2.points[1] += 2
                """Adds points to the player who captured most cards and spades"""
                pelaaja1.countPoints()
                pelaaja2.countPoints()
                print("Pelaajien lopulliset pisteet: " + pelaaja1.name + " " + str(pelaaja1.points[0]) + " pistettä, " + pelaaja2.name + " " + str(pelaaja2.points[0]))       
                if ((pelaaja1.points[0]) > (pelaaja2.points[0])):
                    print("Voittaja on " + pelaaja1.name +"!!!")
                elif ((pelaaja1.points[0]) == (pelaaja2.points[0])):
                    print("Tasapeli!!!")
                else:
                    print("Voittaja on " + pelaaja2.name +"!!!")
                    
            if pelaajaMaara ==3:
                if (((pelaaja1.countCards()) >= (pelaaja2.countCards())) & ((pelaaja1.countCards()) >= (pelaaja3.countCards()))) :
                    pelaaja1.points[1] += 1
                if (((pelaaja2.countCards()) >= (pelaaja1.countCards())) & ((pelaaja2.countCards()) >= (pelaaja3.countCards()))) :
                    pelaaja2.points[1] += 1
                if (((pelaaja3.countCards()) >= (pelaaja1.countCards())) & ((pelaaja3.countCards()) >= (pelaaja2.countCards()))) :
                    pelaaja2.points[1] += 1
                if (((pelaaja1.countSpades()) >= (pelaaja2.countSpades())) & ((pelaaja1.countSpades()) >= (pelaaja3.countSpades()))) :
                    pelaaja1.points[2] += 1
                if (((pelaaja2.countSpades()) >= (pelaaja1.countSpades())) & ((pelaaja2.countSpades()) >= (pelaaja3.countSpades()))) :
                    pelaaja2.points[2] += 1
                if (((pelaaja3.countSpades()) >= (pelaaja1.countSpades())) & ((pelaaja3.countSpades()) >= (pelaaja2.countSpades()))) :
                    pelaaja3.points[2] += 1
                pelaaja1.countPoints()
                pelaaja2.countPoints()
                pelaaja3.countPoints()   
                print("Pelaajien pisteet: " + pelaaja1.name + " " + str(pelaaja1.points[0]) + " pistettä, " + pelaaja2.name + " " + str(pelaaja2.points[0]) + " pistettä, " + pelaaja3.name + " " + str(pelaaja3.points[0]) + " pistettä" ) 
                if (((pelaaja1.points[0]) > (pelaaja2.points[0])) & ((pelaaja1.points[0]) > (pelaaja3.points[0]))):
                    print("Voittaja on " + pelaaja1.name +"!!!")
                elif (((pelaaja2.points[0]) > (pelaaja1.points[0])) & ((pelaaja2.points[0]) > (pelaaja3.points[0]))):
                    print("Voittaja on " + pelaaja2.name +"!!!")
                elif (((pelaaja3.points[0]) > (pelaaja1.points[0])) & ((pelaaja3.points[0]) > (pelaaja2.points[0]))):
                    print("Voittaja on " + pelaaja3.name +"!!!")
                else:
                    print("Tasapeli!!!")
            
            if pelaajaMaara ==4:
                if (((pelaaja1.countCards()) >= (pelaaja2.countCards())) & ((pelaaja1.countCards()) >= (pelaaja3.countCards())) & ((pelaaja1.countCards()) >= (pelaaja4.countCards()))):
                    pelaaja1.points[1] += 1
                if (((pelaaja2.countCards()) >= (pelaaja1.countCards())) & ((pelaaja2.countCards()) >= (pelaaja3.countCards())) & ((pelaaja2.countCards()) >= (pelaaja4.countCards()))):
                    pelaaja2.points[1] += 1
                if (((pelaaja3.countCards()) >= (pelaaja1.countCards())) & ((pelaaja3.countCards()) >= (pelaaja2.countCards())) & ((pelaaja3.countCards()) >= (pelaaja4.countCards()))):
                    pelaaja1.points[1] += 1
                if (((pelaaja4.countCards()) >= (pelaaja1.countCards())) & ((pelaaja4.countCards()) >= (pelaaja2.countCards())) & ((pelaaja4.countCards()) >= (pelaaja3.countCards()))):
                    pelaaja1.points[1] += 1
                if (((pelaaja1.countSpades()) >= (pelaaja2.countSpades())) & ((pelaaja1.countSpades()) >= (pelaaja3.countSpades())) & ((pelaaja1.countSpades()) >= (pelaaja4.countSpades()))):
                    pelaaja1.points[1] += 2
                if (((pelaaja2.countSpades()) >= (pelaaja1.countSpades())) & ((pelaaja2.countSpades()) >= (pelaaja3.countSpades())) & ((pelaaja2.countSpades()) >= (pelaaja4.countSpades()))):
                    pelaaja2.points[1] += 2
                if (((pelaaja3.countSpades()) >= (pelaaja1.countSpades())) & ((pelaaja3.countSpades()) >= (pelaaja2.countSpades())) & ((pelaaja3.countSpades()) >= (pelaaja4.countSpades()))):
                    pelaaja1.points[1] += 2
                if (((pelaaja4.countSpades()) >= (pelaaja1.countSpades())) & ((pelaaja4.countSpades()) >= (pelaaja2.countSpades())) & ((pelaaja4.countSpades()) >= (pelaaja3.countSpades()))):
                    pelaaja1.points[1] += 2
                pelaaja1.countPoints()
                pelaaja2.countPoints()
                pelaaja3.countPoints()
                pelaaja4.countPoints()
                print("Pelaajien lopulliset pisteet: " + pelaaja1.name + " " + str(pelaaja1.points[0]) + " pistettä, " + pelaaja2.name + " " + str(pelaaja2.points[0]) + " pistettä, " + pelaaja3.name + " " + str(pelaaja3.points[0]) + " pistettä, " + pelaaja4.name + " " + str(pelaaja4.points[0]) + " pistettä")
                if (((pelaaja1.points[0]) > (pelaaja2.points[0])) & ((pelaaja1.points[0]) > (pelaaja3.points[0])) & ((pelaaja1.points[0]) > (pelaaja4.points[0]))):
                    print("Voittaja on " + pelaaja1.name +"!!!")
                elif (((pelaaja2.points[0]) > (pelaaja1.points[0])) & ((pelaaja2.points[0]) > (pelaaja3.points[0])) & ((pelaaja2.points[0]) > (pelaaja4.points[0]))):
                    print("Voittaja on " + pelaaja2.name +"!!!")
                elif (((pelaaja3.points[0]) > (pelaaja1.points[0])) & ((pelaaja3.points[0]) > (pelaaja2.points[0])) & ((pelaaja3.points[0]) > (pelaaja4.points[0]))):
                    print("Voittaja on " + pelaaja3.name +"!!!")
                elif (((pelaaja4.points[0]) > (pelaaja1.points[0])) & ((pelaaja4.points[0]) > (pelaaja2.points[0])) & ((pelaaja4.points[0]) > (pelaaja3.points[0]))):
                    print("Voittaja on " + pelaaja4.name +"!!!")
                else:
                    print("Tasapeli!!!")
            print("Peli päättyy!") 
        else: 
            print("Peli päättyy!") 
