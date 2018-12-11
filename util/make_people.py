import csv
import pickle

"""
PEOPLE(**id**, name, birth_year, death_year)
"""

# load in actors' and directors' ids
# into `actors`, `directors`
# with open("actors.pkl", "rb") as actors_file, open("directors.pkl", "rb") as directors_file:
with open("people_ids.pkl", "rb") as pickle_file:
    # actors = pickle.load(actors_file)
    # directors = pickle.load(directors_file)
    people_ids = pickle.load(pickle_file)

people = []
with open("name.basics.tsv", "r") as tsvfile:
    reader = csv.reader(tsvfile, delimiter="\t")

    # nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles
    # only care about the first four!
    # fieldnames = "\t".join(next(reader)[0:4]) + "\n")
    fieldnames = "id\tname\tbirth_year\tdeath_year\n"

    for row in reader:
        # don't add people not in our movies
        if row[0] not in people_ids: continue
        people.append("\t".join(row[0:4]) + "\n")

with open("people.tsv", "w") as tsvfile:
    tsvfile.writelines(fieldnames)
    tsvfile.writelines(people)
