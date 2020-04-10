import csv
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings
import sqlalchemy
import numpy as np
import os

# Importing dependencies for scraping
import requests
from bs4 import BeautifulSoup
my_password = "Bakken11"

USER = "root"
PASSWORD = my_password
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "bushfires_db"

###################################################################
#                 Database Connection to MySQL                    #
###################################################################
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")
try:
    engine.execute(f"CREATE DATABASE {DATABASE}")
except ProgrammingError:
    warnings.warn(
        f"Could not create database {DATABASE}. Database {DATABASE} may already exist."
    )
    pass
engine.execute(f"USE {DATABASE}")

########################################################################################
 Adding Tables to MySQL DB.  If a table already exists, it is dropped and re-added.   #
########################################################################################

####################################################################
                        Fire Count Tables                         #
####################################################################

New South Wales
FIRE_COUNT_TABLENAME1 = "nsw_fire_counts"
engine.execute(f"DROP TABLE IF EXISTS {FIRE_COUNT_TABLENAME1}")

df = pd.read_csv(
    "fire_counts_data/MODIS_fire_counts_2002_2019_NSW_per_fire_year.csv"
).to_sql(
    name=FIRE_COUNT_TABLENAME1,
    con=engine,
    index=False,
    dtype={
        "nsw_month": sqlalchemy.types.String(length=15),
        "nsw_DOY": sqlalchemy.types.INTEGER(),
        "nsw_2002_2003": sqlalchemy.types.INTEGER(),
        "nsw_2003_2004": sqlalchemy.types.INTEGER(),
        "nsw_2004_2005": sqlalchemy.types.INTEGER(),
        "nsw_2005_2006": sqlalchemy.types.INTEGER(),
        "nsw_2006_2007": sqlalchemy.types.INTEGER(),
        "nsw_2007_2008": sqlalchemy.types.INTEGER(),
        "nsw_2008_2009": sqlalchemy.types.INTEGER(),
        "nsw_2009_2010": sqlalchemy.types.INTEGER(),
        "nsw_2010_2011": sqlalchemy.types.INTEGER(),
        "nsw_2011_2012": sqlalchemy.types.INTEGER(),
        "nsw_2012_2013": sqlalchemy.types.INTEGER(),
        "nsw_2013_2014": sqlalchemy.types.INTEGER(),
        "nsw_2014_2015": sqlalchemy.types.INTEGER(),
        "nsw_2015_2016": sqlalchemy.types.INTEGER(),
        "nsw_2016_2017": sqlalchemy.types.INTEGER(),
        "nsw_2017_2018": sqlalchemy.types.INTEGER(),
        "nsw_2018_2019": sqlalchemy.types.INTEGER(),
        "nsw_2019_2020": sqlalchemy.types.INTEGER(),
    },
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
    dtype={
        "queensland_month": sqlalchemy.types.String(length=15),
        "queensland_DOY": sqlalchemy.types.INTEGER(),
        "queensland_2002_2003": sqlalchemy.types.INTEGER(),
        "queensland_2003_2004": sqlalchemy.types.INTEGER(),
        "queensland_2004_2005": sqlalchemy.types.INTEGER(),
        "queensland_2005_2006": sqlalchemy.types.INTEGER(),
        "queensland_2006_2007": sqlalchemy.types.INTEGER(),
        "queensland_2007_2008": sqlalchemy.types.INTEGER(),
        "queensland_2008_2009": sqlalchemy.types.INTEGER(),
        "queensland_2009_2010": sqlalchemy.types.INTEGER(),
        "queensland_2010_2011": sqlalchemy.types.INTEGER(),
        "queensland_2011_2012": sqlalchemy.types.INTEGER(),
        "queensland_2012_2013": sqlalchemy.types.INTEGER(),
        "queensland_2013_2014": sqlalchemy.types.INTEGER(),
        "queensland_2014_2015": sqlalchemy.types.INTEGER(),
        "queensland_2015_2016": sqlalchemy.types.INTEGER(),
        "queensland_2016_2017": sqlalchemy.types.INTEGER(),
        "queensland_2017_2018": sqlalchemy.types.INTEGER(),
        "queensland_2018_2019": sqlalchemy.types.INTEGER(),
        "queensland_2019_2020": sqlalchemy.types.INTEGER(),
    },
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
    dtype={
        "victoria_month": sqlalchemy.types.String(length=15),
        "victoria_DOY": sqlalchemy.types.INTEGER(),
        "victoria_2002_2003": sqlalchemy.types.INTEGER(),
        "victoria_2003_2004": sqlalchemy.types.INTEGER(),
        "victoria_2004_2005": sqlalchemy.types.INTEGER(),
        "victoria_2005_2006": sqlalchemy.types.INTEGER(),
        "victoria_2006_2007": sqlalchemy.types.INTEGER(),
        "victoria_2007_2008": sqlalchemy.types.INTEGER(),
        "victoria_2008_2009": sqlalchemy.types.INTEGER(),
        "victoria_2009_2010": sqlalchemy.types.INTEGER(),
        "victoria_2010_2011": sqlalchemy.types.INTEGER(),
        "victoria_2011_2012": sqlalchemy.types.INTEGER(),
        "victoria_2012_2013": sqlalchemy.types.INTEGER(),
        "victoria_2013_2014": sqlalchemy.types.INTEGER(),
        "victoria_2014_2015": sqlalchemy.types.INTEGER(),
        "victoria_2015_2016": sqlalchemy.types.INTEGER(),
        "victoria_2016_2017": sqlalchemy.types.INTEGER(),
        "victoria_2017_2018": sqlalchemy.types.INTEGER(),
        "victoria_2018_2019": sqlalchemy.types.INTEGER(),
        "victoria_2019_2020": sqlalchemy.types.INTEGER(),
    },
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

# Annual max temp percentage area in decile 10
CLIMATE_TABLENAME8 = "aus_max_temp_area_decile10"
engine.execute(f"DROP TABLE IF EXISTS {CLIMATE_TABLENAME8}")

df = pd.read_csv("climate_data/aus_max_temp_area_decile10.csv").to_sql(
    name=CLIMATE_TABLENAME8,
    con=engine,
    index=False,
    dtype={
        "max_temp_decile10_year": sqlalchemy.types.INTEGER(),
        "maxtemp_total_land_area_percentage": sqlalchemy.types.Float(
            precision=3, asdecimal=True
        ),
    },
)
engine.execute(
    f"ALTER TABLE {CLIMATE_TABLENAME8} ADD PRIMARY KEY (`max_temp_decile10_year`)"
)

# Annual rainfall percentage area in decile 10
CLIMATE_TABLENAME9 = "aus_annual_rainfall_area_decile10"
engine.execute(f"DROP TABLE IF EXISTS {CLIMATE_TABLENAME9}")

df = pd.read_csv("climate_data/aus_annual_rainfall_area_decile10.csv").to_sql(
    name=CLIMATE_TABLENAME9,
    con=engine,
    index=False,
    dtype={
        "annual_rainfall_decile10_year": sqlalchemy.types.INTEGER(),
        "rainfall_total_land_area_percentage": sqlalchemy.types.Float(
            precision=3, asdecimal=True
        ),
    },
)
engine.execute(
    f"ALTER TABLE {CLIMATE_TABLENAME9} ADD PRIMARY KEY (`annual_rainfall_decile10_year`)"
)



##########################################################
#         Protected species impact table + scraper       #
##########################################################

IMPACT_TABLENAME1 = "protected_species_impact" 
engine.execute(f"DROP TABLE IF EXISTS {IMPACT_TABLENAME1}")

# Initial csv loading > df
df = pd.read_csv("protected_species_impact.csv")\
       .fillna('N/A')\
       .rename(columns = {"Percentage of the species modelled likely and known distribution within fire affected areas": "Affected Area", 
                          "EPBC Act listed Threatened Status": "Protected Status", 
                          "EPBC Act listed Migratory Status": "Migratory Status", 
                          "Range states and territories": "Location",
                          "SPRAT ID": "taxon_id"})\
       .replace({'Affected Area': '≥80%'}, '>80%')

# Breaking "Affected Area" by Min and Max ranges
min_range = [df["Affected Area"][e][:3].strip("%|<|>| ") for e in df["Affected Area"].index]
max_range = [df["Affected Area"][e][5:-1].strip("%|<|>| ") for e in df["Affected Area"].index]

# Adding coverage maps
distro_map = ['http://www.environment.gov.au/webgis-framework/apps/species-discovery/sd.html?map_taxon_id=' + str(df["taxon_id"][e]) for e in df["taxon_id"].index]

# Scraping thumbnails from bing
thumbnail_url = []
for e in df["Common Name"].index:
    r = requests.get(('https://www.bing.com/images/search?q={}').format(str(df["Common Name"][e])).replace(" ", "_")).text
    item = BeautifulSoup(r).find_all('img')[1]['src']
    thumbnail_url.append(item)

# Inserting all new columns
df.insert(column='Area Min', value=min_range, loc=1)
df.insert(column='Area Max', value=max_range, loc=2)
df.insert(column='Distribution Map', value=distro_map, loc=3)
df.insert(column='Thumbnail', value=thumbnail_url, loc=4)

# Cleaning some data and rearranging columns
df = df.replace(r'^\s*$', np.NaN, regex=True)
df = df[['taxon_id','Scientific Name','Common Name','Affected Area', 'Area Min', 'Area Max', 'Type', 'Protected Status', 'Migratory Status', 'Location', 'URL', 'Distribution Map', 'Thumbnail']]
df.columns = map(str.lower, df.columns.str.replace(" ", "_"))

# Creating schema for SQL table
schema = {"taxon_id": sqlalchemy.types.INTEGER,
          "scientific_name": sqlalchemy.types.String(length=300),
          "common_name": sqlalchemy.types.String(length=300),
          "affected_area": sqlalchemy.types.String(length=50),
          "area_min": sqlalchemy.types.INTEGER,
          "area_max": sqlalchemy.types.INTEGER,
          "type": sqlalchemy.types.String(length=50),
          "protected_status": sqlalchemy.types.String(length=25),
          "migratory_status ": sqlalchemy.types.String(length=25),
          "location": sqlalchemy.types.String(length=50),
          "url": sqlalchemy.types.String(length=150),
          "distribution_map": sqlalchemy.types.String(length=150),
          "thumbnail": sqlalchemy.types.String(length=150)
}

# Sending to DB
df.to_sql(name=IMPACT_TABLENAME1,
          con=engine,
          index=False,
          dtype=schema
          )

# Adding primary key to table
engine.execute(f"ALTER TABLE {IMPACT_TABLENAME1} ADD PRIMARY KEY (`taxon_id`)")

## End of animal impact table ###


IMPACT_TABLENAME2 = "impact_historic_fires"
engine.execute(f"DROP TABLE IF EXISTS {IMPACT_TABLENAME2}")

df = pd.read_csv("df_hist_fires1.csv").to_sql(
    name=IMPACT_TABLENAME2,
    con=engine,
    index=False,
    dtype={
        "number": sqlalchemy.types.INTEGER,
        "name": sqlalchemy.types.String(length=150),
        "state": sqlalchemy.types.String(length=35),
        "hectacres_burned": sqlalchemy.types.BigInteger(),
        "acres_burned": sqlalchemy.types.BigInteger(),
        "year": sqlalchemy.types.INTEGER(),
        "human_fatalities": sqlalchemy.types.INTEGER(),
        "homes_destroyed": sqlalchemy.types.INTEGER(),},)
engine.execute(f"ALTER TABLE {IMPACT_TABLENAME2} ADD PRIMARY KEY (`number`)"
)

IMPACT_TABLENAME3 = "impact_2019_2020_fires"
engine.execute(f"DROP TABLE IF EXISTS {IMPACT_TABLENAME3}")

df = pd.read_csv("df_2019_2020_fires.csv").to_sql(
    name=IMPACT_TABLENAME3,
    con=engine,
    index=False,
    dtype={
        "number": sqlalchemy.types.INTEGER,
        "year": sqlalchemy.types.INTEGER(),
        "state": sqlalchemy.types.String(length=50),
        "human_fatalities": sqlalchemy.types.INTEGER(),
        "homes_destroyed": sqlalchemy.types.INTEGER(),
        "hectacres_burned": sqlalchemy.types.BigInteger(),
        "acres_burned": sqlalchemy.types.BigInteger(),},)
engine.execute(
    f"ALTER TABLE {IMPACT_TABLENAME3} ADD PRIMARY KEY (`number`)")

IMPACT_TABLENAME4 = "impact_economic"
engine.execute(f"DROP TABLE IF EXISTS {IMPACT_TABLENAME4}")

df = pd.read_csv("aus_economic_data.csv").to_sql(
    name=IMPACT_TABLENAME4,
    con=engine,
    index=False,
    dtype={
        "number": sqlalchemy.types.INTEGER,
        "year": sqlalchemy.types.INTEGER(),
        "gdp_current_us_dol": sqlalchemy.types.INTEGER(),
        "gdp_per_growth_annual": sqlalchemy.types.INTEGER(),
        "domestic_credit_financial_sector_per_gdp": sqlalchemy.types.INTEGER(),
        "domestic_credit_private_sector_banks_per_gdp": sqlalchemy.types.INTEGER(),},)
engine.execute(
    f"ALTER TABLE {IMPACT_TABLENAME4} ADD PRIMARY KEY (`number`)")

IMPACT_TABLENAME5 = "impact_economic_cip"
engine.execute(f"DROP TABLE IF EXISTS {IMPACT_TABLENAME5}")

df = pd.read_csv("aus_cip_data.csv").to_sql(
    name=IMPACT_TABLENAME5,
    con=engine,
    index=False,
    dtype={
        "number": sqlalchemy.types.INTEGER,
        "year": sqlalchemy.types.INTEGER(),
        "new_south_wales_cip": sqlalchemy.types.FLOAT(),
        "victoria_cpi": sqlalchemy.types.FLOAT(),
        "queensland_cpi": sqlalchemy.types.FLOAT(),
        "southern_australia_cpi": sqlalchemy.types.FLOAT(),
        "western_australia_cip": sqlalchemy.types.FLOAT(),
        "tasmania_cpi": sqlalchemy.types.FLOAT(),
        "nothern_territory_cpi": sqlalchemy.types.FLOAT(),
        "australian_capital_territory_cpi": sqlalchemy.types.FLOAT(),},)
engine.execute(
    f"ALTER TABLE {IMPACT_TABLENAME5} ADD PRIMARY KEY (`year`)")



###########################################################
##     Australia Fire Archives table begins here        ###
###########################################################

AUS_FIRES = "aus_fire_history" 
engine.execute(f"DROP TABLE IF EXISTS {AUS_FIRES}")

df = pd.read_csv("aus_fire_locations/australia_rounded.csv").to_sql(
    name = AUS_FIRES,
    con = engine,
    dtype = {'year' : sqlalchemy.types.INTEGER(),'month': sqlalchemy.types.INTEGER()})

engine.execute(f"ALTER TABLE {AUS_FIRES} ADD PRIMARY KEY (`index`)")

AUS_FIRES2 = "agg_fire_maps" 
engine.execute(f"DROP TABLE IF EXISTS {AUS_FIRES2}")

df = pd.read_csv("aus_fire_locations/agg_fire_maps.csv").to_sql(
    name = AUS_FIRES2,
    con = engine,
    dtype = {'year' : sqlalchemy.types.INTEGER(),'count': sqlalchemy.types.INTEGER()})

engine.execute(f"ALTER TABLE {AUS_FIRES2} ADD PRIMARY KEY (`index`)")

###########################################################
##                      *Austin*                        ###
##    Table for Global Fire Map (2019 through 2017)     ###
###########################################################

Creating the MySQL table with each of the cleaned datasets (March 5th, 2020 - > Jan 1st, 2017)
GLOBAL_FIRES_2020_2017 = "g_fires" 
engine.execute(f"DROP TABLE IF EXISTS {GLOBAL_FIRES_2020_2017}")

#2020
chunks = 10000
i = 0
j = 0

for df in pd.read_csv("fd_2020.csv", chunksize=chunks, iterator=True):
    df = df.rename(columns = {c: c.replace(' ', '') for c in df.columns})
    df.index += j

    df.to_sql(
        name = GLOBAL_FIRES_2020_2017,
        con = engine,
        if_exists = 'append'
    )
    
    j = df.index[-1]+1

    print('BUILDING DATA: 2019 (3/5/2019) -> 2020 (3/5/2020) | index: {}'.format(j))

del df
del chunks
del i
del j

# 2019
chunks = 10000
i = 0
j = 0

for df in pd.read_csv("fd_2019.csv", chunksize=chunks, iterator=True):
    df = df.rename(columns = {c: c.replace(' ', '') for c in df.columns})
    df.index += j

    df.to_sql(
        name = GLOBAL_FIRES_2020_2017,
        con = engine,
        if_exists = 'append'
    )
    
    j = df.index[-1]+1

    print('BUILDING DATA: 2018 (3/5/2018) -> 2019 (3/4/2019) | index: {}'.format(j))

del df
del chunks
del i
del j

# 2018
chunks = 10000
i = 0
j = 0

for df in pd.read_csv("fd_2018.csv", chunksize=chunks, iterator=True):
    df = df.rename(columns = {c: c.replace(' ', '') for c in df.columns})
    df.index += j

    df.to_sql(
        name = GLOBAL_FIRES_2020_2017,
        con = engine,
        if_exists = 'append'
    )
    
    j = df.index[-1]+1

    print('BUILDING DATA: 2017 (3/5/2017) -> 2018 (3/4/2018) | index: {}'.format(j))

del df
del chunks
del i
del j

#2017
chunks = 10000
i = 0
j = 0

for df in pd.read_csv("fd_2017.csv", chunksize=chunks, iterator=True):
    df = df.rename(columns = {c: c.replace(' ', '') for c in df.columns})
    df.index += j

    df.to_sql(
        name = GLOBAL_FIRES_2020_2017,
        con = engine,
        if_exists = 'append'
    )
    
    j = df.index[-1]+1

    print('BUILDING DATA: 2017 (1/1/2017) -> 2017 (3/4/2017) | index: {}'.format(j))

del df
del chunks
del i
del j

engine.execute(f"ALTER TABLE {GLOBAL_FIRES_2020_2017} ADD PRIMARY KEY (`index`)")

#################################################################
##    End of Tables for Global Fire Map (2019 through 2017)   ###
#################################################################
