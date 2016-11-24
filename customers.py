import sys
from shops import *

class Customer(object):
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        
    def buyBike(self, shop):
        cost = shop.sellBike(self)
        self.cash -= cost
        print("{}".format(self.name) + " has $%.2f left in their bike fund." %self.cash)
    
    def priceCheck(self, shop):
        shop.checkInventory(self)
    
    