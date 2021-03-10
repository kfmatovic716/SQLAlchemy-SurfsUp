# Import everything you used in the starter_climate_analysis.ipynb file, along with Flask modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# Create an engine
engine = create_engine("sqlite:///data/hawaii.sqlite")

# reflect an existing database into a new model with automap_base() and Base.prepare()
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Instantiate a Session and bind it to the engine
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################
# Instantiate a Flask object at __name__, and save it to a variable called app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Set the app.route() decorator for the base '/'
@app.route("/")
# define a welcome() function that returns a multiline string message to anyone who visits the route
def welcome():
    return  (
        f"Welcome to the Climate API!<br/>"
        f"<br/>"
        f"<br/>"
        f"The following climate-related API's are available in this site:<br/>"
        f"<br/>"
        f"> Precipitation<br/>"
        f"> List of Stations<br/>"
        f"> Temperature Observations<br/>"
    )

# Set the app.route() decorator for the "/api/v1.0/precipitation" route
@app.route("/api/v1.0/precipitation")

# define a precipitation() function that returns jsonified precipitation data from the database
def precipitation():

    session = Session(engine)

    # Calculate the date 1 year ago from last date in database
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    # Query for the date and precipitation for the last year
    prev_yr_prcp = session.query(Measurement.date, Measurement.prcp).\
                        filter(Measurement.date>= prev_year).\
                        order_by(Measurement.date.asc()).all()

    session.close()

    # Create a dictionary to store the date: prcp pairs. 
    prcp_pairs = []
    for date, prcp in prev_yr_prcp:
        dict_row = {}
        dict_row["date"] = date
        dict_row["prcp"] = prcp
        prcp_pairs.append(dict_row)

    # Return the jsonify() representation of the dictionary
    return jsonify(prcp_pairs)
    
    
# Set the app.route() decorator for the "/api/v1.0/stations" route
@app.route("/api/v1.0/stations")

# define a stations() function that returns jsonified station data from the database
def stations():

    session = Session(engine)

    # Query for the list of stations
    stations_all = session.query(Station.station, Station.name).\
                           group_by(Station.station).all()

    session.close()

    # Unravel results into a 1D array and convert to a list
    # Hint: checkout the np.ravel() function to make it easier to convert to a list
    list_stations = list(np.ravel(stations_all))

    # Return the jsonify() representation of the list
    return jsonify(list_stations)


# Set the app.route() decorator for the "/api/v1.0/tobs" route
@app.route("/api/v1.0/tobs")

# define a temp_monthly() function that returns jsonified temperature observations (tobs) data from the database
def temp_monthly():

    session = Session(engine)

    # Calculate the date 1 year ago from last date in database

    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365) 

    # Query the primary station for all tobs from the last year
    temperature = session.query(Measurement.date, Measurement.tobs).\
                            filter(Measurement.date >= prev_year).\
                            order_by(Measurement.date.asc()).all()

    session.close()

    # Unravel results into a 1D array and convert to a list
    # Hint: checkout the np.ravel() function to make it easier to convert to a list
    temp_list = list(np.ravel(temperature))

    # Return the jsonify() representation of the list
    return jsonify(temp_list)


# Set the app.route() decorator for the "/api/v1.0/temp/<start>" route
@app.route("/api/v1.0/temp/<start>")

# Set the app.route() decorator for the"/api/v1.0/temp/<start>/<end>" route
@app.route("/api/v1.0/temp/<start>/<end>")

# define a stats() function that takes a start and end argument, and returns jsonified TMIN, TAVG, TMAX data from the database
def stats(start=None, end=None):

    session = Session(engine)

    #calculate min, avg and max if no end date
    if end == None:
        # calculate TMIN, TAVG, TMAX for dates greater than start
        aggregates = func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)
        temp_data = session.query(*aggregates).filter(Measurement.date >= start).all()

    
        # Unravel results into a 1D array and convert to a list
        temp_data_list = list(np.ravel(temp_data))
        # Return the jsonify() representation of the list
        return jsonify(temp_data_list)

    else:
        # calculate TMIN, TAVG, TMAX with both start and end
        aggregates = func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)
        temp_data = session.query(*aggregates).\
                    filter(Measurement.date >= start).\
                    filter(Measurement.date <= end).all()

        # Unravel results into a 1D array and convert to a list
        temp_data_list = list(np.ravel(temp_data))

        # Return the jsonify() representation of the list
        return jsonify(temp_data_list)

    session.close()

if __name__ == '__main__':
    app.run()
