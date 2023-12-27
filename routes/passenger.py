from flask import Blueprint, render_template, request
from flask import flash, redirect, url_for
from utils.db import db

from models.passenger import Passenger




passenger = Blueprint("passenger", __name__, url_prefix="/passenger")

@passenger.route("/create")
def create_passengers():
    return render_template('views/passenger/create.html')

@passenger.route("/all")
def all_passengers():
    passengers = Passenger.query.all()
    return render_template('views/passenger/index.html', passengers=passengers)

@passenger.route("/read/<int:passenger_id>")
def read_passengers(passenger_id):
    passenger = Passenger.query.get(passenger_id)
    if passenger is None:
        flash('El pasajero no existe','danger')
        return redirect(url_for('index'))
    return render_template('views/passenger/read.html', passenger=passenger)

@passenger.route("/update" , methods=['GET','POST'])
def update_passengers():
    # get query string parameter
    passenger_id = request.args.get('passenger_id')
    passenger = Passenger.query.get(passenger_id)
    if passenger is None:
        return "pasajero no encontrado", 404
    #actualizae los datos si el metodo es post
    if request.method == 'POST':
        passenger.name = request.form['name']
        passenger.lastname = request.form['lastname']
        passenger.age = request.form['age']
        passenger.phone = request.form['phone']
        passenger.email = request.form['email']
        passenger.address = request.form['address']
        db.session.commit()
        flash('El pasajero se ha actualizado correctamente','success')
        return redirect(url_for('passenger.all_passengers'))
    return render_template('views/passenger/update.html', passenger=passenger)

@passenger.route("/delete",methods=['GET','POST'])
def delete_passengers():
    passenger_id = request.args.get('passenger_id')
    passenger = Passenger.query.get(passenger_id)
    if passenger is None:
        return "pasajero no encontrado", 404
    db.session.delete(passenger)
    db.session.commit()
    flash('El pasajero se ha eliminado correctamente','success')
    return redirect(url_for('passenger.all_passengers'))
    


@passenger.route('/', methods=['POST'])
def store_passenger():
    name = request.form['name']
    lastname = request.form['lastname']
    age = request.form['age']
    phone = request.form['phone']
    email = request.form['email']
    address = request.form['address']  
    passenger = Passenger(name, lastname, age, phone, email, address)
    db.session.add(passenger,)
    db.session.commit()
    flash('El pasajero se ha creado correctamente','success')
    return redirect(url_for('passenger.create_passengers'))
    



# @passenger_bp.route("/<passenger_id>", methods=["GET"])
# def get_passenger(passenger_id):
#     return "passenger_id"