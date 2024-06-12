from flask import Flask, render_template, request, url_for, redirect
# It's not a built-in module, this file does the API request
from api import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "GET":
        try:
            # Opens the file in read-mode that contains the API Key
            API = open("key.conf", "r")
            # I use request.args.get in order to make the form method GET and
            # have a query parameter in the URL
            searchQuery = request.args.get("q", "")
            # Pass the user's query and the API as Strings
            searchResults = search(searchQuery, API.read())
            return render_template("results.html", searchQuery=searchQuery, searchResults=searchResults)
        except:
            return "<h3>Something's wrong with Search API 😔 please try again later.<h3>"

@app.route("/privacy-policy")
def privacyPolicy():
    return render_template("privacy-policy.html")

app.run()
