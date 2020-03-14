import csv, os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings
import sqlalchemy
from config import my_password

USER = "root"
PASSWORD = my_password
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "bushfires_db"

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")

try:
    engine.execute(f"CREATE DATABASE {DATABASE}")
except ProgrammingError:
    warnings.warn(
        f"Could not create database {DATABASE}. Database {DATABASE} may already exist."
    )
    pass

engine.execute(f"USE {DATABASE}")

# The below script is for adding tables to the database. If a table already exists, it is dropped and re-added. 

# Fire Count tables begin here --------------------------------------------------------------------------------
# New South Wales 
FIRE_COUNT_TABLENAME1 = "nsw_fire_counts" 
engine.execute(f"DROP TABLE IF EXISTS {FIRE_COUNT_TABLENAME1}")

df = pd.read_csv(
    "fire_counts_data/Table_MODIS_fire_counts_2002_2019_NSW_per_fire_year.csv"
).to_sql(
    name=FIRE_COUNT_TABLENAME1,
    con=engine,
    index=False,
    dtype=sqlalchemy.types.INTEGER(),
)

# Queensland 
FIRE_COUNT_TABLENAME2 = "queensland_fire_counts"
engine.execute(f"DROP TABLE IF EXISTS {FIRE_COUNT_TABLENAME2}")

df = pd.read_csv(
    "fire_counts_data/Table_MODIS_fire_counts_2002_2019_Queensland_per_fire_year.csv"
).to_sql(
    name=FIRE_COUNT_TABLENAME2,
    con=engine,
    index=False,
    dtype=sqlalchemy.types.INTEGER(),
)

# Victoria 
FIRE_COUNT_TABLENAME3 = "victoria_fire_counts" 
engine.execute(f"DROP TABLE IF EXISTS {FIRE_COUNT_TABLENAME3}")

df = pd.read_csv(
    "fire_counts_data/Table_MODIS_fire_counts_2002_2019_Victoria_per_fire_year.csv"
).to_sql(
    name=FIRE_COUNT_TABLENAME3,
    con=engine,
    index=False,
    dtype=sqlalchemy.types.INTEGER(),
)
# End of Fire Count tables


############################################################
### Protected species impact (David's) table begins here ###
############################################################

IMPACT_TABLENAME1 = "protected_species_impact_counts" 
engine.execute(f"DROP TABLE IF EXISTS {IMPACT_TABLENAME1}")

# Creating dict of dtypes for SQL alchemy
schema = {"Scientific Name": sqlalchemy.types.String(length=300), 
          "Common Name": sqlalchemy.types.String(length=300), 
          "Afected Area": sqlalchemy.types.String(length=50), 
          "Area Min": sqlalchemy.types.INTEGER,
          "Area Max": sqlalchemy.types.INTEGER,
          "Type": sqlalchemy.types.String(length=50),
          "Protected Status": sqlalchemy.types.String(length=25),
          "Migratory Status ": sqlalchemy.types.String(length=25),
          "Location": sqlalchemy.types.String(length=50)
}


# Doing some data cleaning
df = pd.read_csv("protected_species_impact.csv")\
       .fillna('N/A')\
       .rename(columns = {"Percentage of the species modelled likely and known distribution within fire affected areas": "Afected Area", 
                          "EPBC Act listed Threatened Status": "Protected Status", 
                          "EPBC Act listed Migratory Status": "Migratory Status", 
                          "Range states and territories": "Location"})\
       .replace({'Afected Area': '≥80%'}, '>80%')

min_range = [df["Afected Area"][e][:3].strip("%|<|>| ") for e in df["Afected Area"].index]
max_range = [df["Afected Area"][e][5:-1].strip("%|<|>| ").replace("", '0') for e in df["Afected Area"].index]

df.insert(column='Area Min', value=min_range, loc=3)
df.insert(column='Area Max', value=max_range, loc=4)


# Sending to DB
df.to_sql(name=IMPACT_TABLENAME1,
             con=engine,
             index=False,
             dtype=schema
             )

### End of animal impact table ###

