from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def show_route():
    response = requests.get("https://data.cityofnewyork.us/resource/m6nq-qud6.json")

    if response.status_code != 200:
        return "Failed to fetch routes", 500

    routes = response.json()
    return render_template("index.html", routes=routes)

@app.route("/routes/<int:vendorid>")
def route_details(vendorid):
    response = requests.get(f"https://data.cityofnewyork.us/resource/m6nq-qud6.json")

    if response.status_code != 200:
        return "Failed to fetch game details", 500

    route = response.json()
    return render_template("items.html", route=route)  

if __name__ == "__main__":
    app.run(debug=True)
