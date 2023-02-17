import pandas
import smtplib
from random import choice
from datetime import datetime as dt

TITLE_MASSAGE = "С днём рождение!"
NAME_FILE_CSV = 'birthdays.csv'

my_email = 'xxxxx@mail.ru'  # Вводим свою почту
password = 'xxxxx'  # Вводим пароль от почты
connect = 'smpt.mail.yahoo.com'  # Вводим протокол для соединения, у каждой почты он свой,
# указывается с которой отправляем письмо
list_name_file = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

# Открываем csv файл и берём нужную информацию
data = pandas.read_csv(NAME_FILE_CSV)
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

# Сравниваем дни
date_now = dt.now()
month_day_now = (date_now.month, date_now.day)
hour = date_now.hour

if month_day_now in birthdays_dict and hour == 8:
    birthdays_person = birthdays_dict[month_day_now]
    name_friend = birthdays_person['name']  # Имя друга
    email_friend = birthdays_person['email']  # Почта куда отправлять письмо

# Создаём письмо
    random_name_letter = choice(list_name_file)  # Выбираем шаблон письма рандомно
    with open(random_name_letter, 'r', encoding='utf-8') as file:
        text = file.read()
        letter = text.replace('[NAME]', name_friend)  # Заменяем '[NAME]' на имя адресата
        final_letter = f'Subject: {TITLE_MASSAGE}\n\n{letter}'  # Письмо с темой и текстом
# Отправка письма
    with smtplib.SMTP(connect) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)  # Моя почта
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_friend,
            msg=final_letter
        )  # Отправка письма самому себе
