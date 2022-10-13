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
}

# def cal_cost(quarters,dimes,nickles,pennies):
#
# def c_cost():
#     coffee_cost = MENU[coffee_type]['ingredients']['cost']
# TODO 1: prompt users for input
# TODO 2: prompt users again when actions completed
# TO DO 3: print report
def report():
    print('water:', f"{resources['water']}ml")
    print('milk:', f"{resources['milk']}ml")
    print('coffee:', f"{resources['coffee']}g")

def check_resources(coffee_type):
    ingredients = MENU[coffee_type]['ingredients']
    if coffee_type != 'espresso':
        water = ingredients['water']
        milk = ingredients['milk']
        coffee = ingredients['coffee']
        if resources['water'] < water:
            print("Sorry, there is not enough water")
        elif resources['milk'] < milk:
            print("Sorry, there is not enough milk")
        elif resources['coffee'] < coffee:
            print("Sorry, there is not enough coffee")
    else:
        water = ingredients['water']
        coffee = ingredients['coffee']
        if resources['water'] < water:
            print("Sorry, there is not enough water")
        elif resources['coffee'] < coffee:
            print("Sorry, there is not enough coffee")




is_off = False
while not is_off:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == 'report':
        report()
        continue
    if choice == 'espresso':
        check_resource(choice)

    elif choice == 'latte':
        check_resource(choice)
    elif choice == 'cappuccino':
        check_resource(choice)
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    if input('Turn off the Cofee Machine:').lower() == 'off':
        is_off = True
