from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def testing():
    return render_template("indextindog.html")


if __name__ == '__main__':
    app.run(debug=True)
