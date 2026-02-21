
from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route("/")
def home():
    return ("Welcome to my assignment")


@app.route("/api", methods=["GET"])
def get_data():
    with open("std.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True)

