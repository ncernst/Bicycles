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
   
    
    
class Schwinn(Bicycle):
    model = "Schwinn"
    wheels = Firestone()
    frame = Carbonite()
        
    def __init__(self):
        super().__init__(Schwinn.model, Schwinn.wheels, Schwinn.frame)
        
        

class Huffy(Bicycle):
    model = "Huffy"
    wheels = Firestone()
    frame = FlexiFrame()
    
    def __init__(self):
        super().__init__(Huffy.model, Huffy.wheels, Huffy.frame)

    
class ToughStuff(Bicycle):
    model = "Tough Stuff"
    wheels = Michelin()
    frame = HardOnes()
    
    def __init__(self):
        super().__init__(ToughStuff.model, ToughStuff.wheels, ToughStuff.frame)

    
class Navigator(Bicycle):
    model = "Navigator"
    wheels = Michelin()
    frame = FlexiFrame()

    def __init__(self):
        super().__init__(Navigator.model, Navigator.wheels, Navigator.frame)   

    
class Cruiser(Bicycle):
    model = "Cruiser"
    wheels = Bridgewaters()
    frame = Carbonite()
    
    def __init__(self):
        super().__init__(Cruiser.model, Cruiser.wheels, Cruiser.frame)

    
class Lucky(Bicycle):
    model = "Lucky"
    wheels = Bridgewaters()
    frame = HardOnes()
    
    def __init__(self):
        super().__init__(Lucky.model, Lucky.wheels, Lucky.frame)
