from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return float(n1 * n2)


def divide(n1, n2):
    return n1 / n2


dict_symbol = {'+': add,
               '-': subtract,
               '*': mult,
               '/': divide}


def calculater():
    print(logo)
    first_number = float(input("Введите первое число:\n"))

    flag = True
    while flag:
        symbol = input('+\n-\n*\n/\nВыберете одну из вышеуказанных операций:\n')
        next_number = float(input("Введите следующее число:\n"))
        cal_fun = dict_symbol[symbol]
        result = cal_fun(first_number, next_number)
        print(f'{first_number} {symbol} {next_number} = {result}')
        question = input(
            f'Введите "далее" чтобы продолжить или "заново" чтобы запустить калькулятор заново:')
        if question == 'далее':
            first_number = result
        else:
            flag = False
            calculater()


calculater()
