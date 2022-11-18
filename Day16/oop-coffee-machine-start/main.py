from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu_object = Menu()
# menu_item_object = MenuItem({'name': 'latte', 'water': 100, 'milk': 0, 'coffee': 16, 'cost': 2})
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

# print(money_machine.report())
# print(coffee_maker.report())

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})  :")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            # print('Make the drink and take payment')
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print('Insufficient resources')
