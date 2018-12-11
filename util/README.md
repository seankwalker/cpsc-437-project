# Data transformation: IMDB format to our format

**Prerequisite:** You need the following files (from IMDB):
1. `title.basics.tsv` (movie information)
2. `title.principals.tsv` (movie cast/crew)
3. `name.basics.tsv` (person information)

Run the scripts in the following order:
1. `python make_movies.py`
2. `python make_genres.py`, `python make_list_of_actors_and_directors_ids.py` (order doesn't matter)
3. `python make_people.py`
4. `python make_appeared_directed.py`
5. `python renumber_ids.py`

You're good to go!
