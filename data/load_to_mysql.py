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
