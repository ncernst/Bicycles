class Frames(object):
    material = None
    weight = None
    cost = None
    
    def returnWeight(self):
        return self.weight
        
    def returnCost(self):
        return self.cost
    
class Carbonite(Frames):
    material = "Carbon"
    weight = 40
    cost = 600.00
    
class FlexiFrame(Frames):
    material = "Aluminum"
    weight = 34
    cost = 350.00
    
class HardOnes(Frames):
    material = "Steel"
    weight = 52
    cost = 100.00