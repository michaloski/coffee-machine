MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def report_res():
    for key in resources:
        if key == 'water' or key == 'milk':
            print(f"{key.title()}: {resources[key]}ml")
        elif key == 'coffee':
            print(f"{key.title()}: {resources[key]}g")
        elif key == 'money':
            print(f"{key.title()}: ${resources[key]}")

def kind_of_coffe(coffee):
    # Coin process
    print("Please insert coins.")
    # quarters = $0.25
    quarters = int(input("How many quarters?: "))

    # dimes = $0.10
    dimes = int(input("How many dimes?: "))

    # nickles = $0.05
    nickles = int(input("How many nickles?: "))

    # pennies = $0.01
    pennies = int(input("How many pennies?: "))
    all_coins = round(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)
    if all_coins >= MENU[coffee]["cost"]:
        money_for_resources = MENU[coffee]["cost"]
        money_for_resources += resources['money']
        resources['money'] = money_for_resources
        all_coins -= MENU[coffee]["cost"]
        print(f"Here is ${round(all_coins, 2)} dollars in change")
    else:
        print("Sorry that's not enough money. Money refunded.")
        machine_work = False

    if not resources["water"] >= MENU[coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        machine_work = False
    else:
        menu_water = MENU[coffee]["ingredients"]["water"]
        resources["water"] -= menu_water

    if "milk" in MENU[coffee]["ingredients"]:
        if not resources["milk"] >= MENU[coffee]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            machine_work = False
        else:
            menu_milk = MENU[coffee]["ingredients"]["milk"]
            resources["milk"] -= menu_milk

    if not resources["coffee"] >= MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        machine_work = False
    else:
        menu_coffee = MENU[coffee]["ingredients"]["coffee"]
        resources["coffee"] -= menu_coffee



machine_work = True
while machine_work:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    #secret words
    if user_choice == 'off':
        exit()
    if user_choice == 'report':
        report_res()

    #kind of coffe
    if user_choice == 'latte':
        kind_of_coffe('latte')
    elif user_choice == 'espresso':
        kind_of_coffe('espresso')
    elif user_choice == 'cappuccino':
        kind_of_coffe('cappuccino')




