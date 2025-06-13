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

@app.route("/routes/<vendorid>")
def route_details(vendorid):
    response = requests.get(DATA_URL)
    if response.status_code != 200:
        return "Failed to fetch trips", 500

    trips = response.json()
    matches = [trip for trip in trips if trip.get("vendorid") == vendorid]
    return render_template("items.html", vendorid=vendorid, trips=matches)

if __name__ == "__main__":
    app.run(debug=True)
