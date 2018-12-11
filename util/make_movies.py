import csv
import pickle

"""
MOVIES(**id**, name, release_year)
""" 

movies = []
movie_ids = set()
with open("title.basics.tsv", "r") as tsvfile:
    reader = csv.reader(tsvfile, delimiter="\t")

    # input fieldnames row
    # id, name, startYear, genres, titleType 
    next(reader)

    # output fieldnames
    fieldnames = "id\tname\trelease_year\n"

    # search
    for row in reader:
        if row[0] != "\\N" and row[1] != "\\N" and row[2] != "\\N" and row[3] != "\\N" and row[4] == "movie":
            # only movies since 2010
            if int(row[2]) < 2010: continue
            movies.append("\t".join(row[0:3]) + "\n")
            movie_ids.add(row[0])

with open("movies.tsv", "w") as tsvfile:
    tsvfile.writelines(fieldnames)
    tsvfile.writelines(movies)

with open("movie_ids.pkl", "wb") as movie_ids_file:
    pickle.dump(movie_ids, movie_ids_file)
