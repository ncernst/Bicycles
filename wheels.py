class Wheels(object):
    model = None
    weight = None
    cost = None
    
    def returnWeight(self):
        return self.weight
        
    def returnCost(self):
        return self.cost
    
class Firestone(Wheels):
    model = "Firestone"
    weight = 10
    cost = 80.00
    
class Michelin(Wheels):
    model = "Michelin"
    weight = 6
    cost = 175.00
    
class Bridgewaters(Wheels):
    model = "Bridgewaters"
    weight = 7
    cost = 50.00