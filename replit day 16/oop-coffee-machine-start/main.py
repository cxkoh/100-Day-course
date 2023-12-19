from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()




is_done = False
while is_done == False:
    inquiry = input(f"Menu items are {menu.get_items()}, what would you like")
    if inquiry == "off":
        is_done = True
    elif inquiry == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(inquiry)
        if coffeemaker.is_resource_sufficient(drink) == True:
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)




