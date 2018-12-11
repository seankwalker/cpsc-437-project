
-- CREATE DATABASE wimpdb;
\c wimpdb;

CREATE TABLE directed(dir_id INT, movie_id INT, CONSTRAINT pk_director PRIMARY KEY(director_id, movie_id));
CREATE TABLE movie(id INT, name VARCHAR(100), release_year INT, CONSTRAINT pk_movie PRIMARY KEY(id));
CREATE TABLE people(id INT, name VARCHAR(40),  death_year INT, birth_year INT, CONSTRAINT pk_person PRIMARY KEY(id));
CREATE TABLE genre(movie_id INT, genre VARCHAR(40), CONSTRAINT pk_genre PRIMARY KEY(movie_id, genre));
CREATE TABLE appeared(actor_id INT, movie_id INT, CONSTRAINT pk_appeared PRIMARY KEY(actor_id, movie_id));


\COPY movies FROM 'data/movies.tsv' DELIMITER E'\t';
\COPY directed FROM 'data/directed.tsv' DELIMITER E'\t';
\COPY people FROM 'data/people.tsv' DELIMITER E'\t';
\COPY genre FROM 'data/genres.tsv' DELIMITER E'\t';
\COPY appeared FROM 'data/appeared.tsv' DELIMITER E'\t';
