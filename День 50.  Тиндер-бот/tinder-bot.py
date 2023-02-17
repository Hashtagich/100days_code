from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

drive_path = 'C:/Development/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(executable_path=drive_path, options=options)

# web_2 = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'
# driver.get(web_2)

web_page = 'https://tinder.com/app/recs'
google_autif_path ='https://accounts.google.com/v3/signin/identifier?dsh=S-1274297518%3A1668423561271934&continue=https%3A%2F%2Faccounts.google.com%2Fgsi%2Fselect%3Fclient_id%3D230402993429-g4nobau40t3v3j0tvqto4j8f35kil4hf.apps.googleusercontent.com%26ux_mode%3Dpopup%26ui_mode%3Dcard%26as%3D7fgPaZ1THetvmHtEkw36yw%26channel_id%3D55b023a186a859b2c59d6a345148b7bec754067df609025164bf0f3a87fc48d6%26origin%3Dhttps%3A%2F%2Ftinder.com&faa=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAtlWJOvwuiRiPebAcuhFsc9dxsfUFvo6k9LIOM1fb23sfPwSfGk0fFbuMlauvUC71c5tZLmcQ'
my_login = 'xxxxxxxxxxx'
text_massage = '''Добрый день! Спасибо за обратную связь! Если Вы читает данное сообщение, то бот успешно выполнил свою задачу. Прошу напишите любое сообщение, например, сообщение получено, чтобы я понял, что бот реально всё сделал до конца. P.S. Если тоже увлекаетесь языком Python и есть интерес в обмене опытом и наблюдениями можно связаться со мной в телеграмме https://t.me/BlackMarvel'''
driver.get(web_page)
sleep(60)

# Для аутентификации
start_path = '//*[@id="s-662773879"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]'
another_path = '//*[@id="s1903812341"]/main/div/div[1]/div/div/div[3]/span/button'
mobil_path = '//*[@id="s1903812341"]/main/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]'
login_path = '//*[@id="s1903812341"]/main/div/div[1]/div/div[2]/div/input'
next_path = '//*[@id="s1903812341"]/main/div/div[1]/div/button/div[2]/div[2]'
# Для лайков
like_next_path = '//*[@id="s-662773879"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span' # рабочая
empty_path = '//*[@id="s-1315570479"]'

massage_wind_path = '//*[@id="s-1953902166"]'  # окно сообщения если получилось совпадение
button_send_massage_path = '//*[@id="s-332402678"]/main/div/div[1]/div/div[3]/div[3]/form/button'  # кнопка отправить сообщение при совпадении

# Логинимся, фейсбука у меня нет, при мобильной реге выдало ошибку на сайте(не отправляет код),
# а при гугловской требуется супер-аутентификация с живым участием.
# Проще либо сохранить, залогиненую страницу либо заходить через куки, если сайт даст

# start_button = driver.find_element(By.XPATH, start_path)
# start_button.click()
# sleep(3)
#
# another_button = driver.find_element(By.XPATH, another_path)
# another_button.click()
# sleep(3)
#
# mobil_button = driver.find_element(By.XPATH, mobil_path)
# mobil_button.click()
# sleep(3)
#
# login = driver.find_element(By.XPATH, login_path)
# login.send_keys(my_login)
# sleep(3)
# next_button = driver.find_element(By.XPATH, next_path)
# next_button.click()

# Далее на телефон приходит код и его по-любому надо вводить т.е. тут как минимум нужен инпут с участием человека


# agree = driver.find_element(By.XPATH, '//*[@id="s1903812341"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
# print('прошел первое облако')

# agree = driver.find_element(By.XPATH, '//*[@id="s1903812341"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()  # работает, кликает на разрешения отслеживания местаположения
# print('yes 1 ')
# sleep(7)
# push = driver.find_element(By.XPATH, '//*[@id="s1903812341"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]').click()  # работает, жмет на кнопку отмены уведомлений
# print('yes 2 ')
# sleep(7)
# team = driver.find_element(By.XPATH, '//*[@id="s1903812341"]/main/div/div[2]/button/svg/path').click()  # не работаетб должна была отключать окно выбора цвета темы
# print('yes 3 ')
# sleep(7)

for i in range(25):
    try:
        # button_empty = driver.find_element(By.XPATH, empty_path) # кликает на пустое пространство слева, но рекламу это не убрало
        # button_empty.click()
        # print('я кликнул в пустоту')
        # sleep(7)
        # driver.refresh()
        # sleep(7)

        button_like_next = driver.find_element(By.XPATH, like_next_path)  # рабочая
        button_like_next.click()
        print('я кликнул')
        sleep(7)

    except ElementClickInterceptedException:
        try:
            match = driver.find_element(By.XPATH, massage_wind_path)  # рабочая
            match.clear()
            match.send_keys(text_massage)
            print('я написал сообщение')
            sleep(7)

        except NoSuchElementException:
            print('ошибки пошли пауза')
            sleep(10)


sleep(5)
driver.close()
driver.quit()


