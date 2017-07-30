'''
Created on 12.2.2016

@author: Joni
'''
import random
from random import shuffle
from card import Card    

class Deck(Card):
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """
    def __init__(self, card):
        self.cards = []
        for suitNum in range(len(Card.suitNames)):
            for faceNum in range(len(Card.faceNames)):
                self.cards.append(Card(suitNum, faceNum))    

    def new_Deck(self):
        """Creates a new deck."""        
        deck = []
        for suitNum in range(13):
            for faceNum in range(4):
                deck.append(Card(faceNum, suitNum))
        return deck
            


    

