# Import dependencies
from flask import Flask, render_template, jsonify, request, redirect
import sqlalchemy
from sqlalchemy.orm import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Date
import datetime, time
from config import password
import os


# Create an instance of Flask app
app = Flask(__name__)

#####################################################################
#                      Database Connection 			        		    		#
#####################################################################

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_CONN")
db = SQLAlchemy(app)


#####################################################################
#                     DictMixIn Function                            #
#####################################################################

class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(getattr(self, column.name), datetime.datetime)
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }

#####################################################################
#             Classes for Fire Count Tables  		          	      	#
#####################################################################

class NSW_Fire_Counts(db.Model, DictMixIn):
    __tablename__ = "nsw_fire_counts"

    nsw_DOY=db.Column(db.Integer(), primary_key=True)
    nsw_2002_2003=db.Column(db.Integer())
    nsw_2003_2004=db.Column(db.Integer()) 
    nsw_2004_2005=db.Column(db.Integer())
    nsw_2005_2006=db.Column(db.Integer())
    nsw_2006_2007=db.Column(db.Integer())
    nsw_2007_2008=db.Column(db.Integer())
    nsw_2008_2009=db.Column(db.Integer())
    nsw_2009_2010=db.Column(db.Integer())
    nsw_2010_2011=db.Column(db.Integer())
    nsw_2011_2012=db.Column(db.Integer())
    nsw_2012_2013=db.Column(db.Integer())
    nsw_2013_2014=db.Column(db.Integer())
    nsw_2014_2015=db.Column(db.Integer())
    nsw_2015_2016=db.Column(db.Integer())
    nsw_2016_2017=db.Column(db.Integer())
    nsw_2017_2018=db.Column(db.Integer())
    nsw_2018_2019=db.Column(db.Integer())
    nsw_2019_2020=db.Column(db.Integer())
    nsw_month=db.Column(db.String())

class Queensland_Fire_Counts(db.Model, DictMixIn):
    __tablename__ = "queensland_fire_counts"

    queensland_DOY=db.Column(db.Integer(), primary_key=True)
    queensland_2002_2003=db.Column(db.Integer())
    queensland_2003_2004=db.Column(db.Integer())
    queensland_2004_2005=db.Column(db.Integer())
    queensland_2005_2006=db.Column(db.Integer())
    queensland_2006_2007=db.Column(db.Integer())
    queensland_2007_2008=db.Column(db.Integer())
    queensland_2008_2009=db.Column(db.Integer())
    queensland_2009_2010=db.Column(db.Integer())
    queensland_2010_2011=db.Column(db.Integer())
    queensland_2011_2012=db.Column(db.Integer())
    queensland_2012_2013=db.Column(db.Integer())
    queensland_2013_2014=db.Column(db.Integer())
    queensland_2014_2015=db.Column(db.Integer())
    queensland_2015_2016=db.Column(db.Integer())
    queensland_2016_2017=db.Column(db.Integer())
    queensland_2017_2018=db.Column(db.Integer())
    queensland_2018_2019=db.Column(db.Integer())
    queensland_2019_2020=db.Column(db.Integer())
    queensland_month=db.Column(db.String())


class Victoria_Fire_Counts(db.Model, DictMixIn):
    __tablename__ = "victoria_fire_counts"

    victoria_DOY=db.Column(db.Integer(), primary_key=True)
    victoria_2002_2003=db.Column(db.Integer())
    victoria_2003_2004=db.Column(db.Integer())
    victoria_2004_2005=db.Column(db.Integer())
    victoria_2005_2006=db.Column(db.Integer())
    victoria_2006_2007=db.Column(db.Integer())
    victoria_2007_2008=db.Column(db.Integer())
    victoria_2008_2009=db.Column(db.Integer())
    victoria_2009_2010=db.Column(db.Integer())
    victoria_2010_2011=db.Column(db.Integer())
    victoria_2011_2012=db.Column(db.Integer())
    victoria_2012_2013=db.Column(db.Integer())
    victoria_2013_2014=db.Column(db.Integer())
    victoria_2014_2015=db.Column(db.Integer())
    victoria_2015_2016=db.Column(db.Integer())
    victoria_2016_2017=db.Column(db.Integer())
    victoria_2017_2018=db.Column(db.Integer())
    victoria_2018_2019=db.Column(db.Integer())
    victoria_2019_2020=db.Column(db.Integer())
    victoria_month=db.Column(db.String())

class NSW_Annual_Total_Fire_Counts(db.Model, DictMixIn):
	__tablename__ = "nsw_annual_total_fire_counts"

	nsw_fire_year=db.Column(db.String(), primary_key=True)
	nsw_total_fires=db.Column(db.Integer())

