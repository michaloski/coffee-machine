from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

x = Menu()
y = MoneyMachine()
z = CoffeeMaker()

def coffe_choice(coffee):
    if choice == coffee:
        item = x.find_drink(coffee)
        menu_item = MenuItem(item.name, item.ingredients["water"], item.ingredients["milk"], item.ingredients["coffee"], item.cost)
        if z.is_resource_sufficient(menu_item):
            if y.make_payment(1.5):
                z.make_coffee(menu_item)
            else:
                coffe_machine = False
        else:
            coffe_machine = False

coffe_machine = True
while coffe_machine:
    choice = input(f"What would you like? ({x.get_items()}): ")

    if choice == 'off':
        exit()
    if choice == 'report':
        z.report()
        y.report()
    if choice == 'espresso':
        coffe_choice(choice)
    elif choice == 'latte':
        coffe_choice(choice)
    elif choice == 'cappuccino':
        coffe_choice(choice)