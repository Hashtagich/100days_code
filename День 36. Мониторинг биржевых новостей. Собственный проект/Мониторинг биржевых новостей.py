import requests
import smtplib
from datetime import datetime as dt, date

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key_alphavantage = 'GHLMQ5XGMJE4SW92'
api_key_news = '3c01dadf057846888c62b3c96f153af6'

my_email = 'xxxxx@mail.ru'  # Вводим свою почту
email = 'xxxxx@mail.ru'  # Вводим почту собеседника
password = 'xxxxx'  # Вводим пароль от почты
connect = 'smpt.mail.yahoo.com'  # Вводим протокол для соединения, у каждой почты он свой, указывается для своей


def data_yesterday_and_before(data_today):
    """Функция для получения вчерашней и позавчерашней даты в виде картежа"""
    year, month, day = data_today.year, data_today.month, data_today.day - 1
    day_before = data_today.day - 2
    d_yesterday = date(year, month, day)
    d_yesterday_before = date(year, month, day_before)
    return d_yesterday, d_yesterday_before


url_alphavantage = 'https://www.alphavantage.co/query'  # Запрашиваем информацию о стоимостях акций компании
parameters_alphavantage = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': api_key_alphavantage,
}

response_alphavantage = requests.get(url_alphavantage, params=parameters_alphavantage)
response_alphavantage.raise_for_status()
data_alphavantage = response_alphavantage.json()

data_now = dt.now()  # Узнаём сегодняшнюю дату и получаем стоимость на момент закрытия биржи на вчера и позавчера
data_yesterday_and_day_before = data_yesterday_and_before(data_now)
data_yesterday, data_yesterday_before = str(data_yesterday_and_day_before[0]), str(data_yesterday_and_day_before[1])

cost_yesterday_close = float(data_alphavantage['Time Series (Daily)'][data_yesterday]['4. close'])
cost_yesterday_before_close = float(data_alphavantage['Time Series (Daily)'][data_yesterday_before]['4. close'])
difference = cost_yesterday_close - cost_yesterday_before_close  # вычисляем разницу между стоимостями
diff_percent = (difference / cost_yesterday_close) * 100

title_message = f'Изменение на {round(diff_percent, 2)}%'

if abs(diff_percent) > 5:  # отправляем письмо с 3-мя последними новостями если разница больше 5%
    url_news = 'https://newsapi.org/v2/everything'
    parameters_news = {
        'q': COMPANY_NAME,
        'from': data_yesterday_before,
        'sortBy': 'publishedAt',
        'apiKey': api_key_news,
    }

    response_news = requests.get(url_news, params=parameters_news)
    response_news.raise_for_status()
    data_news = response_news.json()

    lst_three_news = [f"Название: {i['title']} кр.описание:{i['content']} подробнее:{i['url']}\n\n"
                      for i in data_news['articles'][:3]]
    text = ''.join(lst_three_news)
    letters = f'Subject: {title_message}\n\n{text}'  # Письмо с темой и текстом

    with smtplib.SMTP(connect) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)  # Моя почта
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=letters
        )  # Отправка письма собеседнику
