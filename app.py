import urllib.parse, urllib.request, urllib.error, json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def is_it_raining_in_seattle():
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    if is_it_raining_in_seattle == "true":
        rainCheck = "<h1>Yes</h1>"
    else:
        rainCheck = "<h1>No</h1>"
    return render_template("index.html")
