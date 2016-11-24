from bicycles import *
from customers import *
from shops import *
from manufacturer import *


if __name__ == '__main__':
    theShop = BikeShop("Ye Old Bike Shoppe", 1.2)
    nathan = Customer("Nathan", 1000)
    heath = Customer("Heath", 500)
    eric = Customer("Eric", 200)
    manu = Manufacturer("Bike Builders Inc.", 1.05)
    #This will print theShop's inventory
    theShop.checkInventory()

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
    manu.checkProduction()
    theShop.stockInventory(manu)
    theShop.checkInventory()

