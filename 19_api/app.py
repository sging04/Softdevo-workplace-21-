from flask import Flask, render_template
import urllib
import json
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    r = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=e2ap3uxmHNj4uFNli4Pycwao3UBhp6EcFKpVEkh0").read()
    return render_template("index.html", json.loads(r)["hdurl"])

app.run()  # Q4: Where have you seen similar construcs in other languages?
