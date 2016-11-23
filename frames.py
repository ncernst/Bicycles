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
    cost = 95.00
    
class FlexiFrame(Frames):
    material = "Aluminum"
    weight = 34
    cost = 78.00
    
class HardOnes(Frames):
    material = "Steel"
    weight = 52
    cost = 87.00