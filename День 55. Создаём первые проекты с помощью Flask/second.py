from flask import Flask

app = Flask(__name__)


def make_bold(func):
    # def wrapper(*args):
    #     return f'<b>{func(*args)}</b>'
    # return wrapper
    return lambda *args: f'<b>{func(*args)}</b>'


def make_emphasis(func):
    # def wrapper(*args):
    #     return f'<em>{func(*args)}</em>'
    # return wrapper
    return lambda *args: f'<em>{func(*args)}</em>'


def make_underlined(func):
    # def wrapper(*args):
    #     return f'<u>{func(*args)}</u>'
    # return wrapper
    return lambda *args: f'<u>{func(*args)}</u>'

@app.route('/')
def hello_world():
    return 'Hello, word!'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye!'


if __name__ == '__main__':
    app.run(debug=True)



