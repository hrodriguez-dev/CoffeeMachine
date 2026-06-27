#/////////////////////////////////Coffee Machine Simulator/////////////////////////////////
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
#///////////// Coffee Machine Resources /////////////////
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
#//////////////////// Variables /////////////////////////
machine_ON = True

#/////////////////// Functions //////////////////////////
#This function check for water resources
def check_water(coffee_type):
    water = resources["water"]
    water_for_coffee = MENU[coffee_type]["ingredients"]["water"]
    if water >= water_for_coffee:
        return True
    else:
        return False

#This function update resources
def update_resources(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    if coffee_type != "espresso":
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    resources["money"] += MENU[coffee_type]["cost"]


#This function handle the money
def cachier(coffee_type):
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(f"Total Inserted: ${total:.2f} ")

    if total >= MENU[coffee_type]["cost"]:
        change = total - MENU[coffee_type]["cost"]
        print(f"Here is your change: ${change:.2f}")
        print(f"Here is your {coffee_type}. Enjoy!\n")
        #Update the water and money resources
        update_resources(coffee_type)
        return
    else:
        print("Sorry there is not enough money\n")
        return

#This function check for water and make the coffee
def coffee_machine(coffee_type):
    enough_water = check_water(coffee_type)
    if enough_water:
        print(f"Price: ${MENU[coffee_type]["cost"]:.2f}")
        cachier(coffee_type)
    else:
        print("Sorry there is not enough water\n")
        return


print("//////////////////// Coffee Machine ////////////////////")
while machine_ON:
    #Ask the costumer what coffee they want
    user_entry = input("What Coffee would you like? (espresso/latte/cappuccino): ").lower()

    if user_entry == "espresso":
        coffee_machine("espresso")
    elif user_entry == "latte":
        coffee_machine("latte")
    elif user_entry == "cappuccino":
        coffee_machine("cappuccino")
    elif user_entry == "off":
        machine_ON = False
        print("Coffee machine turning OFF")
    #Print the coffe machine resources
    elif user_entry == "report":
        print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: {resources["money"]}\n")
    #Print when user input an invalid input
    else:
        print("Please enter a valid input")
