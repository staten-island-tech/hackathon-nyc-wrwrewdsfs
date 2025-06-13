from flask import Flask, render_template
import requests

app = Flask(__name__)

DATA_URL = "https://data.cityofnewyork.us/resource/h9gi-nx95.json?$limit=100"  # limit to prevent overload

@app.route("/")
def show_route():
    response = requests.get(DATA_URL)
    if response.status_code != 200:
        return "Failed to fetch trips", 500

    trips = response.json()
    return render_template("index.html", trips=trips)

@app.route("/vehicles/<vehicle_type>")
def vehicle_type_details(vehicle_type):
    response = requests.get(DATA_URL)
    if response.status_code != 200:
        return "Failed to fetch data", 500

    crashes = response.json()
    matches = [
        crash for crash in crashes
        if crash.get("vehicle_type_code1", "").lower() == vehicle_type.lower()
    ]
    return render_template("items.html", vehicle_type=vehicle_type, crashes=matches)

if __name__ == "__main__":
    app.run(debug=True)
