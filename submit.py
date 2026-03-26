#  Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas.
#   Upon successful submission, the user should be redirected to another page displaying the message "Data submitted successfully".
#    If there's an error during submission, display the error on the same page without redirection.

from flask import Flask, request, redirect, url_for, render_template
import certifi
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://deeprajsingh141:testing14@clusterdemo.t9u1cxq.mongodb.net/?appName=clusterdemo")
db = client["mydatabase"]
collection = db["mycollection"]
@app.route("/")
def home():
    return """
    <form action="/submit" method="POST">
        <input type="text" name="name" placeholder="Enter Name" required><br>
        <input type="email" name="email" placeholder="Enter Email" required><br>
        <button type="submit">Submit</button>
    </form>
    """
@app.route("/submit", methods=["POST"])
def submit_data():
    name = request.form.get("name")
    email = request.form.get("email")

    collection.insert_one({
        "name": name,
        "email": email
    })

    return "Data inserted successfully!"

if __name__ == "__main__":
    app.run(debug=True)