from flask import Flask, make_response, request, jsonify, Response
import urllib
import json
import os, sys, socket
import requests

# Phase 3 - p5002


app = Flask(__name__)

#DATASERVER = "http://127.0.0.1:5003"


@app.route("/mess", methods=["POST"])
def messit():
    drummer = request.data
    resp = findme2(drummer)
    return resp


def findme2(d):
    u = requests.post(DATASERVER + "/lookupdrummer", data=d)
    page = u.content
    return page


@app.route("/options", methods=["GET"])
def options_route():
    u = DATASERVER + "/options"
    if request.method == "GET":
        page = requests.get(u)
        options = page.json()
        resp = Response(json.dumps(options), content_type='application/json')
    return resp


if __name__ == '__main__':
    DATASERVER = os.getenv('data_server')
    app.run(debug=True, host='0.0.0.0', port=int('5002'))
