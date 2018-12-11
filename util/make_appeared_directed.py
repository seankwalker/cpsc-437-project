import csv
import pickle

with open("movie_ids.pkl", "rb") as pickle_file, open("people_ids.pkl", "rb") as pickle_file2:
    movie_ids = pickle.load(pickle_file)
    people_ids = pickle.load(pickle_file2)

appeared = []
directed = []
with open("title.principals.tsv", "r") as tsvfile:
    reader = csv.reader(tsvfile, delimiter="\t")
    next(reader)

    for row in reader:
        # tconst, ordering, nconst, category, job, characters
        if row[0] not in movie_ids: continue
        if row[2] not in people_ids: continue

        if row[3] in ("actor", "actress"):
            appeared.append(row[2] + "\t" + row[0] + "\n")
        elif row[3] == "director":
            directed.append(row[2] + "\t" + row[0] + "\n")

with open("appeared.tsv", "w") as tsvfile:
    tsvfile.write("actor_id\tmovie_id\n")
    tsvfile.writelines(appeared)

with open("directed.tsv", "w") as tsvfile:
    tsvfile.write("dir_id\tmovie_id\n")
    tsvfile.writelines(directed)
