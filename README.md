# SQLAlchemy-SurfsUp

### Overview 

    > Data exploration of temperature and temperature stations in Hawaii using SQL Alchemy ORM queries, Pandas and Matplotlib. Climate date in Hawaii is stored in sqlite database.

    > This climate analysis will benefit you if you are planning a trip to Hawaii. There are 3 different parts in this analysis:

        > Climate Analysis and Exploration
        > Climate App using Flask
        > Temperature Analysis

#### Climate Analysis and Exploration

    > Used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database

    > Used SQLAlchemy `create_engine` to connect to sqlite database

    > Used SQLAlchemy `automap_base()` to reflect tables into classes and saved a reference to those classes called `Station` and `Measurement`

    > Analyzed precipitation in the last 12 months, generated statistics using Pandas dataframe and graphed precipitation data

    > Analyzed station locations and temperature observation counts in the last 12 months, generated a histogram to plot the station with highest number of observations

#### Climate App using Flask

    > Designed a Flask API based on the queries that were developed
    > Available routes:
        > / - home route and shows all available routes

        > /api/v1.0/precipitation - queries the database retrieving the las 12 monthgs of precipitation data returning results in JSON format of a dictionary using `date` as the key and `prcp` as the value

        > /api/v1.0/stations - returns a list of stations

        > /api/v1.0/tobs - queries dates and temperature observations for the most active station and returning list of temperature observation in JSON format
        
        > /api/v1.0/<start> - given only a start date, the endpoint calculates the minimum, average, and maximum temperature for all dates greater than or equal to the start date and returns results in a JSON format

        > /api/v1.0/<start>/<end> - given both start and end date, the endpoint calculates the minimum, average, and maximum temperature for dates between the start and end date and returns reults in JSON format

#### Temperature Analysis

    > A function called `calc_temps` is created and will accept a start date and end date. The function will return the minimum, average, and maximum temperatures for the range of dates entered by the user. The dates should be entered in "YYYY-MM-DD" format.

    > Use this function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

    > Used Matplotlib to generate bar chart of min, avg, and max temperature
        > use average temperature as the bar height
        > Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR)


