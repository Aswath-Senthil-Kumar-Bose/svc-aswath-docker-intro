#!/usr/bin/python

from cowpy import cow
from flask import Flask, Response
import requests
import logging
import os
# ...
PSC_FOLKS_URL = os.environ.get(
    "PSC_FOLKS_URL",
    "https://ingress-platform.live-aws-useast1.bose.io/dev/svc-dom-docker-intro/stable-test/psc-folks"
)
APP_PORT = int(os.environ.get("APP_PORT", "80"))

app = Flask(__name__)

PSC_FOLKS_URL = "https://ingress-platform.live-aws-useast1.bose.io/dev/svc-dom-docker-intro/stable-test/psc-folks"
APP_PORT = 80

@app.route("/")
def moo():
    return cow.get_cow()().milk("Love this Cute World!")


@app.route("/cows")
def get_folks():

    # Get PSC folks from psc-folks API
    services_r = requests.get(PSC_FOLKS_URL)
    folks = services_r.json()

    # Convert PSC folks into cows
    cows = ""
    for folk in folks:
        name = folk.get("name", "")
        logging.warning("Beginning tranformation of " + name + " into cow.")
        cows += cow.get_cow()().milk(name + " is a cow.") + "\n"

    return cows


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=APP_PORT)
