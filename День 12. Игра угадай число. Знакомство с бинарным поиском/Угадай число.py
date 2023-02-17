from random import randint

dict_difficulty = {'тяжело': 5, 'легко': 10}


def game():
    game_on = True
    print('Добро пожаловать в игру "Угадай слово"!\nВаша задача угадать число от 1 до 100.')
    random_number = randint(1, 100)
    choice_difficulty = input('Выберите сложность "легко" или "тяжело":\n')
    attempts = dict_difficulty[choice_difficulty]

    while game_on:
        if attempts == 0:
            print('Попытки закончились. Вы проиграли!')
            game_on = False
            break
        else:
            print(f'Кол-во попыток: {attempts}')
            guess_num = int(input('Введите число:\n'))
            if guess_num == random_number:
                print('Вы угадали!')
                game_on = False
                break
            elif guess_num < random_number:
                print('Недобор')
                attempts -= 1
            else:
                print('Перебор')
                attempts -= 1

    question = input('Ещё партию? "да", "нет":\n')
    if question == 'да':
        game()


game()
