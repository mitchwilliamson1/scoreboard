from bottle import Bottle, route, template, request, response
from .players import Players
import urllib
import json

playersapp = Bottle()


@playersapp.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

PASS = "nicetry"


@playersapp.route("/", method=["OPTIONS", "POST"])
def slash():
    if request.method == "OPTIONS":
        return
    json_obj = json.loads(request.body.read())
    response.status = 200
    return json.dumps({"pass": True})
    if json_obj['pass'] == PASS:
        return json.dumps({"pass": True})
    else:
        return "false"

@playersapp.route("/get_players")
def get_players():
    return Players().get_players()


@playersapp.route("/get_teams")
def get_players():
    return Players().get_teams()


@playersapp.route("/create_player", method=["POST", "OPTIONS"])
def save():
    if request.method == "OPTIONS":
        return
    json_obj = json.loads(request.body.getvalue())
    Players().create_player(json_obj['create_player']) 
    return request.json


@playersapp.route("/create_team", method=["POST", "OPTIONS"])
def save():
    if request.method == "OPTIONS":
        return
    json_obj = json.loads(request.body.getvalue())
    Players().create_team(json_obj['create_team']) 
    return request.json


@playersapp.route("/save", method="POST")
def save():
    json_obj = json.loads(request.body.read())
    Players().save(json_obj) 
    return request.json

@playersapp.route("/create_bill", method="POST")
def create_bill():
    Players().create_bill(request.json)
    return request.json