class Queensland_Annual_Total_Fire_Counts(db.Model, DictMixIn):
	__tablename__ = "queensland_annual_total_fire_counts"

	queensland_fire_year=db.Column(db.String(), primary_key=True)
	queensland_total_fires=db.Column(db.Integer())

class Victoria_Annual_Total_Fire_Counts(db.Model, DictMixIn):
	__tablename__ = "victoria_annual_total_fire_counts"

	victoria_fire_year=db.Column(db.String(), primary_key=True)
	victoria_total_fires=db.Column(db.Integer())  

#####################################################################
# Classes for Climate and Greenhouse Gases/Air Pollutant Tables     #
#####################################################################

class AUS_Max_Temp_Anomaly_Data(db.Model, DictMixIn):
    __tablename__ = "aus_max_temp_anomaly_data"

    max_temp_anomaly_year=db.Column(db.Integer(), primary_key=True)
    max_temp_anomaly_celcius=db.Column(db.Float())

class AUS_Min_Temp_Anomaly_Data(db.Model, DictMixIn):
    __tablename__ = "aus_min_temp_anomaly_data"

    min_temp_anomaly_year=db.Column(db.Integer(), primary_key=True)
    min_temp_anomaly_celcius=db.Column(db.Float())

class AUS_Mean_Temp_Anomaly_Data(db.Model, DictMixIn):
    __tablename__ = "aus_mean_temp_anomaly_data"

    mean_temp_anomaly_year=db.Column(db.Integer(), primary_key=True)
    mean_temp_anomaly_celcius=db.Column(db.Float())

class AUS_Annual_Rainfall_Data(db.Model, DictMixIn):
    __tablename__ = "aus_annual_rainfall_data"

    annual_rainfall_year=db.Column(db.Integer(), primary_key=True)
    annual_rainfall_mm=db.Column(db.Float())

class AUS_Annual_Rainfall_Anomaly_Data(db.Model, DictMixIn):
    __tablename__ = "aus_annual_rainfall_anomaly_data"

    annual_rainfall_anomaly_year=db.Column(db.Integer(), primary_key=True)
    annual_rainfall_anomaly_mm=db.Column(db.Float())

class AUS_Sea_Surface_Temp_Anomaly_Data(db.Model, DictMixIn):
    __tablename__ = "aus_sea_surface_temp_anomaly_data"

    sea_surface_temp_anomaly_year=db.Column(db.Integer(), primary_key=True)
    sea_surface_temp_anomaly_celcius=db.Column(db.Float())

class AUS_Air_Pollutants_Combined_Data(db.Model, DictMixIn):
    __tablename__ = "aus_air_pollutants_combined_data"

    air_pollutant_year=db.Column(db.Integer(), primary_key=True)
    CO2_ppm=db.Column(db.Float())
    CH4_ppb=db.Column(db.Float())
    N2O_ppb=db.Column(db.Float())

class AUS_Max_Temp_Area_Decile10(db.Model, DictMixIn):
    __tablename__ = "aus_max_temp_area_decile10"

    max_temp_decile10_year=db.Column(db.Integer(), primary_key=True)
    maxtemp_total_land_area_percentage=db.Column(db.Float())

class AUS_Annual_Rainfall_Area_Decile10(db.Model, DictMixIn):
    __tablename__ = "aus_annual_rainfall_area_decile10"

    annual_rainfall_decile10_year=db.Column(db.Integer(), primary_key=True)
    rainfall_total_land_area_percentage=db.Column(db.Float())

#####################################################################
#           Classes for Australia Fire Archive Tables               #
#####################################################################

class aus_fire_history(db.Model, DictMixIn):
    __tablename__ = "aus_fire_history"

    index = db.Column(db.Integer(), primary_key = True)
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    bright_ti4 = db.Column(db.Float())
    scan = db.Column(db.Float())
    track = db.Column(db.Float())
    acq_date = db.Column(db.Date)
    confidence = db.Column(db.String())
    bright_ti5 = db.Column(db.Float())
    frp = db.Column(db.Float())

#####################################################################
#           Classes for Protected Species Impact Table              #
#####################################################################

class ProtectedSpecies(db.Model, DictMixIn):
    __tablename__ = "protected_species_impact"

    taxon_id = db.Column(db.Integer(), primary_key=True)
    scientific_name = db.Column(db.String())
    common_name = db.Column(db.String())
    afected_area = db.Column(db.String())
    area_min = db.Column(db.Integer())
    area_max = db.Column(db.Integer())
    type = db.Column(db.String())
    protected_status = db.Column(db.String())
    migratory_status = db.Column(db.String())
    location = db.Column(db.String())
    url = db.Column(db.String())
    distribution_map = db.Column(db.String())
    thumbnail = db.Column(db.String())

