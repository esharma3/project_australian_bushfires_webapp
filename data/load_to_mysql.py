import csv
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings
import sqlalchemy
from config import my_password
import numpy as np

###################################################################
#                 Database Connection to MySQL                    #
###################################################################

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

#########################################################################################
#  Adding Tables to MySQL DB.  If a table already exists, it is dropped and re-added.   #
#########################################################################################

#####################################################################
#                         Fire Count Tables                         #
#####################################################################

# New South Wales
FIRE_COUNT_TABLENAME1 = "nsw_fire_counts"
engine.execute(f"DROP TABLE IF EXISTS {FIRE_COUNT_TABLENAME1}")

df = pd.read_csv(
    "fire_counts_data/MODIS_fire_counts_2002_2019_NSW_per_fire_year.csv"
).to_sql(
    name=FIRE_COUNT_TABLENAME1,
    con=engine,
    index=False,
    dtype=sqlalchemy.types.INTEGER(),
)
engine.execute(f"ALTER TABLE {FIRE_COUNT_TABLENAME1} ADD PRIMARY KEY (`nsw_DOY`)")

FIRE_COUNT_TABLENAME2 = "nsw_annual_total_fire_counts"
engine.execute(f"DROP TABLE IF EXISTS {FIRE_COUNT_TABLENAME2}")

df = pd.read_csv("fire_counts_data/nsw_annual_total_fire_counts.csv").to_sql(
    name=FIRE_COUNT_TABLENAME2,
    con=engine,
    index=False,
    dtype={
        "nsw_fire_year": sqlalchemy.types.String(length=15),
        "nsw_total_fires": sqlalchemy.types.INTEGER(),
    },
)
engine.execute(f"ALTER TABLE {FIRE_COUNT_TABLENAME2} ADD PRIMARY KEY (`nsw_fire_year`)")

# Queensland
FIRE_COUNT_TABLENAME3 = "queensland_fire_counts"
engine.execute(f"DROP TABLE IF EXISTS {FIRE_COUNT_TABLENAME3}")

df = pd.read_csv(
    "fire_counts_data/MODIS_fire_counts_2002_2019_Queensland_per_fire_year.csv"
).to_sql(
    name=FIRE_COUNT_TABLENAME3,
    con=engine,
    index=False,
    dtype=sqlalchemy.types.INTEGER(),
)
engine.execute(
    f"ALTER TABLE {FIRE_COUNT_TABLENAME3} ADD PRIMARY KEY (`queensland_DOY`)"
)

FIRE_COUNT_TABLENAME4 = "queensland_annual_total_fire_counts"
engine.execute(f"DROP TABLE IF EXISTS {FIRE_COUNT_TABLENAME4}")

df = pd.read_csv("fire_counts_data/queensland_annual_total_fire_counts.csv").to_sql(
    name=FIRE_COUNT_TABLENAME4,
    con=engine,
    index=False,
    dtype={
        "queensland_fire_year": sqlalchemy.types.String(length=15),
        "queensland_total_fires": sqlalchemy.types.INTEGER(),
    },
)
engine.execute(
    f"ALTER TABLE {FIRE_COUNT_TABLENAME4} ADD PRIMARY KEY (`queensland_fire_year`)"
)

# Victoria
FIRE_COUNT_TABLENAME5 = "victoria_fire_counts"
engine.execute(f"DROP TABLE IF EXISTS {FIRE_COUNT_TABLENAME5}")

df = pd.read_csv(
    "fire_counts_data/MODIS_fire_counts_2002_2019_Victoria_per_fire_year.csv"
).to_sql(
    name=FIRE_COUNT_TABLENAME5,
    con=engine,
    index=False,
    dtype=sqlalchemy.types.INTEGER(),
)
engine.execute(f"ALTER TABLE {FIRE_COUNT_TABLENAME5} ADD PRIMARY KEY (`victoria_DOY`)")

FIRE_COUNT_TABLENAME6 = "victoria_annual_total_fire_counts"
engine.execute(f"DROP TABLE IF EXISTS {FIRE_COUNT_TABLENAME6}")

