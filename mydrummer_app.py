from flask import Flask, make_response, request, jsonify, Response
import urllib
import json
import os
import requests


options_cache = False

app = Flask(__name__)

DATASERVER = "http://127.0.0.1:5003"

@app.route("/drummer_list")
def drummer_list():
    u = urllib.urlopen(DATASERVER + "/drummer_list")
    page = u.read()
    drummer_list = json.loads(page)["drummers"]

    resp = make_response(jsonify(drummers=drummer_list))
    return resp


@app.route("/stevegadd")
def drummer():
    u = urllib.urlopen(DATASERVER + "/stevegadd")
    page = u.read()
    stevegadd = json.loads(page)['stevegadd']
    resp = Response(json.dumps(stevegadd))
    return resp

@app.route("/buddyrich")
def buddyrich():
    u = urllib.urlopen(DATASERVER + "/buddyrich")
    page = u.read()
    buddyrich = json.loads(page)['buddyrich']
    resp = Response(json.dumps(buddyrich))
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
    app.run(debug=True, host='0.0.0.0', port=int("5002"))
