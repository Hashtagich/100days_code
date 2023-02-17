import smtplib

my_email = 'xxxxx@mail.ru'  # Вводим свою почту
email = 'xxxxx@mail.ru'  # Вводим почту собеседника
password = 'xxxxx'  # Вводим пароль от почты
connect = 'smpt.mail.yahoo.com'  # Вводим протокол для соединения, у каждой почты он свой, указывается для своей
letters = 'Subject: Тестовая тема письма\n\nТело письма, тесте-тест.'  # Письмо с темой и текстом

with smtplib.SMTP(connect) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)  # Моя почта
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email,
        msg=letters
    )  # Отправка письма собеседнику собеседника
    