from flask import Blueprint, render_template




passenger = Blueprint("passenger", __name__, url_prefix="/passenger")

@passenger.route("/create")
def create_passengers():
    return render_template('views/passenger/create.html')

@passenger.route("/list")
def read_passengers():
    return render_template('views/passenger/read.html')

@passenger.route("/update")
def update_passengers():
    return render_template('views/passenger/update.html')

@passenger.route("/delete")
def delete_passengers():
    return render_template('views/passenger/delete.html')
    



# @passenger_bp.route("/<passenger_id>", methods=["GET"])
# def get_passenger(passenger_id):
#     return "passenger_id"