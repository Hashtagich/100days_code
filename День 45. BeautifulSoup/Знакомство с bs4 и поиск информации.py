from bs4 import BeautifulSoup
import requests

web = 'https://news.ycombinator.com/news'

respons = requests.get(web)
text = respons.text
soup = BeautifulSoup(text, 'html.parser')

article_tag = soup.select(selector='.titleline')
article_upvote = soup.find_all(name='span', class_='score')

list_text = [i.getText() for i in article_tag]
list_link = [i.find(name='a').get('href') for i in article_tag]
list_score = [int(i.getText().split()[0]) for i in article_upvote]

# print(*list_text, sep='\n')
# print(*list_link, sep='\n')
# print(list_score, max(list_score))


dic = {i[0]: (i[1], i[2]) for i in zip(list_text, list_link, list_score)}
max_score_new = max(dic.items(), key=lambda x: x[1][1])
print(max_score_new)
print(soup)