from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)
today_year = date.today().year
lst_posts = [
  {
  'id': 1,
  "title": "Title #1",
  "subtitle": 'subtitle 123',
  'body': 'some dawafawdvgsfdafaf',
},
  {
  'id': 2,
  "title": "Title #2",
  "subtitle": 'subtitle 456',
  'body': 'more dawafawdvgsfdafaf',
},
  {
  'id': 3,
  "title": "Title #3",
  "subtitle": 'subtitle 789',
  'body': 'and another one dawafawdvgsfdafaf',
},
  {
  'id': 4,
  "title": "Title #4",
  "subtitle": 'subtitle 000',
  'body': 'stop this  shit dawafawdvgsfdafaf',
}
]
url = 'https://api.npoint.io/867e3f77bebb1af35147'
response = requests.get(url)

@app.route('/')
def start_page():
    all_posts = response.json()
    return render_template("indexst.html", year=today_year, post=all_posts)


@app.route('/about')
def about_page():
    return render_template("about.html", year=today_year)


@app.route('/contact')
def contact_page():
    return render_template("contact.html", year=today_year)


@app.route('/<int:num>')
def read_post(num):
    posts = response.json()[num]
    return render_template("pagepost.html", post=posts, year=today_year)


if __name__ == '__main__':
    app.run(debug=True)
