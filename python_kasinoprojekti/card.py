'''
Created on 12.2.2016

@author: Joni
'''
class Card():
    """Represents a standard playing card.
    
    Attributes:
      suitNames: integer 0-3
      faceNames: integer 0-12
    """
    suitNames = ["c", "d", "h", "s"]
    faceNames = ["2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "J", "Q", "K", "A"]
    
    def __init__(self, suitNames=0, faceNames=0):
        self.suitNames = suitNames
        self.faceNames = faceNames    
    
    def getHandValue(self):
        """Returns hand value of a card"""
        if ((self.suitName() =="s") & (self.faceName() =="2")):
            return 15
        elif ((self.suitName() =="d") & (self.faceName() =="10")):
            return 16
        elif self.faceName() =="A":
            return 14
        elif self.faceName() =="K":
            return 13
        elif self.faceName() =="Q":
            return 12
        elif self.faceName() =="J":
            return 11
        else:
            return int(self.faceName())     
        
    def getTableValue(self):    
        """Returns table value of a card"""
        if self.faceName() =="A":
            return 1
        elif self.faceName() =="K":
            return 13
        elif self.faceName() =="Q":
            return 12
        elif self.faceName() =="J":
            return 11
        else:
            return int(self.faceName())
    
    def getPoints(self):
        """Returns points of a card"""
        if ((self.suitName() =="s") & (self.faceName() =="2")):
            return 1
        elif ((self.suitName() =="d") & (self.faceName() =="10")):
            return 2
        elif self.faceName() =="A":
            return 1
        else:
            return 0
        
    def faceName(self):
        """Returns face of a card"""
        return Card.faceNames[self.faceNames]
    
    def suitName(self):
        """Returns suit of a card"""
        return Card.suitNames[self.suitNames]

    def __str__(self):
        """Returns a human-readable string representation."""
        return "%s%s" % (self.faceName(), self.suitName())



