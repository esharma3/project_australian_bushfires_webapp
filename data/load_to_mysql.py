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
TABLENAME = "australia"

df = pd.read_csv("australia.csv", dtype = {"acq_time": "str"})
# Extract, convert to hours and minutes
hour_delta = df["acq_time"].apply(lambda s: pd.to_timedelta(int(s[0:-2]), unit="hours"))
min_delta = df["acq_time"].apply(lambda s: pd.to_timedelta(int(s[-2:]), unit="minutes"))

# Combine to datetime format and append to df
df["acc_datetime"] = pd.to_datetime(df["acq_date"]) + hour_delta + min_delta

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")

try:
    engine.execute(f"CREATE DATABASE {DATABASE}")
except ProgrammingError:
    warnings.warn(
        f"Could not create database {DATABASE}. Database {DATABASE} may already exist."
    )
    pass

engine.execute(f"USE {DATABASE}")

# Send above DataFrame to SQL
df.to_sql(name = TABLENAME, con = engine)