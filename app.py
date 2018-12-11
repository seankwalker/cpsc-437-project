from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/movies'
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/name/<name>")
def get_movie_name(name):
    return "name : {}".format(name)

if __name__ == '__main__':
    app.debug = True
    app.run()

