from bs4 import BeautifulSoup
import requests

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'


response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())

name_film = soup.find_all(class_="jsx-4245974604")
list_film = [i.getText() for i in name_film]
# print(*list_film, sep='\n')

with open('movie.txt', 'w', encoding='utf-8') as f:
    for i in list_film:
        f.write(f'{i}\n')
