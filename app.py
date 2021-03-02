# Import everything you used in the starter_climate_analysis.ipynb file, along with Flask modules
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask


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
    return  "Welcome to the Climate App! It's so much fun to learn about the Climate, isn't it?"

# Set the app.route() decorator for the "/api/v1.0/precipitation" route
@app.route("/api/v1.0/precipitation")
# define a precipitation() function that returns jsonified precipitation data from the database
def precipitation():
    return 
# In the function (logic should be the same from the starter_climate_analysis.ipynb notebook):
    # Calculate the date 1 year ago from last date in database

    # Query for the date and precipitation for the last year

    # Create a dictionary to store the date: prcp pairs. 
    # Hint: check out a dictionary comprehension, which is similar to a list comprehension but allows you to create dictionaries
    
    # Return the jsonify() representation of the dictionary
    
# Set the app.route() decorator for the "/api/v1.0/stations" route
@app.route("/api/v1.0/stations")
# define a stations() function that returns jsonified station data from the database
def stations():
    return
# In the function (logic should be the same from the starter_climate_analysis.ipynb notebook):
    # Query for the list of stations

    # Unravel results into a 1D array and convert to a list
    # Hint: checkout the np.ravel() function to make it easier to convert to a list
    
    # Return the jsonify() representation of the list


# Set the app.route() decorator for the "/api/v1.0/tobs" route
@app.route("/api/v1.0/tobs")
# define a temp_monthly() function that returns jsonified temperature observations (tobs) data from the database
def temp_monthly():
    return
# In the function (logic should be the same from the starter_climate_analysis.ipynb notebook):
    # Calculate the date 1 year ago from last date in database

    # Query the primary station for all tobs from the last year
    
    # Unravel results into a 1D array and convert to a list
    # Hint: checkout the np.ravel() function to make it easier to convert to a list
    
    # Return the jsonify() representation of the list


# Set the app.route() decorator for the "/api/v1.0/temp/<start>" route and "/api/v1.0/temp/<start>/<end>" route
# define a stats() function that takes a start and end argument, and returns jsonified TMIN, TAVG, TMAX data from the database
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # If the end argument is None:
        # calculate TMIN, TAVG, TMAX for dates greater than start
        
        # Unravel results into a 1D array and convert to a list
        # Hint: checkout the np.ravel() function to make it easier to convert to a list
    
        # Return the jsonify() representation of the list

    # Else:
        # calculate TMIN, TAVG, TMAX with both start and stop
        
        # Unravel results into a 1D array and convert to a list
        # Hint: checkout the np.ravel() function to make it easier to convert to a list
    
        # Return the jsonify() representation of the list


if __name__ == '__main__':
    app.run()
