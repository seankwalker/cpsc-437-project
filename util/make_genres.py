import csv
import pickle

"""
GENRE(**movie_id**, **genre**)
"""

with open("movie_ids.pkl", "rb") as movie_ids_file:
    movie_ids = pickle.load(movie_ids_file)

genre = []
with open("title.basics.tsv", "r") as tsvfile:
    reader = csv.reader(tsvfile, delimiter="\t")

    # input
    # id, name, startYear, genres, titleType 
    fieldnames = "\t".join(next(reader)[0:3]) + "\n"
    fieldnames = "movie_id\tgenre\n"

    # output
    for row in reader:
        if row[0] in movie_ids:
            movie_genres = row[3]
            if "," in movie_genres:
                # multiple genres
                for movie_genre in movie_genres.split(","):
                    # new row for each genre
                    genre.append(row[0] + "\t" + movie_genre.lower() + "\n")
            else:
                # one genre
                genre.append(row[0] + "\t" + movie_genres.lower() + "\n")

with open("genres.tsv", "w") as tsvfile:
    tsvfile.writelines(fieldnames)
    tsvfile.writelines(genre)
