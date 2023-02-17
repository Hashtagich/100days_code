from datetime import datetime as dt
import smtplib
from random import choice

NAME_FILE_TXT = 'quotes.txt'
TITLE_MASSAGE = 'Мотивационное письмо'  # Тема письма

my_email = 'xxxxx@mail.ru'  # Вводим свою почту
password = 'xxxxx'  # Вводим пароль от почты
email = 'xxxxx@mail.ru'  # Вводим почту куда отправлять письмо
connect = 'smpt.mail.yahoo.com'  # Вводим протокол для соединения, у каждой почты он свой,
# указывается с которой отправляем письмо

date_today = dt.now()  # Сегодняшняя дата
day_today = date_today.isoweekday()  # День недели (от 1 до 7)
hours_today = date_today.hour  # Час

if day_today == 1 and hours_today == 8:  # Отправлять письмо только в 8 утра понедельника
    with open(NAME_FILE_TXT, 'r', encoding='utf-8') as file:
        list_text = [i.rstrip('\n') for i in file.readlines()]

    random_text = choice(list_text)  # Рандомный текст для сообщения
    letters = f'Subject: {TITLE_MASSAGE}\n\n{random_text}.'  # Письмо с темой и текстом

    with smtplib.SMTP(connect) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)  # Моя почта
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=letters
        )  # Отправка письма самому себе
