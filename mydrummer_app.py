from flask import Flask, make_response, request, jsonify, Response
#import datetime
import urllib
import json
import os, sys, socket
import requests

# import dns.resolver
# import paho.mqtt.publish as publish

# options_cache = ({'options':[]},datetime.datetime.now())
#options_cache = False
#results_cache = False

app = Flask(__name__)


#data_server = "http://127.0.0.1:5003"
#data_server = dataserver
#data_server = "http://stage2--mydrummer--drumdata--2c5f29.gce.shipped-cisco.com"

# Setup MQTT Topic Info
#lhost = socket.gethostname()


# TODO - Decide if this will be maintaned going forward
@app.route("/")
def drummer_list():
    u = urllib.urlopen(DATASERVER)
    page = u.read()
    drummer_list = json.loads(page)["drummers"]

    resp = make_response(jsonify(drummers=drummer_list))
    return resp


if __name__ == '__main__':
    #data_server = "http://doit--mydrummer--drumdata--42e669.gce.shipped-cisco.com"
    DATASERVER = os.getenv('data_server')
    app.run(debug=True, host='0.0.0.0')
