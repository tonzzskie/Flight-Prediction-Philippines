from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("c1_flight_rf.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)

        # Departure
        dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)

        # Duration
        Duration_hours = abs(arrival_hour - dep_hour)
        Duration_mins = abs(arrival_min - dep_min)

        # Total Stops
        No_Stops = int(request.form["stops"])

        # Airline Company
        airline = request.form['airline']
        Airline_CebuPacific = 0
        Airline_Other = 0
        Airline_PhilippineAirlines = 0
        Airline_PhilippinesAirAsia = 0

        if airline == 'Cebu Pacific':
            Airline_CebuPacific = 1
        elif airline == 'Philippine Airlines':
            Airline_PhilippineAirlines = 1
        elif airline == 'Philippines AirAsia':
            Airline_PhilippinesAirAsia = 1
        else:
            Airline_Other = 1

        # Source (From)
        Source = request.form["Source"]
        Destination_From_DVO = 0
        Destination_From_MNL = 0
        Destination_From_SUG = 0

        if Source == 'DVO':
            Destination_From_DVO = 1
        elif Source == 'MNL':
            Destination_From_MNL = 1
        elif Source == 'SUG':
            Destination_From_SUG = 1

        # Destination (To)
        Destination = request.form["Destination"]
        Destination_To_DVO = 0
        Destination_To_MNL = 0
        Destination_To_SUG = 0

        if Destination == 'DVO':
            Destination_To_DVO = 1
        elif Destination == 'MNL':
            Destination_To_MNL = 1
        elif Destination == 'SUG':
            Destination_To_SUG = 1

        # Prediction
        prediction = model.predict([[
            No_Stops,
            journey_day,
            journey_month,
            dep_hour,
            dep_min,
            arrival_hour,
            arrival_min,
            Duration_hours,
            Duration_mins,
            Airline_CebuPacific,
            Airline_Other,
            Airline_PhilippineAirlines,
            Airline_PhilippinesAirAsia,
            Destination_From_DVO,
            Destination_From_MNL,
            Destination_From_SUG,
            Destination_To_DVO,
            Destination_To_MNL,
            Destination_To_SUG
        ]])

        output = round(prediction[0], 2)
        return render_template('home.html', prediction_text="Your Flight price is ₱ {}".format(output))

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
