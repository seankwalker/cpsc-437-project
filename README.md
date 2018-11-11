# wimpdb
("Worse Internet Movie Project Database")  
For Yale's CPSC 437: Database Systems.  

## Authors
* Fatima Kahbi '19
* Sanya Nijhawan '20
* Sean Walker '19

## Technologies
* Database: PostgreSQL
* Frontend: Basic Bootstrap, Jinja, JS if needed (nothing too fancy)
* Backend: Python (Flask)
* Host on Heroku

## Data
From IMDB

## Schema
MOVIES(__id__, name, rating, budget, box\_office, release\_year)

GENRE(__movie\_id__, __genre__)

PEOPLE(__id__, name, gender, birth\_year)

APPEARED(__actor\_id__, movie\_id)

DIRECTED(__dir\_id__, movie\_id)

