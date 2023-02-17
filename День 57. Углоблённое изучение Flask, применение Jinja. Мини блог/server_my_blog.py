from flask import Flask, render_template
import requests
from datetime import date

app = Flask(__name__)
# генератор блога для api https://www.npoint.io/docs/867e3f77bebb1af35147

@app.route('/post/<int:num>')
def read_post(num):
    today_year = date.today().year
    url = 'https://api.npoint.io/867e3f77bebb1af35147'
    response = requests.get(url)
    all_posts = response.json()[num]
    return render_template("post.html", post=all_posts, year=today_year)


@app.route('/')
def blog():
    today_year = date.today().year
    url = 'https://api.npoint.io/867e3f77bebb1af35147'
    response = requests.get(url)
    all_posts = response.json()
    return render_template("blog.html", post=all_posts, year=today_year)


if __name__ == '__main__':
    app.run(debug=True)



# url = 'https://api.npoint.io/867e3f77bebb1af35147'
# response = requests.get(url)
# all_posts = response.json()
# print(all_posts)


# lst =[
#   {
#   'id': 1,
#   "title": "Title #1",
#   "subtitle": 'some text 123',
#   'body': 'some dawafawdvgsfdafaf',
# },
#   {
#   'id': 2,
#   "title": "Title #2",
#   "subtitle": 'some text 456',
#   'body': 'more dawafawdvgsfdafaf',
# },
#   {
#   'id': 3,
#   "title": "Title #3",
#   "subtitle": 'some text 789',
#   'body': 'and another one dawafawdvgsfdafaf',
# },
#   {
#   'id': 4,
#   "title": "Title #4",
#   "subtitle": 'some text 000',
#   'body': 'stop this  shit dawafawdvgsfdafaf',
# }
# ]