# Задание: С заданного сайта возьмите события и дату и создайте словари в словаре
# Решение: Основная конструкция не меняется, решение состоит из 3 строк, начиная с переменной words.
# Для удобства поиска на данном сайте использовали By.CSS_SELECTOR
# Для меньшего использования памяти использовали генератор выражений 
# Код можно напить и с меньшим применением переменных, но тогда теряется читабельность кода
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


drive_path = 'C:/Development/chromedriver'
web_page = 'https://www.python.org/'
words_path = '.event-widget'

driver = webdriver.Chrome(executable_path=drive_path)
driver.get(web_page)

words = driver.find_element(By.CSS_SELECTOR, words_path).text.split('\n')
generate = ({'time': words[i], 'name': words[i+1]} for i in range(2, len(words), 2))
dt = {k: v for k, v in enumerate(generate)}
print(dt)


# sleep(2)
driver.close()
driver.quit()



















