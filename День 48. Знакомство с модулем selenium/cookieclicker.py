from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time


def get_price(string):
    list_words = string.text.split()
    ind = list_words.index('-') + 1
    return int(list_words[ind].replace(',', ''))


drive_path = 'C:/Development/chromedriver'
web_page = 'http://orteil.dashnet.org/experiments/cookie/'
how_minutes_work = 1
timeout = time() + 60 * how_minutes_work

driver = webdriver.Chrome(executable_path=drive_path)
driver.get(web_page)

button_cookie = driver.find_element(By.ID, 'cookie')
money_score = driver.find_element(By.ID, 'money')

while True:
    if time() > timeout:
        break

    price_list = (
        'buyTime machine',
        'buyPortal',
        'buyAlchemy lab',
        'buyShipment',
        'buyMine',
        'buyFactory',
        'buyGrandma',
        'buyCursor'
    )
    button_cookie.click()

    for item in price_list:
        money = int(money_score.text.replace(',', '')) if "," in money_score.text else int(money_score.text)

        if money > get_price(driver.find_element(By.ID, item)):
            driver.find_element(By.ID, item).click()
            break


total_score = driver.find_element(By.ID, 'cps')
print(total_score.text)

driver.close()
driver.quit()
