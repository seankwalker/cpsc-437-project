
CREATE DATABASE IF NOT EXISTS wimpdb;
USE wimpdb;

CREATE TABLE IF NOT EXISTS movie(id INT, name VARCHAR(40), rating DECIMAL(2,1), box_office INT, release_date INT, CONSTRAINT pk_movie PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS person(id INT, name VARCHAR(40), gender CHAR, birth DATE, CONSTRAINT pk_person PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS appeared(actor_id INT, movie_id INT, role VARCHAR(40), CONSTRAINT pk_appeared PRIMARY KEY(actor_id, movie_id));
CREATE TABLE IF NOT EXISTS directed(director_id INT, movie_id INT,, CONSTRAINT pk_director PRIMARY KEY(director_id, movie_id));

COPY movie
FROM '~/Desktop/cpsc-437-project/data/movies.tsv' DELIMITER E'\t';

COPY genre
FROM '~/Desktop/cpsc-437-project/data/movies.tsv' DELIMITER E'\t';

COPY people
FROM '~/Desktop/cpsc-437-project/data/movies.tsv' DELIMITER E'\t';

COPY appeared
FROM '~/Desktop/cpsc-437-project/data/movies.tsv' DELIMITER E'\t';

COPY directed
FROM '~/Desktop/cpsc-437-project/data/movies.tsv' DELIMITER E'\t';
