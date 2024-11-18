from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FlightData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carrier_iata = db.Column(db.String(10), nullable=False)
    flight_number = db.Column(db.String(10), nullable=False)
    departure_airport = db.Column(db.String(10), nullable=False)
    arrival_airport = db.Column(db.String(10), nullable=False)
    status_details = db.Column(db.Text, nullable=True)

class ADSBData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight = db.Column(db.String(20), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    altitude = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    last_update = db.Column(db.Integer, nullable=False)