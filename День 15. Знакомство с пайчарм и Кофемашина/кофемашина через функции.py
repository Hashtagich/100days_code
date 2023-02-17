MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def report():
    print(f'Water: {water}ml'
          f'\nMilk: {milk}ml'
          f'\nCoffee: {coffee}g'
          f'\nMoney: {money}$')


def drink():
    result = True
    if guess_water > water:
        print('Недостаточно кофе! Выберите другой напиток или пополните ресурсы.')
        result = False
    if guess_milk > milk:
        print('Недостаточно молока! Выберите другой напиток или пополните ресурсы.')
        result = False
    if guess_coffee > coffee:
        print('Недостаточно воды! Выберите другой напиток или пополните ресурсы.')
        result = False
    return result


def how_change():
    global money
    global change
    quarters = int(input('Сколько четвертаков положите?: '))
    dimes = int(input('Сколько десяток положите?: '))
    nickles = int(input('Сколько пятаков положите?: '))
    pennies = int(input('Сколько пенни положите?: '))
    total_money = 0.25 * quarters + 0.10 * dimes + 0.5 * nickles + 0.1 * pennies
    change = total_money - money_coffee


money = 0
change = 0
flag = True

while flag:
    guess = input("Какой напиток выберете? (cappuccino/espresso/latte):\n").lower()
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if guess == 'report':
        report()
    elif guess == 'exit':
        flag = False
        break
    else:
        guess_water = MENU[guess]['ingredients']["water"]
        guess_milk = MENU[guess]['ingredients']["milk"]
        guess_coffee = MENU[guess]['ingredients']["coffee"]
        money_coffee = MENU[guess]["cost"]
        word = drink()
        if word:
            how_change()
            if change >= 0:
                money += money_coffee
                print(f"Ваша сдача: {change}$")
                print(f"Ваш {guess} готов!")
                resources["water"] = water - guess_water
                resources["milk"] = milk - guess_milk
                resources["coffee"] = coffee - guess_coffee
            else:
                print('Вы внесли мало денег. Повторите заказ.')
        else:
            continue