#####################################################################
#                 Economic/Fire Impact Table                        #
#####################################################################
class HistoricFires(db.Model, DictMixIn):
    __tablename__ = "historic_fires_impact"

    taxon_id = db.Column(db.Integer(), primary_key=True)
    scientific_name = db.Column(db.String())
    common_name = db.Column(db.String())
    afected_area = db.Column(db.String())


# TEAM: KEEP ADDING YOUR CLASSES HERE:



# NO TOUCH
db.session.commit()



#####################################################################
#                        __FLASK ROUTES__                           #
#####################################################################


#####################################################################
#                             Home Page					         	        	#
#####################################################################

@app.route("/")
def index():
    return render_template("index.html")


#####################################################################
#                 Australia Fire Locations  		                    #
#####################################################################

@app.route("/aus_fire_history_page.html")
def load_aus_fire_locations():
    return render_template("aus_fire_history_page.html")

@app.route("/aus_fire_history")
def load_aus_fire_locations_data():

	combined_aus_fire_history = []	

	fire_archives = aus_fire_history.query.all()

	for result in fire_archives:
		combined_aus_fire_history.append(result.to_dict())

	return jsonify(combined_aus_fire_history)
  
#####################################################################
#                    Fire Counts Page and Route 	                	#
#####################################################################

@app.route("/fire_count_page")
def fire_count_page():
	return render_template("fire-count.html")


@app.route("/fire_count")
def fire_count():

	combined_fire_count_list = []	

	nsw_results = NSW_Fire_Counts.query.all()
	for result in nsw_results:
		combined_fire_count_list.append(result.to_dict())

	queensland_results = Queensland_Fire_Counts.query.all()
	for result in queensland_results:
		combined_fire_count_list.append(result.to_dict())

	victoria_results = Victoria_Fire_Counts.query.all()
	for result in victoria_results:
		combined_fire_count_list.append(result.to_dict())

	return jsonify(combined_fire_count_list)


@app.route("/annual_total_fire_counts")
def annual_total_fire_counts():

	combined_total_fire_list = []

	nsw_results = NSW_Annual_Total_Fire_Counts.query.all()
	for result in nsw_results:
		combined_total_fire_list.append(result.to_dict())

	queensland_results = Queensland_Annual_Total_Fire_Counts.query.all()
	for result in queensland_results:
		combined_total_fire_list.append(result.to_dict())

	victoria_results = Victoria_Annual_Total_Fire_Counts.query.all()
	for result in victoria_results:
		combined_total_fire_list.append(result.to_dict())

	return jsonify(combined_total_fire_list)


########################################################################################
#                        API search string for total fire counts                       #
#  Ex: http://127.0.0.1:5000/total_firecounts_search_type?state=nsw&year=2002/2003     #
########################################################################################

@app.route("/total_firecounts_search_type")
def total_firecounts_search_type():

    # search type parameters - state and/or year
    request_state = request.args.get("state")
    request_year = request.args.get("year")

    combined_total_fire_list = []
    data = []

    try:
        nsw_results = NSW_Annual_Total_Fire_Counts.query.all()
        for result in nsw_results:
            combined_total_fire_list.append(result.to_dict())

        queensland_results = Queensland_Annual_Total_Fire_Counts.query.all()
        for result in queensland_results:
            combined_total_fire_list.append(result.to_dict())

        victoria_results = Victoria_Annual_Total_Fire_Counts.query.all()
        for result in victoria_results:
            combined_total_fire_list.append(result.to_dict())

        # if no search parameter is entered then return entire fire-count dataset
        if (not request_state) and (not request_year):
            return jsonify(combined_total_fire_list)

        # if search parameter (endpoint) is entered then use the state and year filters to return the results
        if request_state and request_year:

            if request_state.lower() == "nsw" or request_state.lower() == "new south wales":
                for row in nsw_results:
                    if request_year == row.to_dict()["nsw_fire_year"]:
                        data.append(row.to_dict())
   
            elif request_state.lower() == "queensland":
                for row in queensland_results:
                    if request_year == row.to_dict()["queensland_fire_year"]:
                        data.append(row.to_dict())
                                          
            elif request_state.lower() == "victoria":
                for row in victoria_results:
                    if request_year == row.to_dict()["victoria_fire_year"]:
                        data.append(row.to_dict())
            else:
                return ""

            return jsonify(data)

        # request for total-fire-count data based on state filter only
        if request_state and (not request_year):

            if request_state.lower() == "nsw" or request_state.lower() == "new south wales":
                return jsonify([row.to_dict() for row in nsw_results])
            elif request_state.lower() == "queensland":
                return jsonify([row.to_dict() for row in queensland_results])
            elif request_state.lower() == "victoria":
                return jsonify([row.to_dict() for row in victoria_results])
            else:
                return ""

        # request for total-fire-count data based on year filter only     
        if request_year and (not request_state):

            for row in nsw_results:
                if request_year == row.to_dict()["nsw_fire_year"]:
                    data.append(row.to_dict())

            for row in queensland_results:
                if request_year == row.to_dict()["queensland_fire_year"]:
                    data.append(row.to_dict()) 

            for row in victoria_results:
                if request_year == row.to_dict()["victoria_fire_year"]:
                    data.append(row.to_dict())  
   
            return jsonify(data)


    except Exception as e:
        return jsonify({"status": "failure", "error": str(e)})


