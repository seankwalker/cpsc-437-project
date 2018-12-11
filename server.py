import psycopg2
conn = psycopg2.connect("host=localhost dbname=wimpdb user=postgres")
cur = conn.cursor()

# create tables
cur.execute("""
CREATE TABLE directed(
    dir_id INT,
    movie_id INT,
    CONSTRAINT pk_director PRIMARY KEY(director_id, movie_id)
);
CREATE TABLE movie(
    id INT,
    name VARCHAR(100),
    release_year INT,
    CONSTRAINT pk_movie PRIMARY KEY(id)
);
CREATE TABLE people(
    id INT,
    name VARCHAR(40),
    death_year INT,
    birth_year INT,
    CONSTRAINT pk_person PRIMARY KEY(id)
);
CREATE TABLE genre(
    movie_id INT,
    genre VARCHAR(40),
    CONSTRAINT pk_genre PRIMARY KEY(movie_id, genre)
);
CREATE TABLE appeared(
    actor_id INT,
    movie_id INT,
    CONSTRAINT pk_appeared PRIMARY KEY(actor_id, movie_id)
);
""")
conn.commit()

# insert data from files into tables
with open('appeared.tsv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'appeared', sep='\t')
f.close()

with open('directed.tsv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'directed', sep='\t')
f.close()

with open('movies.tsv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'movies', sep='\t')
f.close()

with open('genres.tsv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'genre', sep='\t')
f.close()

with open('people.tsv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'people', sep='\t')
f.close()

conn.commit()


one = cur.fetchone()
all = cur.fetchall()
