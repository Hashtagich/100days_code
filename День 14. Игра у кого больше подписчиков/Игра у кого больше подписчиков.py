from logo_for_project import logo_hader_lower, vs
from data_game import data
from random import choice
from replit import clear


def score_up():
    global score
    score += 1


def print_gamer(account):
    """Выводим информацию по игроку."""
    account_name = account['name']
    account_prof = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_prof}, from {account_country}'


def winner(gamer_1, gamer_2, letter):
    if gamer_1 > gamer_2:
        return letter == 'а' or letter == 'a'
    elif gamer_2 > gamer_1:
        return letter == 'б' or letter == 'b'


account_a = choice(data)
account_b = choice(data)
if account_a == account_b:
    account_b = choice(data)

score = 0
game_on = True
print(logo_hader_lower)
account_b = choice(data)

while game_on:
    account_a = account_b
    account_b = choice(data)
    if account_a == account_b:
        account_b = choice(data)

    print(f'Игрок А: {print_gamer(account_a)}')
    print(vs)
    print(f'Игрок Б: {print_gamer(account_b)}')
    guess = input('У кого больше подписчиков? А или Б:\n').lower()
    a_follow = account_a['follower_count']
    b_follow = account_b['follower_count']

    is_correct = winner(a_follow, b_follow, guess)

    clear()
    print(logo_hader_lower)

    if is_correct:
        score_up()
        print(f'Верно! Ваш текущий результат {score}.')
    else:
        print(f'Неверно! Финальный результат {score}.')
        game_on = False


# print(data[1]['name'])
# 'name': 'Instagram',
# 'follower_count': 346,
# 'description': 'Social media platform',
# 'country': 'United States'
