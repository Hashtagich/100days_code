from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import shuffle, sample  # ааа = sample(list, 3),  shuffle(list)
# import pyperclip

FONT_NAME = ('TimesNewRoman', 10, 'bold')
NAME_FILE_PASSWORD = 'Пароли.txt'  # Путь и название файла куда будут сохранять все пароли логины и сайты

empty = ''
name_image = 'logo.png'
letter_up = ascii_uppercase  # Все заглавные буквы (A-Z) из модуля string. Тип - строка
letter_down = ascii_lowercase  # Все строчные буквы (a-z) из модуля string. Тип - строка
numbers = digits  # Все цифры (0-9) из модуля string. Тип - строка
simbols = punctuation  # Все символы из модуля string. Тип - строка


def generation_pass(num_letter_up=2, num_letter_down=5, num_digits=2, num_simbols=3):
    # Функция для генерации пароля и его отображения
    # Пароль из суммы рандомно составленных списков (Тип - список).
    easy_password = sample(letter_up, num_letter_up) + sample(letter_down, num_letter_down) + \
                    sample(numbers, num_digits) + sample(simbols, num_simbols)
    shuffle(easy_password)  # Перемешиваем элементы списка
    password = ''.join(easy_password)  # Переводим конечную версию пароля в строку для вывода
    text_password.delete(0, 'end')  # полностью очищает окошко пароля, 0 это начало строки
    text_password.insert(0, password)  # вводит сгенерированный пароль в окошко пароля
    # pyperclip.copy(password)  # Как только пароль будет сгенерирован он сразу будет скопирован в буфер обмена


def add_password():  # Функция для сохранения добавления (сохранения) пароля в конечный файл формат txt
    web = text_website.get()
    email = text_email.get()
    password = text_password.get()
    string = f'{web} | {email} | {password}\n'

    if web == empty or email == empty or password == empty:  # Проверка на не заполненные поля
        messagebox.showinfo(title='Внимание!', message=f'Одно из полей не заполнено. Все поля должны быть заполнены')

    else:  # Уточнение на корректность заполнения полей
        is_ok = messagebox.askokcancel(title=web, message=f'Введены следующие данные: \n\nЭл.почта/Никнейм:{email} '
                                                          f'\nПароль: {password} \n\nCохранить данные?')
        if is_ok:
            with open(NAME_FILE_PASSWORD, 'a', encoding='utf-8') as file:
                file.write(string)
            # После сохранения все поля автоматом очищаются
            text_website.delete(0, 'end')
            text_email.delete(0, 'end')
            text_password.delete(0, 'end')


window = Tk()  # Рабочая область
window.title('Менеджер паролей')  # Название
window.config(padx=20, pady=20)  # Устанавливаем отступ от границ

canvas = Canvas(width=400, height=240)  # Холст для заливки и наложения изображений
my_pass_img = PhotoImage(file=name_image)
canvas.create_image(160, 120, image=my_pass_img)
canvas.grid(row=1, column=1)

# Ярлыки
lab_website = Label(text='Ссылка на сайт:', font=FONT_NAME)  # Ярлык вебсайта
lab_website.grid(row=2, column=0, sticky='w')
lab_website.config(padx=0, pady=5)

lab_email = Label(text='Эл.почта/Никнейм:', font=FONT_NAME)  # Ярлык никнейм или почта
lab_email.grid(row=3, column=0, sticky='w')

lab_password = Label(text='Пароль:', font=FONT_NAME)  # Ярлык никнейм или почта
lab_password.grid(row=4, column=0, sticky='w')
lab_password.config(padx=0, pady=5)

# Кнопки
gen_pass_butt = Button(text='Сгенерировать пароль', font=FONT_NAME, command=generation_pass)  # Кнопка генерации пароль
gen_pass_butt.grid(row=4, column=1, stick='e')

add_pass_butt = Button(text='Добавить', font=FONT_NAME, command=add_password)  # Добавления всей инфы в конечный файл
add_pass_butt.grid(row=5, column=1, columnspan=2)
add_pass_butt.config(padx=176, pady=0)

# Окошки ввода
text_website = Entry(width=70)  # Окно ввода сайта
text_website.grid(row=2, column=1, columnspan=2)
text_website.focus()

text_email = Entry(width=70)  # Окно ввода почты
text_email.grid(row=3, column=1, columnspan=2)

text_password = Entry(width=36)  # Окно ввода пароля
text_password.grid(row=4, column=1, stick='w')

window.mainloop()
