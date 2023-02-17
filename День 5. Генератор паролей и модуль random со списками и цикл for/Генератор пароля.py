from random import choice, shuffle

print('Добро пожаловать в генератор паролей')
lst_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lst_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
lst_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = []
easy_password = ''
hard_password = ''

letters = int(input('Сколько букв хотите видеть в пароле?:\n'))
symbol = int(input('Сколько символов хотите видеть в пароле?:\n'))
number = int(input('Сколько цифр хотите видеть в пароле?:\n'))

for _ in range(letters):
    password.append(choice(lst_letters))

for _ in range(symbol):
    password.append(choice(lst_symbols))

for _ in range(number):
    password.append(choice(lst_numbers))

copy_password = password.copy()
shuffle(copy_password)

for i in password:
    easy_password += i

for j in copy_password:
    hard_password += j

print(f'Ваш легкий пароль следующий {easy_password}, a сложный {hard_password}')
