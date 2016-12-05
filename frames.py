class Frames(object):
    material = None
    weight = None
    cost = None
    
    def returnWeight(self):
        return self.weight
        
    def returnCost(self):
        return self.cost

Carbonite = Frames("Carbon", 40, 600.00)  
FlexiFrame = Frames("Aluminum", 34, 350.00)  
HardOnes = Frames("Steel", 52, 100.00)  
