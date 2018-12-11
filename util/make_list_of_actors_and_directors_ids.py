import csv
import pickle

# makes list of all people who have actor or director roles in `title.principals.tsv`

actors = set()
directors = set()
people = set()
with open("movie_ids.pkl", "rb") as pickle_file:
    movie_ids = pickle.load(pickle_file)

with open("title.principals.tsv", "r") as tsvfile:
    reader = csv.reader(tsvfile, delimiter="\t")

    # tconst, ordering, nconst, category, job (doesn't matter), characters(doesn't matter)
    for row in reader:
        # make sure this person made an appearance
        if row[0] not in movie_ids: continue
        if row[3] == "actor" or row[3] == "actress":
            actors.add(row[2])
        elif row[3] == "director":
            directors.add(row[2])

people = actors.union(directors)
# with open("actors.pkl", "wb") as actors_file, open("directors.pkl", "wb") as directors_file, 
with open("people_ids.pkl", "wb") as people_file:
    pickle.dump(people, people_file)
