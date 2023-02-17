import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 54.849539449992086
MY_LONG = 38.24074745178223

my_email = 'xxxxx@mail.ru'  # Вводим свою почту
email = 'xxxxx@mail.ru'  # Вводим почту собеседника
password = 'xxxxx'  # Вводим пароль от почты
connect = 'smpt.mail.yahoo.com'  # Вводим протокол для соединения, у каждой почты он свой, указывается для своей
letters = 'Subject: МКС в небе!\n\nМКС в нашей зоне, посмотри на небо.'  # Письмо с темой и текстом


def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    if (MY_LAT + 5 >= latitude >= MY_LAT - 5) and (MY_LONG + 5 >= longitude >= MY_LONG - 5):
        return True


def is_night():
    parameters = {
        'lat': MY_LAT,
        'lig': MY_LONG,
        'formatted': 0,
    }
    response_sun = requests.get(url='http://api.sunrise-sunset.org/json', params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()
    sunrise = int(data_sun['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data_sun['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now()
    hour = time_now.hour

    if hour >= sunset or hour <= sunrise:
        return True


while True:  # Цикл бесконечен
    time.sleep(60)
    if is_iss_overhead() and is_night():

        with smtplib.SMTP(connect) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)  # Моя почта
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=letters
            )  # Отправка письма собеседнику собеседника
