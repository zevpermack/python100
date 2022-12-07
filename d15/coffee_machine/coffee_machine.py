from data import MENU, resources


def main(money):
    user_request = input(
        "What would you like? (espresso/latte/cappuccino/report/quit): "
    )

    if (
        user_request != "espresso"
        and user_request != "latte"
        and user_request != "cappuccino"
        and user_request != "report"
    ):
        return False, 0
    if user_request == "report":
        show_resources(money)
        return True, money
    else:
        print("Please insert coins.")
        if check_resources(user_request):
            money_inserted = ask_for_coins()
            if money_inserted < MENU[user_request]["cost"]:
                print("Sorry that's not enough money. Money refunded")
                return True, money
            else:
                subtract_resources(user_request)
                cost_of_drink = MENU[user_request]["cost"]
                change = money_inserted - cost_of_drink
                if change:
                    money += cost_of_drink
                serve_drink(change)
                return True, money

        else:
            return False, 0


def show_resources(money):
    print(
        f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}"
    )


def ask_for_coins():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


def check_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        return True


def serve_drink(change):
    print(f"Here is ${change} in change.\nHere is your latte ☕️")


def subtract_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] = (
            resources[ingredient] - MENU[drink]["ingredients"][ingredient]
        )


run_program = True
money = 0
while run_program:
    run_program, money = main(money)
