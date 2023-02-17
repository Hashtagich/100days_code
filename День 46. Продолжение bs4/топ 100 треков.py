import requests
from bs4 import BeautifulSoup


data = '2000-08-12'  # input('Введите дату, в формате ГГГГ-ММ-ДД. например 2000-08-12\n')
URL = 'https://www.billboard.com/charts/hot-100/' + data
# print(URL)
response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')

name_music = soup.find_all(name="h3",
                           id='title-of-a-story',
                           class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                  "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                  "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                                  "u-max-width-230@tablet-only")
name_producer = soup.find_all(name="span",
                              class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                     "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
                                     "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")

list_music = [i.getText().strip() for i in name_music]
list_producer = [i.getText().strip() for i in name_producer]
dict_track = {i[0]: i[1] for i in zip(list_music, list_producer)}

first_producer = soup.find(name="span",
                           class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                           "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
                           "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only "
                           "u-font-size-20@tablet").getText().strip()

first_music = soup.find(name="h3",
                        id='title-of-a-story',
                        class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet "
                               "lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max "
                               "a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only "
                               "u-letter-spacing-0028@tablet").getText().strip()

first = {first_music: first_producer}
first.update(dict_track)
print(first)