#####################################################################
#                          Impact Route                             #
#####################################################################

@app.route("/impact")
def impact():

    data = ProtectedSpecies.query.all()

    impact_list = [e.to_dict() for e in data]

    return render_template("impact.html", data=impact_list)


@app.route("/econ_impact")
def econ_impact():
    human_econ_impact = [] 

    impact_historic_fires = IMPACT_TABLENAME2.query.all()
    for result in impact_historic_fires:
        human_econ_impact_data.append(result.to_dict()) 
    
    impact_2019_fires = IMPACT_TABLENAME3.query.all()
    for result in impact_2019_fires:
        human_econ_impact_data.append(result.to_dict())
    
    impact_economic = IMPACT_TABLENAME4.query.all()
    for result in impact_economic:
        human_econ_impact_data.append(result.to_dict())
    
    impact_consumer = IMPACT_TABLENAME5.query.all()
    for result in impact_economic:
        human_econ_impact_data.append(result.to_dict())
    return render_template("impact.html", x=human_econ_impact)

  
#####################################################################
#                 Climate Fails Page and Route		                  #
#####################################################################

@app.route("/climate_fails_page")
def climate_fails():
	return render_template("climate-fails.html")

@app.route("/climate_data")
def climate_data():

    combined_climate_list = []  

    max_temp_results = AUS_Max_Temp_Anomaly_Data.query.all()
    for result in max_temp_results:
        combined_climate_list.append(result.to_dict()) 

    max_temp_results = AUS_Max_Temp_Anomaly_Data.query.all()
    for result in max_temp_results:
        combined_climate_list.append(result.to_dict())

    min_temp_results = AUS_Min_Temp_Anomaly_Data.query.all()
    for result in min_temp_results:
        combined_climate_list.append(result.to_dict())

    mean_temp_results = AUS_Mean_Temp_Anomaly_Data.query.all()
    for result in mean_temp_results:
        combined_climate_list.append(result.to_dict())

    annual_rainfall_results = AUS_Annual_Rainfall_Data.query.all()
    for result in annual_rainfall_results:
        combined_climate_list.append(result.to_dict())

    rainfall_anomaly_results = AUS_Annual_Rainfall_Anomaly_Data.query.all()
    for result in rainfall_anomaly_results:
        combined_climate_list.append(result.to_dict())  

    sst_anomaly_results = AUS_Sea_Surface_Temp_Anomaly_Data.query.all()
    for result in sst_anomaly_results:
        combined_climate_list.append(result.to_dict())    

    max_temp_decile10_area_results = AUS_Max_Temp_Area_Decile10.query.all()
    for result in max_temp_decile10_area_results:
        combined_climate_list.append(result.to_dict())

    annual_rainfall_area_decile10 = AUS_Annual_Rainfall_Area_Decile10.query.all()
    for result in annual_rainfall_area_decile10:
        combined_climate_list.append(result.to_dict())

    return jsonify(combined_climate_list)


@app.route("/air_pollutant_data")
def air_pollutant_data():

    combined_air_pollutant_list = []   

    air_pollutant_results = AUS_Air_Pollutants_Combined_Data.query.all()
    for result in air_pollutant_results:
        combined_air_pollutant_list.append(result.to_dict())

    return jsonify(combined_air_pollutant_list)


########################################################################################
#            API search string for climate and greenhouse gases/air data               #
#  Ex: http://127.0.0.1:5000/climate_data_search_type?weather-type=max-temp            #
########################################################################################

