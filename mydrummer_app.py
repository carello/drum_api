from flask import Flask, make_response, request, jsonify, Response
import urllib
import json
import os, sys, socket
import requests
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt



#options_cache = False

app = Flask(__name__)

DATASERVER = "http://127.0.0.1:5003"

'''
@app.route("/drummer_list")
def drummer_list():
    u = urllib.urlopen(DATASERVER + "/drummer_list")
    page = u.read()
    drummer_list = json.loads(page)["drummers"]
    resp = make_response(jsonify(drummers=drummer_list))
    return resp


@app.route("/stevegadd", methods=["POST"])
def drummer():
    u = urllib.urlopen(DATASERVER + "/stevegadd")
    page = u.read()
    stevegadd = json.loads(page)['stevegadd']
    resp = Response(json.dumps(stevegadd))
    return resp

@app.route("/buddyrich", methods=["POST"])
def br():
    u = urllib.urlopen(DATASERVER + "/buddyrich")
    page = u.read()
    buddyrich = json.loads(page)['buddyrich']
    resp = Response(json.dumps(buddyrich))
    return resp

@app.route("/carterbeauford", methods=["POST"])
def cb():
    u = urllib.urlopen(DATASERVER + "/carterbeauford")
    page = u.read()
    cb = json.loads(page)['carterbeauford']
    resp = Response(json.dumps(cb))
    return resp


@app.route("/chetcarello", methods=["POST"])
def cc():
    u = urllib.urlopen(DATASERVER + "/chetcarello")
    page = u.read()
    cc = json.loads(page)['chetcarello']
    resp = Response(json.dumps(cc))
    return resp


@app.route("/neilpeart", methods=["POST"])
def np():
    u = urllib.urlopen(DATASERVER + "/neilpeart")
    page = u.read()
    np = json.loads(page)['neilpeart']
    resp = Response(json.dumps(np))
    return resp

@app.route("/vinniecolaiuta", methods=["POST"])
def vc():
    u = urllib.urlopen(DATASERVER + "/vinniecolaiuta")
    page = u.read()
    vc = json.loads(page)['vinniecolaiuta']
    resp = Response(json.dumps(vc))
    return resp

'''
@app.route("/mess", methods=["POST"])
def messit():
    drummer = request.data
    #return drummer
    resp = findme(drummer)
    return resp


def findme(d):
    u = urllib.urlopen(DATASERVER + "/" + d)
    page = u.read()
    vc = json.loads(page)[d]
    resp = Response(json.dumps(vc))
    return resp


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
    #DATASERVER = os.getenv('data_server')
    app.run(debug=True, host='0.0.0.0', port=int('5002'))
