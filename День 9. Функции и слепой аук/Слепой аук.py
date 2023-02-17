from logo_for_project import logo_hamer
from replit import clear

print('Добро пожаловать в "Слепой аукцион"!')
print(logo_hamer)

name = input("Введите имя ")  # это будет ключ для словаря
price = int(input("Введите ставку: $"))  # это будет значение
new_guest = {}
new_guest[name] = price
flag = True


def guest(key, value):
    new_guest[key] = value


def who_winner(new_guest_1):
    a = 0
    winner = ''
    for win in new_guest_1:
        xxx = new_guest_1[win]
        if xxx > a:
            a = xxx
            winner = win
    print(f'Победил {winner} со ставкой ${a}')


while flag:
    question = input("Будут ещё участники продолжить 'да' или 'нет'?\n")
    if question == "да" or question == "Да" or question == "Yes" or question == "yes":
        clear()
        print('Прошу ввести данные следующего участника')
        name_1 = input("введите имя ")  # это будет ключ для словаря
        price1 = int(input("введите ставку: $"))  # это будет значение
        guest(name_1, price1)

    else:
        flag = False
        who_winner(new_guest)
