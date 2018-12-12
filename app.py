import os

from flask import Flask, session, render_template, flash, request, redirect,\
        url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import QueryForm

# Flask setup
app = Flask(__name__)

# Database for SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# API Key for WTForm
# TODO: ideally should take this out for prod
app.config["SECRET_KEY"] = "7d4e41f27d441f27567d441f2b6176a"

# Turn debug mode on, for development purposes (TODO: can take out in prod!)
app.debug = True

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# Database object
db = SQLAlchemy(app)

# Movie, Genre, Person, Appearance, Direction
from models import *

# Bootstrap setup
bootstrap = Bootstrap(app)

# Homepage (form)
@app.route("/", methods=['GET'])
def index():
	form = QueryForm(request.form)
	return render_template('index.html', form=form)

# Form submission
@app.route("/submit", methods=["POST"])
def process_form():
    # Proces form data
	form = QueryForm(request.form)
	start_year = request.form["start_year"]
	end_year = request.form["end_year"]
	director = request.form["director"]
	actor = request.form["actor"]
	genres = form.genres.data

    # MVP of database operations
    # TODO: make this actually use filters and such
    # movies = Movie.query.join(Genre, Movie.id == Genre.movie_id).filter(Movie.release_year == year, Genre.genre == genre).all()

    #return render_template("result.html",
    #        message=f"All {genre} movies from {year}:",
    #        movies=enumerate(movies, 1))

# Run Flask
if __name__ == '__main__':
    app.run()
