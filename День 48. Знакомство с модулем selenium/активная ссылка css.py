from selenium import webdriver
from selenium.webdriver.common.by import By
from re import findall
from time import sleep

drive_path = 'C:/Development/chromedriver'
web_page = 'https://en.wikipedia.org/wiki/Main_Page'
words_path = 'articlecount'

driver = webdriver.Chrome(executable_path=drive_path)
driver.get(web_page)

word = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(word.text)
# words = driver.find_element(By.ID, words_path).text
# print(','.join(findall(r'\d+', words)))



# sleep(2)
driver.close()
driver.quit()