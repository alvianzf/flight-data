# Step 1: Data Processing and Integration with Flask
from flask import Flask, jsonify
from pyspark.sql import SparkSession
from models import db, FlightData, ADSBData  # Assuming Flask-SQLAlchemy models are defined

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/flightdb'
db.init_app(app)

@app.route('/process-data', methods=['GET'])
def process_flight_data():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("Flight Data Processing") \
        .getOrCreate()

    # Load JSON files
    oag_df = spark.read.json("/path/to/oag_multiple.json")
    adsb_df = spark.read.json("/path/to/adsb_multi_aircraft.json")

    # Data cleaning and transformation
    flights_df = oag_df.select("carrier.iata", "flightNumber", "departure.airport.iata", "arrival.airport.iata", "statusDetails")
    adsb_df = adsb_df.select("Flight", "Latitude", "Longitude", "Altitude", "Speed", "LastUpdate")

    # Analysis: Calculate delayed flights
    delayed_flights = oag_df.filter(oag_df.statusDetails.state == "Delayed").count()

    # Store processed data in Flask-SQLAlchemy Database
    for row in flights_df.collect():
        flight_data = FlightData(
            carrier_iata=row["iata"],
            flight_number=row["flightNumber"],
            departure_airport=row["departure.airport.iata"],
            arrival_airport=row["arrival.airport.iata"],
            status_details=str(row["statusDetails"])
        )
        db.session.add(flight_data)

    for row in adsb_df.collect():
        adsb_data = ADSBData(
            flight=row["Flight"],
            latitude=row["Latitude"],
            longitude=row["Longitude"],
            altitude=row["Altitude"],
            speed=row["Speed"],
            last_update=row["LastUpdate"]
        )
        db.session.add(adsb_data)

    db.session.commit()
    spark.stop()

    return jsonify({"message": "Data processing completed", "total_delayed_flights": delayed_flights})

@app.route('/api/flight-data', methods=['GET'])
def get_flight_data():
    flight_data = FlightData.query.all()
    results = [{
        "carrier_iata": data.carrier_iata,
        "flight_number": data.flight_number,
        "departure_airport": data.departure_airport,
        "arrival_airport": data.arrival_airport,
        "status_details": data.status_details
    } for data in flight_data]

    return jsonify({"flights": results})

if __name__ == '__main__':
    app.run(debug=True)
