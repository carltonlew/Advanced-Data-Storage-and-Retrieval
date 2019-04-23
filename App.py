import pandas as pd 
import numpy as np 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

from flask import Flask, jsonify

# Database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

Station = Base.classes.station 
Measurement = Base.classes.measurement 

# Create a session from python to the DB
session = Session 

# Flask setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def home():
    """List all available api routes"""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

@app.route("/api/v1.0/precipitation")
def pcpt():
    """Query the dates and precipitation amounts for the last year"""
    # Last date read in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    # The date one year before last date in the database
    year_ago = last_date - dt.timedelta(days=365)

# Return a list of dates and precipitation readings
prcp_results = session.query(Measurement.date, func.avg(Measurement.prcp)).filter(Measurement.date>year_ago).\
                group_by(Measurement.date).all()

# Convert the query to a dictionary
results = []
for result in prcp_results:
    all_prcp=list(np.ravel(result))
    date_str = dt.datetime.strftime(all_prcp[0], "%Y-%m-%d")
    pcrp_dict={}
    prcp_dict[date_str] = '{:.4f}'.format(all_prcp[1])
    results.append(results)

return jsonify(results)

@app.route('/api/v1.0/stations')
def stations():
    # Query the station info
    station_results = session.query(Station).all()
# Create a dictionary from station query
stations = []
for station in station_results:
    stat_dict={}
    stat_dict['station'] = station.station
    stat_dict['name'] = station.name
    stat_dict['latitude'] = station.latitude
    stat_dict['longitude'] = station.longitude
    stat_dict['elevation'] = station.elevation
    stations.append(stat_dict)

    return jsonify(stations)

@app.route('/api/v1.0/tobs')
def tobs():
    # Last date read in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    # The date one year before last date in the database
    year_ago = last_date - dt.timedelta(days=365)
Reurn a list of dates and temperature readings
    tobs_results = session.query(Measurement.date, func.avg(Measurement.tobs)).filter(Measurement.date>year_ago).\
    group_by(Measurement.date).all()

Convert the query to a dictionary 
    results = []
    for result in tobs_results
        all_tobs=list(np.ravel(result))
        date_str = dt.datetime.strftime(all_tobs[0], "%Y-%m-%d")
        tobs_dict={}
        tobs_dict['Date'] = date_str
        tobs_dict['Temperature'] = '{:.2f}'.format(all_tobs)
        results.append(tobs_dict)

        return jsonify(results)

        
