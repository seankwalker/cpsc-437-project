# wimpdb
("Worse Internet Movie [Project] Database")
For Yale's CPSC 437: Database Systems.

## Authors
* Fatima Kahbi '19
* Sanya Nijhawan '20
* Sean Walker '19

## Technologies
* Database: PostgreSQL
* Frontend: Bootstrap, Jinja
* Backend: Python (Flask)
* Hosted on Heroku

## Data
[From IMDB](https://www.imdb.com/interfaces/)

Only including movies since 2010, due to Heroku DB size constraints.

See the `util/` directory for scripts we wrote to transform data from the format it is in the IMDB files into the format we used for our database. In particular, we excluded all films made before 2010 (and, of course, all actors & directors who don't appear/direct any films 2010 and after) and re-did the id system for people and movies s.t. each are merely id'd by the natural numbers (a different set, i.e. there's movie id 1, 2, 3, ... and person id 1, 2, 3, ...).

## Schema
MOVIES(__id__, name, release\_year)

GENRES(__movie\_id__, __genre__)

PEOPLE(__id__, name, birth\_year, death\_year)

APPEARED(__actor\_id__, **movie\_id**)

DIRECTED(__director\_id__, **movie\_id**)

## Report
0) Why we chose this topic:
- We like movies and want to know information about them, with an easy to use but simple interface.
- We are passionate about recent movies, specifically from 2010 onwards statistics.

1) Why WIMPDB is useful and interesting:
- Useful for finding movie titles based on limited information about the movie (e.g., only knowing who directed it, its genre, or when it was released).
- Find new movies to watch released in a given year or with your favorite actors or directors
- Learn about movie statistics such as the genre breakdown for a given year range.

2) Technical Challenges:
- transforming our SQL queries for use with SQLAlchemy
- Using python scripts to clean and format data that we got from IMDB.
- Dealing with issues of Python3 vs Python2 usage in local environments
- Limitations on amount of data we could use due to Heroku constraints.

3) What NF Our Table Meets:
- Our tables meet 1NF: no multivalued attributes in any table. Rather than having the genre attribute be a part of the movies table and be multi-valued, we de composed it into two tables, one dedicated to storing the movies with the genres. We did the same thing with actors and directors, decomposing those into appeared and directed tables to avoid multivalued attributes for 'actor' and 'director' attributes within the movies table.

- Our tables meet 2NF: it is in 1NF and has no partial dependencies. There is never a case where a non-key attribute depends on less than the entire candidate key. appeared, directed, and genres are all composed of the candidate key alone, and movies and genres both do not contain partial dependencies; each non-primary attribute is dependent upon the primary key (st with {primaryA, primaryB} as superkey, primaryA-->non-primary does not occur).

- Our table meets 3NF: it is in 2NF and has no transitive dependencies. We created tables appeared and directed to represent the relationship between people (containing info on the actors/directors) and the movies (containing info specific to the movies). This prevented a situation where a movie_id would determine the actor_name, but actor_name would determine birth_year (a transitive dependency st non-primary-->non-primary).  

Movies: id --> name, release_year
People: id --> name, birth_year, death_year
Appeared: neither movie_id nor actor_id uniquely determine the other attribute, so the primary key is {movie_id, actor_id}
Acted: neither movie_id nor dir_id uniquely determine the other attribute, so the primary key is {movie_id, dir_id}
Genres: neither movie_id nor genre uniquely determine the other attribute, so the primary key is {movie_id, genre}

- Our table meets BCNF: it is in 3NF and for each functional dependency x->y, x is either a key or super key.
Movies: {id} is key
People: {id} is key
Appeared: {movie_id, actor_id} is superkey
Directed: {movie_id, director_id} is superkey
Genres: {movie_id, genre} is superkey

4) Most Interesting Factor of our Project:
- Being able to search for movies with specific actors, genre and time range!
- Our web app's tech-y aesthetic :)
