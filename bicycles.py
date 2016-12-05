import sys
from wheels import *
from frames import *

class Bicycle(object):
    
    def __init__(self, model, wheels, frame):
        self.model = model
        self.wheels = wheels
        self.frame = frame

    def weight(self):
        wheelWeight = self.wheels.returnWeight()
        frameWeight = self.frame.returnWeight()
        totalWeight = wheelWeight + frameWeight
        return totalWeight 
    
    def cost(self):
        wheelCost = self.wheels.returnCost()
        frameCost = self.frame.returnCost()
        totalCost = wheelCost + frameCost
        return totalCost
        
Schwinn = Bicycle("Schwinn", Firestone, Carbonite)
Huffy = Bicycle("Huffy", Firestone, FlexiFrame)
ToughStuff = Bicycle("ToughStuff", Michelin, HardOnes)
Navigator = Bicycle("Navigator", Michelin, HardOnes)
Cruiser = Bicycle("Cruiser", Bridgewaters, Carbonite)
Lucky = Bicycle("Lucky", Bridgewaters, HardOnes)
