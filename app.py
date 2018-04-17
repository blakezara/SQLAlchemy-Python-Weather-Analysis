# Import Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

from flask import Flask, jsonify
import datetime as dt

engine = create_engine("sqlite:///hawaii.sqlite", echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

# Date
today = dt.date.today()
year = dt.timedelta(days=365)
year_ago = dt.date.today()- year



def calc_temps(start_date, end_date):
    minimum = session.query(func.min(Measurement.tobs)).filter(Measurement.date > start_date)\
                             .filter(Measurement.date < end_date).all()
    maximum = session.query(func.max(Measurement.tobs)).filter(Measurement.date > start_date)\
                             .filter(Measurement.date < end_date).all()
    average = session.query(func.avg(Measurement.tobs)).filter(Measurement.date > start_date)\
                             .filter(Measurement.date < end_date).all()
    return minimum, maximum, average

# create app
app = Flask(__name__)

# define routes and functions

# home
@app.route("/")
def home():
    return (
        f"Welcome to the Hawaiian Weather Center!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"Returns precipitation data for the previous year<br/><br/>"
        f"/api/v1.0/stations<br/>"
        f"Returns a list of weather stations<br/><br/>"
        f"/api/v1.0/tobs<br/>"
        f"Returns observed temperatures from the previous year<br/><br/>"
        f"/api/v1.0/[start]/<br/>"
        f"Returns the minimum, average, and maximum temperatures<br/>"
               
    )

# return precipitation data for previous year
@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > year_ago).all()
    recent_prcp_json = jsonify(dict(results))
    return recent_prcp_json

# return a json list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    results_1 = session.query(Measurement.station, func.count(Measurement.tobs))\
    .group_by(Measurement.station)\
    .order_by(func.count(Measurement.tobs).desc()).all()
    station_list_json = jsonify(results_1)
    return station_list_json

# return a json list of Temperature Observations (tobs) for the previous year
@app.route("/api/v1.0/tobs")
def tobs():
    recent_tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > year_ago).all()
    recent_tobs_json = jsonify(dict(recent_tobs))
    return recent_tobs_json

# return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# cannot get these to run
@app.route("/api/v1.0/<start>/")
def temp_info_start(start_date):
    temp_data = calc_temps(start_date)
    Min, Avg, Max = temp_data[0]
    temp_results = {
        "minimum temperature":Min,
        "average temperature":Avg,
        "maximum temperature":Max
    }
    temp_results_json = jsonify(temp_results)
    return temp_results_json


@app.route("/api/v1.0/<start>/<end>")
def temp_info_start_end(start_date, end_date):
    temp_data = calc_temps(start_date, end_date)
    Min, Avg, Max = temp_data[0]
    temp_results = {
        "minimum temperature":Min,
        "average temperature":Avg,
        "maximum temperature":Max
    }
    temp_results_json = jsonify(temp_results)
    return temp_results_json


if __name__ == "__main__":
    app.run()