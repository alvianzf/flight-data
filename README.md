# Documentation for Flight Data Processing and Integration with Flask

**Technologies and Libraries**

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5.3-red.svg)](https://spark.apache.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-green.svg)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13.x-blue.svg)](https://www.postgresql.org/)
[![pip](https://img.shields.io/badge/pip-21.x-blue.svg)](https://pip.pypa.io/)


**Overview**

This project is designed to process and integrate flight data using Flask and Apache Spark. It involves loading JSON files containing flight data, cleaning and transforming the data, analyzing delayed flights, and storing the processed data in a Flask-SQLAlchemy database. The project also includes an API endpoint to retrieve flight data.

**Problem Statement**

The goal is to create a system that can efficiently process large amounts of flight data, identify delayed flights, and provide a user-friendly interface to access this information.

**Steps to Run the Project**

1. **Install Requirements**: Ensure all dependencies are installed by running `pip install -r requirements.txt` in the project directory.
2. **Configure Database**: Update `app.py` with the correct PostgreSQL database URI in the `app.config['SQLALCHEMY_DATABASE_URI']` line.
3. **Run the Flask App**: Execute `python app.py` to start the Flask application.
4. **Process Data**: Send a GET request to `/process-data` to initiate the data processing and integration process.
5. **Retrieve Flight Data**: Send a GET request to `/api/flight-data` to retrieve processed flight data.

**How to Install Dependencies**

1. **Python**: Ensure Python 3.x is installed on your system.
2. **pip**: The Python package manager, pip, is required to install project dependencies.
3. **Apache Spark**: Apache Spark is required for data processing. Follow the installation instructions for your operating system on the Apache Spark website.
4. **PostgreSQL**: A PostgreSQL database is required for storing processed data. Follow the installation instructions for your operating system on the PostgreSQL website.
5. **pip install**: Run `pip install -r requirements.txt` in the project directory to install all project dependencies.

**Data Processing Steps**

1. **Initialize Spark Session**: This is done in the `process_flight_data` function in `app.py`.
2. **Load JSON Files**: The JSON files are loaded using the `spark.read.json` function in `app.py`.
3. **Data Cleaning and Transformation**: The data is cleaned and transformed in the `process_flight_data` function in `app.py`.
4. **Delayed Flights Analysis**: The number of delayed flights is calculated in the `process_flight_data` function in `app.py`.
5. **Store Processed Data**: The processed data is stored in the Flask-SQLAlchemy database in the `process_flight_data` function in `app.py`.

**API Response Documentation**

The API endpoint `/process-data` returns a JSON object with the following keys:
- `message`: A string indicating the status of the data processing. It will be "Data processing completed" if the processing was successful.
- `total_delayed_flights`: An integer indicating the total number of delayed flights in the processed data.

The API endpoint `/api/flight-data` returns a JSON object with a single key:
- `flights`: A list of flight data. Each flight data is a dictionary with the following keys:
  - `carrier_iata`: The IATA code of the carrier.
  - `flight_number`: The flight number.
  - `departure_airport`: The IATA code of the departure airport.
  - `arrival_airport`: The IATA code of the arrival airport.
  - `status_details`: The details of the flight status.

**API Response Format (JSON)**

**/process-data**
```json
{
  "message": "Data processing completed",
  "total_delayed_flights": 10
}
```

**/api/flight-data**
```json
{
  "flights": [
    {
      "carrier_iata": "AA",
      "flight_number": "1234",
      "departure_airport": "JFK",
      "arrival_airport": "LAX",
      "status_details": "On Time"
    },
    {
      "carrier_iata": "UA",
      "flight_number": "5678",
      "departure_airport": "SFO",
      "arrival_airport": "ORD",
      "status_details": "Delayed"
    }
  ]
}
```

**Troubleshooting**

* Ensure all dependencies are installed correctly.
* Verify the PostgreSQL database URI is correct and the database is running.
* Check the Apache Spark installation and ensure it is properly configured.
* If encountering issues with data processing, verify the JSON file paths and formats are correct.
