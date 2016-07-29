from flask import Flask, make_response, request, jsonify, Response
import urllib
import json
import os, sys, socket
import requests


app = Flask(__name__)

#DATASERVER = "http://127.0.0.1:5003"


@app.route("/mess", methods=["POST"])
def messit():
    drummer = request.data
    #return drummer
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
        status = 200
    resp = Response(
        json.dumps(options, sort_keys=True, indent = 4, separators = (',', ': ')),
        content_type='application/json', status=status)
    return resp


if __name__ == '__main__':
    DATASERVER = os.getenv('data_server')
    app.run(debug=True, host='0.0.0.0')
