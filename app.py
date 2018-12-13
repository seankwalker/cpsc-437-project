import os

from flask import Flask, session, render_template, flash, request, redirect,\
	url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import QueryForm
from sqlalchemy import create_engine
import pygal

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

@app.route("/search", methods=["GET"])
def search():
    """
    Endpoint for searchbox to query to get search suggestions.
    """
    if not request.args.get("q"):
        raise RuntimeError("missing search query")

    result = Person.query.filter(Person.name.ilike("%" + request.args.get("q")
	    + "%")).all()
    json = []
    for person in result:
        json.append({"name": person.name})
    return jsonify(json)

# Search form submission
@app.route("/submit", methods=["POST"])
def process_form():
    start_year = request.form["start_year"]
    end_year = request.form["end_year"]
    director = request.form["director"]
    actor = request.form["actor"]
    genres = request.form.getlist("genres")

    results = set()
    filters = {}

    # Start and end year are required
    movies_in_year_range = Movie.query.filter(
    Movie.release_year >= start_year,
    Movie.release_year <= end_year).order_by(Movie.release_year)
    results = set(movies_in_year_range)
    filters["start_year"] = start_year
    filters["end_year"] = end_year

    if director:
        movies_with_director = Movie.query.join(Direction,
                Movie.id == Direction.movie_id).join(Person,
                Direction.director_id == Person.id).filter(
                        Person.name == director)
        results &= set(movies_with_director)
        filters["director"] = director
    if actor:
        movies_with_actor = Movie.query.join(Appearance,
		        Movie.id == Appearance.movie_id).join(Person,
			        Appearance.actor_id == Person.id).filter(
				            Person.name == actor)
        results &= set(movies_with_actor)
        filters["actor"] = actor
    if genres:
        movies_of_genre = Movie.query.join(Genre,
                Movie.id == Genre.movie_id).filter(Genre.genre.in_(genres))
        results &= set(movies_of_genre)
        filters["genres"] = genres

    # Get genres of all resulting movies
    results_with_genres = []
    for movie in results:
        this_movies_genres = Genre.query.filter(Genre.movie_id == movie.id).all()
        results_with_genres.append({"name": movie.name,
                "release_year": movie.release_year, "genre": [g.genre for g in this_movies_genres]})

    # Render result in order of release year, alphabetical order within a year
    sorted_results = sorted(results_with_genres,
	    key=lambda movie: (movie["release_year"], movie["name"]))
    return render_template("result.html",
            searched_for=filters,
            movies=enumerate(sorted_results, 1))

# Breakdown form
@app.route("/breakdown", methods=["GET"])
def breakdown_form():
    return render_template("breakdown-form.html")

@app.route("/submit_breakdown", methods=["POST"])
def process_breakdown_form():
    start_year = request.form["start_year"]
    end_year = request.form["end_year"]

    engine = create_engine("postgres://lznmvmnwxewfng:879d2624ccd62d5435178e4a54f13e8e8415009d91427fa53524c58c03c19897@ec2-54-197-234-33.compute-1.amazonaws.com:5432/dcodd2lcc71npc")
    cur = engine.connect()

    counts = cur.execute("""SELECT genre, COUNT(movies.id) FROM movies, genres WHERE genres.movie_id = movies.id AND movies.release_year BETWEEN %s AND %s GROUP BY genre""", start_year, end_year)

    result = [count for count in counts]
    # print([r[0] for r in result])
    # print([r[1] for r in result])

    result_graph = pygal.Bar()
    pie_chart = pygal.Pie()
    for r in result:
        result_graph.add(r[0], r[1])
        pie_chart.add(r[0], r[1])

    return render_template("breakdown-result.html", graph=result_graph, pie=pie_chart, start_year=start_year, end_year=end_year, genres=result)

# Run Flask
if __name__ == "__main__":
    app.run()