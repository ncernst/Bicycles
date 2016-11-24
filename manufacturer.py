from bicycles import *
from shops import *
import random

class Manufacturer(object):
    bikeModels = ["Schwinn", "Huffy", "Tough Stuff", "Navigator", "Cruiser", "Lucky"]
    bikesMade = set({})
    profit = 0
    
    
    def addBikes(self, bikeList):
        i = len(self.bikesMade)
        if i < 3:
            picker = random.choice(self.bikeModels)
            self.bikesMade.add(picker)
            self.addBikes(self.bikesMade)
        else:
            #if None in self.bikesMade:
            #    self.bikesMade.remove(None)
            return
    
    def checkProduction(self):
        print("Here are the bikes we sell and their prices:")
        for bikes in self.bikesMade:
            bike = BikeShop.modelTypes[bikes.lower()]
            rawCost = bike.cost()
            wholesalePrice = rawCost * self.margin
            print("{}".format(bikes) + " -- Cost: $%.2f" %wholesalePrice)
        
    def wholesellBikes(self, model, count):
        value = BikeShop.modelTypes[model.lower()]
        rawCost = value.cost()
        rawCost = int(rawCost)
        totalPrice = (rawCost * self.margin) 
        self.profit += (totalPrice - rawCost)
        print("Great! {} {}".format(count, model) + "bikes, that'll be $%.2f" %totalPrice)
        return totalPrice
        

    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.addBikes(self.bikesMade)
        
         
