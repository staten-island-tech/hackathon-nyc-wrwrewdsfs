from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")