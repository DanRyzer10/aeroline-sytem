from flask import Flask, render_template, request, redirect, url_for, flash
from routes.passenger import passenger
from routes.flight import flight
from utils.db import db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+oracledb://system:oracle123@localhost:1521/xe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# SQLAlchemy(app)

app.secret_key = 'clave_secreta'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.register_blueprint(passenger)
app.register_blueprint(flight)



# Routes for the passenger

# @app.route('/passenger/create')
# def create_passengers():
#     return render_template('views/passenger/create.html')

# @app.route('/passenger/list')
# def read_passengers():
#      return render_template('views/passenger/read.html')

# @app.route('/passenger/update')
# def update_passengers():
#     return render_template('views/passenger/update.html')

# @app.route('/passenger/delete')
# def delete_passengers():
#      return render_template('views/passenger/delete.html')


# #routes for the flight

# @app.route('/flight/create')
# def create_flights():
#     return render_template('views/flight/create.html')

# @app.route('/flight/list')
# def read_flights():
#     return render_template('views/flight/read.html')

# @app.route('/flight/update')
# def update_flights():
#     return render_template('views/flight/update.html')

# @app.route('/flight/delete')
# def delete_flights():
#     return render_template('views/flight/delete.html')

# #-----------------------------------------------
# #post passenger
# @app.route('/passenger', methods=['POST'])
# def store_passenger():
#     flash('El pasajero se ha creado correctamente','success')
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     db
#     app.run(debug=True)