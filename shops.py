import sys
from bicycles import *
 

class BikeShop(object):
    profit = 0.00
    modelTypes = {"schwinn" : Schwinn(), "huffy" : Huffy(), "tough stuff" : ToughStuff(), "navigator" : Navigator(), "cruiser" : Cruiser(), "lucky" : Lucky()}
    
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.inventory = {"Schwinn" : 10, "Huffy" : 10, "Tough Stuff" : 10, "Navigator" : 10, "Cruiser" : 10, "Lucky" : 10}
        
    def stockInventory(self):
        for bike in self.inventory:
            print("You have {} {} bikes in your inventory. How many {} bikes would you like to add?"
            .format(self.inventory[bike], bike, bike))
            
            add = input(">>> ")
            self.inventory[bike] += int(add)
    
    def checkInventory(self, customer = None, sale = False):
        if customer != None and sale == False:
            print("{} can afford the following bikes:".format(customer.name))
        
        for bike in self.inventory:
            if self.inventory[bike] > 0:
                if customer == None:
                    print("{} -- In stock: {}, Wholesale: {}, Retail: {}"
                    .format(bike, self.inventory[bike], self.modelTypes[bike.lower()].cost(), self.modelTypes[bike.lower()].cost()*self.margin))
                else:
                    if customer.cash >= self.modelTypes[bike.lower()].cost()*self.margin:
                        print("{} -- In stock: {}, Cost: {} "
                        .format(bike, self.inventory[bike], self.modelTypes[bike.lower()].cost()*self.margin))
        
        if customer == None:
            print("Current profits for {} is $".format(self.name) + "%.2f" % self.profit)
    
    def soldOut(self):
        checker = True
        for bike in self.inventory:
            if self.inventory[bike] > 0:
                checker = False
        return checker


    def sellBike(self, customer):
        checker = self.soldOut()
        if checker == True:
            print("Sorry, we're all sold out. Check back later")
            return
        print("What type of bike are you looking for, {}? Here's what we have in your price range.".format(customer.name))
        self.checkInventory(customer, True)
        choice = input(">>> ")
        
        for stock in self.inventory:
            if stock.lower() == choice.lower():
                    bike = self.modelTypes[stock.lower()]
                    self.inventory[stock] -= 1
                    checker = True
                    break
                
        if checker == False:
            print("Sorry, we don't have those. Maybe try the shop down the block.")
            return 0
        

            
        wholesalePrice = bike.cost()
        retailPrice = wholesalePrice * self.margin
        print("Great, that'll be %.2f" %retailPrice)
        self.profit += (retailPrice - wholesalePrice)
        return retailPrice
