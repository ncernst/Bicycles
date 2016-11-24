from bicycles import *
from customers import *
from shops import *


if __name__ == '__main__':
    theShop = BikeShop("Ye Old Bike Shoppe", 1.2)
    nathan = Customer("Nathan", 1000)
    heath = Customer("Heath", 500)
    eric = Customer("Eric", 200)
    #This will print theShop's inventory
    theShop.checkInventory()
    print("")
    #This will check theShop for bikes that each individual customer can afford
    #nathan.priceCheck(theShop)
    #heath.priceCheck(theShop)
    #eric.priceCheck(theShop)
    
    #This will have each of the individual customers buy a bike from theShop
    nathan.buyBike(theShop)
    heath.buyBike(theShop)
    eric.buyBike(theShop)

    
    #This will show the new inventory and profit total after purchases
    theShop.checkInventory()
