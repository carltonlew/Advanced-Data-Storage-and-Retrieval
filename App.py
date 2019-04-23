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


