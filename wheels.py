class Wheels(object):
    model = None
    weight = None
    cost = None
    
    def returnWeight(self):
        return self.weight
        
    def returnCost(self):
        return self.cost

Firestone = Wheels("Firestone", 10, 80.00) 
Michelin = Wheels("Michelin", 6, 175.00) 
Bridgewaters = Wheels("Bridgewaters", 7, 50.00) 
