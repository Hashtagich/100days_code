logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphaber = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'] * 2
alphaber_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z'] * 2
print(logo)


def code_caesar(text_1, shift_1, direction_1):
    end = ""
    for word in text_1:
        if word in alphaber:
            position = alphaber.index(word)  # ищем в справочнике алфавит под какой цифрой-индексом
            # стоит первая вторая и другие буквы введённого слова
            if direction_1 == "encode":
                new_position = position + shift_1  # если инкод, то к полученным индексам прибавляем значение шага
                # сдвига
            elif direction == "decode":
                new_position = position - shift_1  # если декодер, то от полученным индексов отнимаем значение шага
                # сдвига
            end += alphaber[new_position]  # в пустое слово добавляем по букве из справочника алфавит индексы
            # букв уже новые
        elif word in alphaber_1:
            position = alphaber_1.index(word) # ищем в справочнике алфавит под какой цифрой-индексом стоит первая
            # вторая и другие буквы введённого слова
            if direction_1 == "encode":
                new_position = position + shift_1  # если инкод, то к полученным индексам прибавляем значение
                # шага сдвига
            elif direction == "decode":
                new_position = position - shift_1  # если декодер, то от полученным индексов отнимаем значение
                # шага сдвига
            end += alphaber_1[new_position]  # в пустое слово добавляем по букве из справочника алфавит индексы
            # букв уже новые
        else:
            end += word
    print(end)
    print(f'The {direction_1}d text is {end}')  # результат декода или инкода это "end"


question = "yes"

while question == "да" or question == "Да" or question == "Yes" or question == "yes":
    direction = input('Нажми "encode" чтобы инкодить, нажми "decode" чтобы декодить:\n')
    text = input('Введи фразу для шифровки:\n')
    shift = int(input('Введи шаг:\n'))
    shift = shift % 25
    code_caesar(text_1=text, shift_1=shift, direction_1=direction)
    question = input("Желаете продолжить 'да' или 'нет'?\n")
    if question == "нет" or question == "Нет" or question == "No" or question == "no":
        print("Goodbye!")