df = pd.read_csv("fire_counts_data/victoria_annual_total_fire_counts.csv").to_sql(
    name=FIRE_COUNT_TABLENAME6,
    con=engine,
    index=False,
    dtype={
        "victoria_fire_year": sqlalchemy.types.String(length=15),
        "victoria_total_fires": sqlalchemy.types.INTEGER(),
    },
)
engine.execute(
    f"ALTER TABLE {FIRE_COUNT_TABLENAME6} ADD PRIMARY KEY (`victoria_fire_year`)"
)

#####################################################################
#                Climate and Air Pollutant Tables                   #
#####################################################################

# Australia Max Temp Anomaly Table
CLIMATE_TABLENAME1 = "aus_max_temp_anomaly_data"
engine.execute(f"DROP TABLE IF EXISTS {CLIMATE_TABLENAME1}")

df = pd.read_csv("climate_data/aus_max_temp_anomaly_data.csv").to_sql(
    name=CLIMATE_TABLENAME1,
    con=engine,
    index=False,
    dtype={
        "max_temp_anomaly_year": sqlalchemy.types.INTEGER(),
        "max_temp_anomaly_celcius": sqlalchemy.types.Float(precision=3, asdecimal=True),
    },
)
engine.execute(
    f"ALTER TABLE {CLIMATE_TABLENAME1} ADD PRIMARY KEY (`max_temp_anomaly_year`)"
)

# Australia Min Temp Anomaly Table
CLIMATE_TABLENAME2 = "aus_min_temp_anomaly_data"
engine.execute(f"DROP TABLE IF EXISTS {CLIMATE_TABLENAME2}")

df = pd.read_csv("climate_data/aus_min_temp_anomaly_data.csv").to_sql(
    name=CLIMATE_TABLENAME2,
    con=engine,
    index=False,
    dtype={
        "min_temp_anomaly_year": sqlalchemy.types.INTEGER(),
        "min_temp_anomaly_celcius": sqlalchemy.types.Float(precision=3, asdecimal=True),
    },
)
engine.execute(
    f"ALTER TABLE {CLIMATE_TABLENAME2} ADD PRIMARY KEY (`min_temp_anomaly_year`)"
)

# Australia Mean Temp Anomaly Table
CLIMATE_TABLENAME3 = "aus_mean_temp_anomaly_data"
engine.execute(f"DROP TABLE IF EXISTS {CLIMATE_TABLENAME3}")

df = pd.read_csv("climate_data/aus_mean_temp_anomaly_data.csv").to_sql(
    name=CLIMATE_TABLENAME3,
    con=engine,
    index=False,
    dtype={
        "mean_temp_anomaly_year": sqlalchemy.types.INTEGER(),
        "mean_temp_anomaly_celcius": sqlalchemy.types.Float(
            precision=3, asdecimal=True
        ),
    },
)
engine.execute(
    f"ALTER TABLE {CLIMATE_TABLENAME3} ADD PRIMARY KEY (`mean_temp_anomaly_year`)"
)

# Australia Annual Rainfall Table
CLIMATE_TABLENAME4 = "aus_annual_rainfall_data"
engine.execute(f"DROP TABLE IF EXISTS {CLIMATE_TABLENAME4}")

df = pd.read_csv("climate_data/aus_annual_rainfall_data.csv").to_sql(
    name=CLIMATE_TABLENAME4,
    con=engine,
    index=False,
    dtype={
        "annual_rainfall_year": sqlalchemy.types.INTEGER(),
        "annual_rainfall_mm": sqlalchemy.types.Float(precision=3, asdecimal=True),
    },
)
engine.execute(
    f"ALTER TABLE {CLIMATE_TABLENAME4} ADD PRIMARY KEY (`annual_rainfall_year`)"
)

# Australia Annual Rainfall Anomaly Table
CLIMATE_TABLENAME5 = "aus_annual_rainfall_anomaly_data"
engine.execute(f"DROP TABLE IF EXISTS {CLIMATE_TABLENAME5}")

