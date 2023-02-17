from flask import Flask, render_template
from requests import get

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello!'


@app.route('/guess/<name_guess>')
def guess(name_guess):
    gender_url = f'https://api.genderize.io?name={name_guess}'
    gender_response = get(url=gender_url)
    gender_date = gender_response.json()
    rand_gender = gender_date['gender']

    years_old_url = f'https://api.agify.io?name={name_guess}'
    years_old_response = get(url=years_old_url)
    years_old_date = years_old_response.json()
    rand_years_old = years_old_date['age']

    return render_template("index.html", name=name_guess, gender=rand_gender, years_old=rand_years_old)


if __name__ == '__main__':
    app.run(debug=True)
