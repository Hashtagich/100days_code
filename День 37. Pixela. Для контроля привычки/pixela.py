import requests
from datetime import datetime

USERNAME = 'hastagich'
TOKEN = 's65gf41a6gr4'
GRAPH_ID = 'textgraph1'

pixela_endpoint = "https://pixe.la/v1/users"


today = datetime.now()
date_now = today.strftime('%Y%m%d')
date_update = date_now
date_del = date_now

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
url_post_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
url_update_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_update}'
url_del_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_del}'


user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
graph_config = {
    'id': GRAPH_ID,
    'name': 'Coding',
    'unit': 'min',
    'type': 'float',
    'color': 'sora',
}
pixel_config = {
    'date': date_now,
    'quantity': '0.0',
}
pixel_update_config = {
    'quantity': '0.0',
}


def html():
    html_pixela = f'{graph_endpoint}/{GRAPH_ID}.html'
    print(html_pixela)


def create_account():
    """Создаём учётную запись, создать можно один раз, потом будет ошибка, что аккаунт уже создан"""
    global USERNAME, TOKEN, graph_endpoint, url_post_pixel, url_update_pixel, url_del_pixel
    USERNAME = input('Введите Ваш никнейм:\n')
    TOKEN = input('Введите Ваш уникальный код:\n')
    user_parameters['username'] = USERNAME
    user_parameters['token'] = TOKEN
    headers['X-USER-TOKEN'] = TOKEN
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    url_post_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    url_update_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_update}'
    url_del_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_del}'
    response = requests.post(url=pixela_endpoint, json=user_parameters)
    html()
    print(response.text)  # проверка на выполнение функции, можно не запускать


def create_table():
    """Создаём таблицу, если изменить 'GRAPH_ID' то это будет другая таблица"""
    global GRAPH_ID, url_post_pixel, url_update_pixel, url_del_pixel
    GRAPH_ID = input('Введите ID таблицы:\n')
    graph_config['id'] = GRAPH_ID
    graph_config['name'] = input('Введите название таблицы:\n')
    graph_config['unit'] = input('В каких единицах будет измеряться Ваш показатель?:\n')
    graph_config['type'] = input('int или float?:\n')
    graph_config['color'] = input('Выберите цвет:\n'
                                  '"sora"-синий\n'
                                  '"shibafu"-зеленый\n'
                                  '"momiji"-красный\n'
                                  '"ichou"-желтый\n'
                                  '"ajisai"-фиолетовый\n'
                                  '"kuro"-черный:\n')
    url_post_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    url_update_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_update}'
    url_del_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_del}'
    html()
    response_pixela = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response_pixela.text)  # проверяем на успешность ввода


def post_pixel():
    """Размещаем пиксель на графике"""
    pixel_config['quantity'] = input(f"Сколько {graph_config['unit']} за сегодня?")
    html()
    response_pixel = requests.post(url=url_post_pixel, json=pixel_config, headers=headers)
    print(response_pixel.text)


def update_pixel():
    """Изменяем параметр пикселя"""
    pixel_update_config['quantity'] = input(f"Сколько {graph_config['unit']} за сегодня?")
    html()
    response_pixel_update = requests.put(url=url_update_pixel, json=pixel_update_config, headers=headers)
    print(response_pixel_update.text)


def delete_pixel():
    """Удаление пикселя"""
    response_pixel_del = requests.delete(url=url_del_pixel, headers=headers)
    html()
    print(response_pixel_del.text)


dict_fun = {
        'Создать учётную запись': create_account,
        'Создать новую таблицу': create_table,
        'Добавить новый пиксель в действующую таблицу': post_pixel,
        'Обновить данные пикселя в действующей таблице': update_pixel,
        'Удалить пиксель из действующей таблицы': delete_pixel,
}


choice = "'Создать учётную запись'\n'Создать новую таблицу'\n'Добавить новый пиксель в действующую таблицу'\n" \
         "'Обновить данные пикселя в действующую таблицу'\n'Удалить пиксель'"

YES = ['yes', 'y', 'да', 'конечно', 'разумеется', '+']
NO = ['no', 'n', 'нет', 'не', '-']
prog_on = True

while prog_on:
    key = input(f'Выберите действие: {choice}:\n').lower()
    if key in choice:
        dict_fun[key]()
        true_again = input('Желаете продолжить?:\n').lower()
        if true_again in NO:
            print('Всего хорошего!')
            prog_on = False
    else:
        print('Ошибка ввода, перезапускаю!')
