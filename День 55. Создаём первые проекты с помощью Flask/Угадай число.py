from flask import Flask
from random import randint

app = Flask(__name__)
goal_num = randint(0, 9)
print(goal_num)

@app.route('/')
def hello_world():
    return '<h1>Угадайте число от 0 до 9!</h1>' \
           '<img src="https://i.gifer.com/origin/af/af2cc4e6cd466cb15f6c06fe0da4b87c_w200.webp"width=200>'


@app.route('/<int:number>')
def say_bye(number):
    if goal_num == number:
        return '<h1 style="color:green;">Ты угадал!</h1>'\
               '<img src="https://i.gifer.com/origin/e5/e565e75c87c44d9082e1ed9e8445970a_w200.webp"width=400>'
    elif number > goal_num:
        return '<h1 style="color:red;">Перебор! Попробуй ещё раз!</h1>'\
               '<img src="https://i.gifer.com/origin/87/876fd3a2c5091f991dd3ce95847c47b1_w200.webp"width=400>'
    else:
        return '<h1 style="color:red;">Недобор! Попробуй ещё раз!</h1>'\
               '<img src="https://i.gifer.com/origin/87/876fd3a2c5091f991dd3ce95847c47b1_w200.webp"width=400>'


if __name__ == '__main__':
    app.run(debug=True)



