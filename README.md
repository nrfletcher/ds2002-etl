# Data Science ETL Project
- Author: Riley Fletcher
- Focus: Automotive Industry
- Date: 4/6/2024

## Intro
- This project utilizes SQLite by downloading the bundle distribution and directly accessing it via the executables provided.
- This executable can be found at https://www.sqlite.org/download.html, this project was built using Precompiled Binaries for Windows.
- The .gitignore specifies these executables, and while SQLite3 can be added to PATH, it should be noted that this project was built with all files in .gitignore present at the root of the project.
- If SQLite3.exe is not present in your project root before running the setup script, it is not assured this project will build correctly.
```sql
./sqlite3.exe automotives.db # Selects database
```
- Once in the shell:
```sql
.databases; # Should show 'automotives' and automotives.db should be present
.tables; # Should show 'cars', 'manufacturers', 'chiptuners', 'country_ids', and 'country_stats'
```
- We can use the interactive shell to build tables, but Python scripts are used for everything in this project. Only use sqlite3.exe directly for viewing purposes.

## Data Sources
- Free Tuning SQL Sample Database 
https://www.teoalida.com/cardatabase/tuning/
- Manufacturers Gist 
https://gist.github.com/OdeToCode/582e9c044eee5882d54a6e5997c0be52#file-manufacturers-csv
- Countries API 
https://restcountries.com/#rest-countries
- Car Data CSV 
https://www.kaggle.com/datasets/arnavsmayan/vehicle-manufacturing-dataset
- World Happiness Report CSV 
https://www.kaggle.com/datasets/unsdsn/world-happiness

## Database Schema & Creation
- With SQLite3, database creation is quite simple - using the connect function will either connect to an existing database, or if that database does not exist, simply creates it instead and continues on.
### Tables
- Manufacturers
- Chiptuners
- Cars
- Country Identifier
- Country Statistic

## Environment Variables
- The .env folder is included in the .gitignore, which contains API keys. To use this project you will need your own API key.
- See SQLite3 field types (helpful)
``` sql
PRAGMA table_info(table_name);
```