from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

drive_path = 'C:/Development/chromedriver'
web_page = 'http://secure-retreat-92358.herokuapp.com/'
my_mail, my_first_name, my_last_name = 'testmail.@mail.ru', '123qwe', 'kersh'  # логин, пароль для входа
# Пути для поиска нужных полей
first_name_path = 'fName'
last_name_path = 'lName'
email_path = 'email'
button_name_path = 'form button'


driver = webdriver.Chrome(executable_path=drive_path)
driver.get(web_page)

# Находим нужные поля и заключаем их в переменные
first_name = driver.find_element(By.NAME, first_name_path)  # поле имени
last_name = driver.find_element(By.NAME, last_name_path)  # поле фамилии
email = driver.find_element(By.NAME, email_path)  # поле почты
button = driver.find_element(By.CSS_SELECTOR, button_name_path)  # кнопка войти

first_name.send_keys(my_first_name)
last_name.send_keys(my_last_name)
email.send_keys(my_mail)
sleep(2)
email.send_keys(Keys.ENTER)  # подтверждаем ввод нажатием ENTER
# или
# button.click()  # подтверждаем ввод нажатием на кнопку на сайте

sleep(5)
driver.close()
driver.quit()
