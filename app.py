from flask import Flask, session, render_template, flash, request, redirect,\
url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import QueryForm

# Flask setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/wimpdb'
app.config['SECRET_KEY'] = '7d4e41f27d441f27567d441f2b6176a'
db = SQLAlchemy(app)

# Bootstrap setup
bootstrap = Bootstrap(app)

# index.html
@app.route("/", methods=['GET'])
def index():
	form = QueryForm(request.form)
	return render_template('index.html', form=form)

# Form submission
@app.route("/submit", methods=["POST"])
def process_form():
	form = QueryForm(request.form)
	start_year = request.form["start_year"]
	end_year = request.form["end_year"]
	director = request.form["director"]
	actor = request.form["actor"]
	genres = form.genres.data
	print genres
	return 'ok'
    # Query the Heroku DB with SQLAlchemy (`db`)

# Run Flask
if __name__ == '__main__':
    app.debug = True
    app.run()

