# Data Science ETL Project
- Author: Riley Fletcher
- Focus: Automotive Industry
- Date: 4/6/2024
## Intro
- This project utilizes SQLite by downloading the bundle distribution and directly accessing it via the executables provided.
- This executable can be found at "https://www.sqlite.org/download.html", this project was built using Precompiled Binaries for Windows
- The .gitignore specifies these executables, and sqlite3.exe is required to recreate the steps for this project.
```sql
./sqlite3.exe automotives.db # Lets us access database
```
- We can use the interactive shell, but Python scripts are used for everything in this project.

## Data Sources
- Free Tuning SQL Sample Database https://www.teoalida.com/cardatabase/tuning/
- Manufacturers Gist https://gist.github.com/OdeToCode/582e9c044eee5882d54a6e5997c0be52#file-manufacturers-csv
- Countries API https://restcountries.com/#rest-countries
- Car Data CSV https://www.kaggle.com/datasets/arnavsmayan/vehicle-manufacturing-dataset
- World Happiness Report CSV https://www.kaggle.com/datasets/unsdsn/world-happiness

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
```
PRAGMA table_info(table_name);
```