df = pd.read_csv("climate_data/aus_annual_rainfall_anomaly_data.csv").to_sql(
    name=CLIMATE_TABLENAME5,
    con=engine,
    index=False,
    dtype={
        "annual_rainfall_anomaly_year": sqlalchemy.types.INTEGER(),
        "annual_rainfall_anomaly_mm": sqlalchemy.types.Float(
            precision=3, asdecimal=True
        ),
    },
)
engine.execute(
    f"ALTER TABLE {CLIMATE_TABLENAME5} ADD PRIMARY KEY (`annual_rainfall_anomaly_year`)"
)

# Australia Sea Surface Temperature Anomaly Table
CLIMATE_TABLENAME6 = "aus_sea_surface_temp_anomaly_data"
engine.execute(f"DROP TABLE IF EXISTS {CLIMATE_TABLENAME6}")

df = pd.read_csv("climate_data/aus_sea_surface_temp_anomaly_data.csv").to_sql(
    name=CLIMATE_TABLENAME6,
    con=engine,
    index=False,
    dtype={
        "sea_surface_temp_anomaly_year": sqlalchemy.types.INTEGER(),
        "sea_surface_temp_anomaly_celcius": sqlalchemy.types.Float(
            precision=3, asdecimal=True
        ),
    },
)
engine.execute(
    f"ALTER TABLE {CLIMATE_TABLENAME6} ADD PRIMARY KEY (`sea_surface_temp_anomaly_year`)"
)

# Australia Air Pollutants Table
CLIMATE_TABLENAME7 = "aus_air_pollutants_combined_data"
engine.execute(f"DROP TABLE IF EXISTS {CLIMATE_TABLENAME7}")

df = pd.read_csv("air_pollutant_data/aus_air_pollutants_combined_data.csv").to_sql(
    name=CLIMATE_TABLENAME7,
    con=engine,
    index=False,
    dtype={
        "air_pollutant_year": sqlalchemy.types.INTEGER(),
        "CO2_ppm": sqlalchemy.types.Float(precision=3, asdecimal=True),
        "CH4_ppb": sqlalchemy.types.Float(precision=3, asdecimal=True),
        "N2O_ppb": sqlalchemy.types.Float(precision=3, asdecimal=True),
    },
)
engine.execute(
    f"ALTER TABLE {CLIMATE_TABLENAME7} ADD PRIMARY KEY (`air_pollutant_year`)"
)


##############################################
# Protected species impact table begins here #
##############################################

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
df = df.replace(r'^\s*$', np.NaN, regex=True)


# Sending to DB
df.to_sql(name=IMPACT_TABLENAME1,
          con=engine,
          index=False,
          dtype=schema
          )

# Adding primary key to table
engine.execute(f"ALTER TABLE {IMPACT_TABLENAME1} ADD PRIMARY KEY (`Scientific Name`)")

### End of animal impact table ###



############################################################
### Protected species impact (James') table begins here ###
############################################################
############################################################
### Fire Impacts (James') table begins here ###
############################################################
IMPACT_HISTORIC_FIRES = "historic_fire_data" 
engine.execute(f"DROP TABLE IF EXISTS {IMPACT_HISTORIC_FIRES}")

df = pd.read_csv(
    "df_hist_fires.csv"
).to_sql(
    name=IMPACT_HISTORIC_FIRES,
    con=engine,
    index=False,
    dtype=sqlalchemy.types.INTEGER(),
)
IMPACT_2019_FIRES = "2019_fires" 
engine.execute(f"DROP TABLE IF EXISTS {IMPACT_2019_FIRES}")

df = pd.read_csv(
    "df_2019_2020_fires.csv"
).to_sql(
    name=IMPACT_2019_FIRES,
    con=engine,
    index=False,
    dtype=sqlalchemy.types.INTEGER(),
)
############################################################
### Fire Impacts (James) table ends here
############################################################

############################################################
### Australia Fire Archives (Catherines) table begins here ###
############################################################

AUS_FIRES = "aus_fire_history" 
engine.execute(f"DROP TABLE IF EXISTS {AUS_FIRES}")

df = pd.read_csv("australia.csv").to_sql(
    name = AUS_FIRES,
    con = engine,
    dtype = {'acq_date': sqlalchemy.types.Date, 
    'acq_time': sqlalchemy.types.Time(4)})

### Australia Fire Archives (Catherines) table ends here ###