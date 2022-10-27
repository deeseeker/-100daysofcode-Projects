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

def check_resource(coffee_type):
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


#TO DO : we need to build a resource regulator
# TO DO: coin processor

def converter(quarters,dimes,nickles, pennies):
    """converts coins to dollars"""
    dollars = (0.25*quarters) + (0.10*dimes) + (0.05*nickles) + (0.01*pennies)
    return dollars
def check_transaction(coffee_type, payment):
    cost = MENU[coffee_type]['cost']
    if payment < cost:
        print("Sorry that's not enough money. Money refunded.")
    elif payment > cost:
        change = payment - cost
        print(f"Here is ${change} in change")
        print(f"Here is your {coffee_type}. Enjoy!")
    else:
        resources["Money"] = f"${cost}"
        print(f"Here is ${change} in change")
        print(f"Here is your {coffee_type}. Enjoy!")

def resource_manager(coffee_type):
    ingredients = MENU[coffee_type]['ingredients']
    if coffee_type != 'espresso':
        resources['water'] -= ingredients['water']
        resources["milk"] -= ingredients['milk']
        resources["coffee"] -= ingredients['coffee']
    else:
        resources['water'] -= ingredients['water']
        resources["coffee"] -= ingredients['coffee']


is_off = False
while not is_off:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == 'report':
        report()
        continue

    #process users drink:
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
    payment = converter(quarters,dimes,nickles,pennies)
    check_transaction(choice,payment)
    resource_manager(choice)
 


    if input('Turn off the Cofee Machine:').lower() == 'off':
        is_off = True
