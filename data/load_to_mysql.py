import csv, os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings
from config import my_password

USER = "root"
PASSWORD = my_password
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "bushfires_db"
TABLENAME = "fire_archives"

df = pd.read_csv("fire_archives.csv")

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")
try:
    engine.execute(f"CREATE DATABASE {DATABASE}")
except ProgrammingError:
    warnings.warn(
        f"Could not create database {DATABASE}. Database {DATABASE} may already exist."
    )
    pass
engine.execute(f"USE {DATABASE}")
# engine.execute(f"DROP TABLE IF EXISTS {TABLENAME}")

#Send above DataFrame to SQL
df.to_sql(name = TABLENAME, con = engine)