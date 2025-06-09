from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def show_route():
    response = requests.get("https://data.cityofnewyork.us/resource/ycrg-ses3.json")

    if response.status_code != 200:
        return "Failed to fetch routes", 500

    routes = response.json()
    return render_template("index.html", routes=routes)

@app.route("/games/<int:game_id>")
def route_details(game_id):
    response = requests.get(f"https://www.freetogame.com/api/game?id={game_id}")

    if response.status_code != 200:
        return "Failed to fetch game details", 500

    route = response.json()
    return render_template("items.html", route=route)  

if __name__ == "__main__":
    app.run(debug=True)
