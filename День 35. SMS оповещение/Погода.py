import requests
import smtplib
import os

MY_LAT = 54.849539
MY_LONG = 38.240747

api = "https://api.openweathermap.org/data/2.5/weather"
api_key = "a3f064b73ec6247f3323af1ae37526f8"  # ключ рабочий
my_email = 'xxxxx@mail.ru'  # Вводим свою почту
email = 'xxxxx@mail.ru'  # Вводим почту собеседника
password = 'xxxxx'  # Вводим пароль от почты
connect = 'smpt.mail.yahoo.com'  # Вводим протокол для соединения, у каждой почты он свой, указывается для своей

weather_parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': api_key,
}

response_weather = requests.get(api, params=weather_parameters)
response_weather.raise_for_status()
data = response_weather.json()

id_weather = int(data['weather'][0]['id'])

if id_weather < 700:
    text = 'Возьми зонт!'
else:
    text = 'Всё в порядке!'

letters = f'Subject: Предупреждение о дожде!\n\n{text}'  # Письмо с темой и текстом

with smtplib.SMTP(connect) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)  # Моя почта
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email,
        msg=letters
    )  # Отправка письма собеседнику
