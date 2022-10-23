from importlib import resources

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
    },
}
profit = 0
Resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Checks if the resources is sufficient against the ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= Resources[item]:
            print(f"sorry there is no enough {item}")
            return False
    return True


def process_coins():
    """returns the total calculated from coin inserted """
    print("please insert coins: ")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successfull(money_received, drink_cost):
    """Returns True if payment received and False is not enough money"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("There is no enough money")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredient from the resources"""
    for item in order_ingredients:
        Resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True

while is_on:
    choice = input("What would you like to buy:'espresso','latte', 'cappuccino' ").lower()
    if choice == "off".upper():
        is_on = False
    elif choice == 'report':
        print(f"water: {Resources['water']}ml")
        print(f"milk: {Resources['milk']}ml")
        print(f"coffee: {Resources['coffee']}g")
        print(f"money:${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
