import random
print('Добро пожаловать в игру "Виселица!"')
print('Ваша задача по-буквенно угадать слово')
word_list = ['добыча', 'рулетка', 'артефакт', 'лама', 'кот', 'дождь', 'охота', 'асфальт']

lives = [''' ''', '''
 +---+
 |   |
 0   |
     |
     |
     |
=======
''', '''
 +---+
 |   |
 0   |
 |   |
     |
     |
=======
''', '''
 +---+
 |   |
 0   |
/|   |
     |
     |
=======
''', '''
 +---+
 |   |
 0   |
/|\  |
     |
     |
=======
''', '''
 +---+
 |   |
 0   |
/|\  |
/    |
     |
=======
''', '''
 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
=======
''']
word_from_list = random.choice(word_list)
letters = '_ ' * len(word_from_list)
letter_list = list(word_from_list)
answer_lisr = ['_ '] * len(word_from_list)
print('Загадано слово из ' + str(len(word_from_list)) + ' букв')
print(letters)
end = False
i = 0
q = 6
fail_letters = []
while not end:
    letter_gamer = input('Введите букву на русской раскладке\n').lower()
    for n in range(0, len(word_from_list)):
        if letter_gamer == answer_lisr[n]:
            print('Вы уже угадали данную букву')
        elif letter_gamer == letter_list[n]:
            answer_lisr[n] = letter_gamer
            print(answer_lisr)
    if letter_gamer not in letter_list and letter_gamer in fail_letters:
        fail_letters.append(letter_gamer)
        print(answer_lisr)
        print('Вы уже вводили эту букву. Этой буквы нет в данном слове')
    elif letter_gamer not in letter_list and letter_gamer not in fail_letters:
        fail_letters.append(letter_gamer)
        i += 1
        mm = q-i
        print(lives[i])
        print(answer_lisr)
        print('Нет. Осталось попыток ' + str(mm))
        if i == 6:
            end = True
            print(f'Было загадано слово {word_from_list}. Вы проиграли!')
    if '_ ' not in answer_lisr:
        end = True
        print(f'Верно это {word_from_list}. Вы победили!')
    
