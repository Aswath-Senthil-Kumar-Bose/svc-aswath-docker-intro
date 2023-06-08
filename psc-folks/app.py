#!/usr/bin/python
from flask import Flask, Response
import json

app = Flask(__name__)


@app.route("/")
def folks():
    psc_folks = [
        {"name": "Dominick Peluso", "email": "dominick_peluso@bose.com", "title": "Docker Debutant"},
        {"name": "Peter Tanski", "email": "peter_tanski@bose.com", "title": "The Most Interesting Man in Bose"},
        {"name": "Joe Bermann", "email": "joe_bermann@bose.com", "title": "Manager of Mystery"},
    ]
    return json.dumps(psc_folks)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