@app.route("/climate_data_search_type")
def climate_data_search_type():

    # search type parameter - weather type. Refer the API documentation on About Page for more on weather parameters.
    request_weather_type = request.args.get("weather-type")
  
    combined_climate_list = []  
    combined_climate_list_default = []  

    try:
        # if no search criteria is entered then return the entire climate & gases dataset
        if not request_weather_type:

            max_temp_results = AUS_Max_Temp_Anomaly_Data.query.all()
            for result in max_temp_results:
                combined_climate_list_default.append(result.to_dict())

            min_temp_results = AUS_Min_Temp_Anomaly_Data.query.all()
            for result in min_temp_results:
                combined_climate_list_default.append(result.to_dict())

            mean_temp_results = AUS_Mean_Temp_Anomaly_Data.query.all()
            for result in mean_temp_results:
                combined_climate_list_default.append(result.to_dict())

            annual_rainfall_results = AUS_Annual_Rainfall_Data.query.all()
            for result in annual_rainfall_results:
                combined_climate_list_default.append(result.to_dict())

            rainfall_anomaly_results = AUS_Annual_Rainfall_Anomaly_Data.query.all()
            for result in rainfall_anomaly_results:
                combined_climate_list_default.append(result.to_dict())  

            sst_anomaly_results = AUS_Sea_Surface_Temp_Anomaly_Data.query.all()
            for result in sst_anomaly_results:
                combined_climate_list_default.append(result.to_dict())    

            max_temp_decile10_area_results = AUS_Max_Temp_Area_Decile10.query.all()
            for result in max_temp_decile10_area_results:
                combined_climate_list_default.append(result.to_dict())

            annual_rainfall_area_decile10 = AUS_Annual_Rainfall_Area_Decile10.query.all()
            for result in annual_rainfall_area_decile10:
                combined_climate_list_default.append(result.to_dict())

            air_pollutant_results = AUS_Air_Pollutants_Combined_Data.query.all()
            for result in air_pollutant_results:
                combined_climate_list_default.append(result.to_dict())

            return jsonify(combined_climate_list_default)      
              
        # if search criteria (endpoint) is entered then use the search criteria as a filter to return the results
        if request_weather_type.lower() == "max-temp-anomaly":
            max_temp_results = AUS_Max_Temp_Anomaly_Data.query.all()
            for result in max_temp_results:
                combined_climate_list.append(result.to_dict())

        elif request_weather_type.lower() == "min-temp-anomaly":
            min_temp_results = AUS_Min_Temp_Anomaly_Data.query.all()
            for result in min_temp_results:
                combined_climate_list.append(result.to_dict())       

        elif request_weather_type.lower() == "mean-temp-anomaly":
            mean_temp_results = AUS_Mean_Temp_Anomaly_Data.query.all()
            for result in mean_temp_results:
                combined_climate_list.append(result.to_dict())

        elif request_weather_type.lower() == "annual-rainfall":
            annual_rainfall_results = AUS_Annual_Rainfall_Data.query.all()
            for result in annual_rainfall_results:
                combined_climate_list.append(result.to_dict())

        elif request_weather_type.lower() == "rainfall-anomaly":
            rainfall_anomaly_results = AUS_Annual_Rainfall_Anomaly_Data.query.all()
            for result in rainfall_anomaly_results:
                combined_climate_list.append(result.to_dict())  

        elif request_weather_type.lower() == "sst-anomaly":
            sst_anomaly_results = AUS_Sea_Surface_Temp_Anomaly_Data.query.all()
            for result in sst_anomaly_results:
                combined_climate_list.append(result.to_dict())    

        elif request_weather_type.lower() == "max-temp-decile10":
            max_temp_decile10_area_results = AUS_Max_Temp_Area_Decile10.query.all()
            for result in max_temp_decile10_area_results:
                combined_climate_list.append(result.to_dict())

        elif request_weather_type.lower() == "annual-rainfall-decile10":
            annual_rainfall_area_decile10 = AUS_Annual_Rainfall_Area_Decile10.query.all()
            for result in annual_rainfall_area_decile10:
                combined_climate_list.append(result.to_dict())

        elif request_weather_type.lower() == "gases":
            air_pollutant_results = AUS_Air_Pollutants_Combined_Data.query.all()
            for result in air_pollutant_results:
                combined_climate_list.append(result.to_dict())

        return jsonify(combined_climate_list)


    except Exception as e:
        return jsonify({"status": "failure", "error": str(e)})




#####################################################################
#                            Main		     			                  		#
#####################################################################

if __name__ == "__main__":
    app.run(debug=True)
