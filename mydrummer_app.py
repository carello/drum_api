from flask import Flask, make_response, request, jsonify, Response
import datetime
import urllib
import json
import os, sys, socket
import requests

# import dns.resolver


# options_cache = ({'options':[]},datetime.datetime.now())
options_cache = False
#results_cache = False

app = Flask(__name__)


#DATASERVER = "http://127.0.0.1:5003"


@app.route("/drummer_list")
def drummer_list():
    u = urllib.urlopen(DATASERVER + "/drummer_list")
    page = u.read()
    drummer_list = json.loads(page)["drummers"]

    resp = make_response(jsonify(drummers=drummer_list))
    return resp


@app.route("/options", methods=["GET", "PUT", "POST"])
def options_route():
    '''
    Methods used to view options, add new option, and replace options.
    '''
    
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
