from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/passenger/create')
def create_passengers():
    return render_template('views/passenger/create.html')

@app.route('/passenger/list')
def read_passengers():
    return render_template('views/passenger/read.html')

@app.route('/passenger/update')
def update_passengers():
    return render_template('views/passenger/update.html')

@app.route('/passenger/delete')
def delete_passengers():
    return render_template('views/passenger/delete.html')

if __name__ == '__main__':
    app.run(debug=True)