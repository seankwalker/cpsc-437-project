import pickle

"""
Change all IDs from ttXXXXXXX to 1, 2, 3, ...
"""

# iterate over movie ids
with open("movie_ids.pkl", "rb") as pickle_file:
    ids = pickle.load(pickle_file)

# iterate over people ids
with open("people_ids.pkl", "rb") as pickle_file:
    people_ids = pickle.load(pickle_file)

# we reference a given movie_id in:
# - MOVIES (one row in the table)
# - GENRES (arbitrarily many rows in the table)
# - APPEARED (arbitrarily many rows in the table)
# - DIRECTED (arbitrarily many rows in the table)

# we reference a given person id in:
# - PEOPLE (one row)
# - APPEARED, DIRECTED (arb. many)

with open("movies.tsv", "r") as movies_file, open("genres.tsv", "r") as genres_file, open("appeared.tsv", "r") as appeared_file, open("directed.tsv", "r") as directed_file, open("people.tsv", "r") as people_file:

    movies_file_lines = movies_file.readlines()
    genres_file_lines = genres_file.readlines()
    appeared_file_lines = appeared_file.readlines()
    directed_file_lines = directed_file.readlines()
    people_file_lines = people_file.readlines()

    new_id = 1
    for movie_id in ids:
        # renumber in MOVIES
        movies_file_lines = [line.replace(movie_id, str(new_id)) for line in movies_file_lines]

        # renumber in GENRES
        genres_file_lines = [line.replace(movie_id, str(new_id)) for line in genres_file_lines]

        # renumber in APPEARED
        appeared_file_lines = [line.replace(movie_id, str(new_id)) for line in appeared_file_lines]

        # renumber in DIRECTED
        directed_file_lines = [line.replace(movie_id, str(new_id)) for line in directed_file_lines]

        new_id += 1

    new_person_id = 1
    for person_id in people_ids:
        # PEOPLE
        people_file_lines = [line.replace(person_id, str(new_person_id)) for line in people_file_lines]

        # APPEARED
        appeared_file_lines = [line.replace(person_id, str(new_person_id)) for line in appeared_file_lines]
    
        # DIRECTED
        directed_file_lines = [line.replace(person_id, str(new_person_id)) for line in directed_file_lines]
        
        new_person_id += 1

with open("movies_renumbered.tsv", "w") as movies_file:
    movies_file.writelines(movies_file_lines)
with open("genres_renumbered.tsv", "w") as genres_file:
    genres_file.writelines(genres_file_lines)
with open("appeared_renumbered.tsv", "w") as appeared_file:
    appeared_file.writelines(appeared_file_lines)
with open("directed_renumbered.tsv", "w") as directed_file:
    directed_file.writelines(directed_file_lines)
with open("people_renumbered.tsv", "w") as people_file:
    people_file.writelines(people_file_lines)
