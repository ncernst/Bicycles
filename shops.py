import sys
from bicycles import *
from customers import * 

class BikeShop(object):
    profit = 0.00
    modelTypes = {"Schwinn" : Schwinn(), "Huffy" : Huffy(), "ToughStuff" : ToughStuff(), "Navigator" : Navigator(), "Cruiser" : Cruiser(), "Lucky" : Lucky()}
    
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.inventory = {"Schwinn" : 10, "Huffy" : 10, "ToughStuff" : 10, "Navigator" : 10, "Cruiser" : 10, "Lucky" : 10}
        
    def stockInventory(self):
        for bike in self.inventory:
            print("You have {} {} bikes in your inventory. How many {} bikes would you like to add?".format(self.inventory[bike], bike, bike))
            add = input(">>> ")
            self.inventory[bike] += int(add)
    
    def checkInventory(self):
        for bike in self.inventory:
            if self.inventory[bike] > 0:
                print("{}: {}".format(bike, self.inventory[bike]))
    
    def soldOut(self):
        checker = True
        for bike in self.inventory:
            if self.inventory[bike] > 0:
                checker = False
                return
        if checker == True:
                print("Sorry, we're all sold out. Check back later")
                exit()

        
    def sellBike(self):
        self.soldOut()
        print("What type of bike are you looking for? Here's what we have.")
        self.checkInventory()
        choice = input(">>> ")
        for model in self.modelTypes:
            if model == choice:
                bike = self.modelTypes[model]
        
        wholesalePrice = bike.cost()
        retailPrice = wholesalePrice * self.margin
        self.profit += retailPrice - wholesalePrice
        print("Great, that'll be %.2f" %retailPrice)
        return retailPrice

        
