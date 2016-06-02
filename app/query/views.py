from flask import (
    Blueprint, render_template, session, g, flash, request, redirect, url_for,
    current_app
)
from models import QueryDrill
import json

query_app = Blueprint('query_app', __name__)

@query_app.route("/query", methods=['GET', 'POST'])
def query():
    drill = QueryDrill("http://data-node002:8047")
    res = drill.run_query("select * from `MDB.exponea`.`customers` limit 10")
    return json.dumps(res)

@query_app.route("/", methods=['GET'])
def main():
    return render_template("main.html")

@query_app.route("/demo", methods=['GET'])
def demo():
    return render_template("demo.html")