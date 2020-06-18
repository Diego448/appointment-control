from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/appointments/all')
def show_all_appointments():
    return render_template('all-appointments.html')

@app.route('/appointments/add')
def add_appointment():
    return render_template('AddAppointment.html')