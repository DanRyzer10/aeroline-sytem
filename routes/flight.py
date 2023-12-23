from flask import Blueprint, render_template, request
from flask import flash, redirect, url_for
from utils.db import db


flight = Blueprint("flight", __name__, url_prefix="/flight")

@flight.route("/create")
def create_flights():
    return render_template('views/flight/create.html')