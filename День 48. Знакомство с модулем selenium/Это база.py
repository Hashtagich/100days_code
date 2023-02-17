from selenium import webdriver  # импортируем метод модуля
from selenium.webdriver.common.by import By  # импортируем метод By чтобы использовать в find_element
import time  # для задержки работы программы

drive_path = 'C:/Development/chromedriver'  # путь к драйверу для работы браузера с модулем
driver = webdriver.Chrome(executable_path=drive_path)  # После точки пишем браузер, естественно драйвер должен быть соответствующий

web_page = 'https://www.ozon.ru/product/kran-sharovyy-polipropilenovyy-vieir-25mm-komplekt-2sht-589749779' \
           '/?avtc=1&avte=2&avts=1668333624&sh=6OfCnxh_ZA'  # ссылка на сайт
name_obj = '//*[@id="layoutPage"]/div[1]/div[3]/div[1]/div/div[1]/div/ol/li[4]/a/span'  # адрес элемента для работы

driver.get(web_page)  # открываем страницу в Chrome

price = driver.find_element(By.XPATH, name_obj)  # с помощью By.XPATH или любого подходящего
# (By.NAME,
# By.CSS_SELECTOR,
# By.CLASS_NAME и т.д.) находим нужную нам кнопку ссылку или текст и присваиваем её в переменную
# или сразу пишем команду после скобок
print(price.text)  # в данном случаи достаём и выводим текст


time.sleep(1)  # устанавливаем задержку на выполнение следующего шага своего рода пауза
driver.close()  # закрываем вкладку
driver.quit()  # закрываем браузер
