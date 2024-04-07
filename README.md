# Data Science ETL Project
- Author: Riley Fletcher
- Focus: Automotive Industry
- Date: 4/6/2024

## Instructions
- This project utilizes SQLite by downloading the bundle distribution and directly accessing it via the executables provided.
- This executable can be found at https://www.sqlite.org/download.html, this project was built using Precompiled Binaries for Windows.
- The .gitignore specifies these executables, and while SQLite3 can be added to PATH, it should be noted that this project was built with all files in .gitignore present at the root of the project.
- If using SQLite3.exe directly in root of project, follow instructions exactly. If using sqlite3 via a global install with PATH, use 'sqlite3' instead of './sqlite3.exe'.
### Database Init
- To build the database, simply run the setup script in the root directory.
```bash
python build.py
```
- If successful, there should now be an 'automotives.db' file in the root directory. Now, we can interact using SQLite3.exe or sqlite3 if on PATH.
```sql
./sqlite3.exe automotives.db # Selects database
```
- Once in the shell:
```sql
.databases; # Should show 'automotives' and automotives.db should be present
.tables; # Should show 'cars', 'manufacturers', 'chiptuners', 'country_ids', and 'country_stats'
select * from cars; # Should show all fields in cars
pragma table_info(cars); # Should show cars table schema
```
- We can use the interactive shell to build tables, but Python scripts are used for everything in this project. Only use sqlite3.exe directly for viewing purposes.
### SQL Queries
- Here are some SQL queries we can now do on our database with relational connections.
```sql
# Shows us all car models with a non-modified HP greater than 300
select model from chiptuners where "bhp standard" > 300;

# Shows us countries with a GDP per capita over 1
select country, gdp from country_stat where gdp > 1;

# Shows us how many of each car make exist in cars table
select count(make), make from cars group by make;

# Get all car manufacturers which are based in countries ranked top 10 for overall happiness 
select m.make, m.country from manufacturers m join country c on m.country_id = c.country_id join country_stat cs on c.country_id = cs.country_id where cs.rank <= 10 group by m.make;

# See how many major car manufacturers each country has (ascending order)
select count(country), country from manufacturers group by country order by count(country);

# Shows us statistics for all countries with a major car manufacturer
select * from country_stat where country_id > 0;
```

## Database Schema & Creation
- With SQLite3, database creation is simple - using the connect function will either connect to an existing database, or if that database does not exist, simply creates it instead and continues on.
### Tables
- Manufacturers (Car manufacturers) (foreign key association to country via country_id, foreign key associations to chiptuners and cars via make_id)
- Chiptuners (Instances of car modification specifications) (foreign key association with manufacturers via make_id)
- Cars (Specific trims and years of car models) (foreign key association with manufacturers via make_id)
- Country (Country name, abbreviation, etc.) (foreign key connections to manufacturers and country_stat via country_id)
- Country Statistic (global rankings and individual measurements such as GDP) (foreign key connection to country via country_id)

## Data Sources
- Free Tuning SQL Sample Database 
https://www.teoalida.com/cardatabase/tuning/
- Manufacturers Gist 
https://gist.github.com/OdeToCode/582e9c044eee5882d54a6e5997c0be52#file-manufacturers-csv
- Countries API 
https://restcountries.com/#rest-countries
- Car Data CSV (only used first 500 for size consideration) 
https://www.kaggle.com/datasets/arnavsmayan/vehicle-manufacturing-dataset
- World Happiness Report CSV 
https://www.kaggle.com/datasets/unsdsn/world-happiness

## Extras

### Helpful commands
- See SQLite3 field types (helpful)
``` sql
PRAGMA table_info(table_name);
```