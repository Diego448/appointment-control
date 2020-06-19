from flask import Flask, render_template, request
from db_utilities import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/appointments/all')
def show_all_appointments():
    appointments = get_all_appointemnts()
    return render_template('all-appointments.html', data=appointments)

@app.route('/appointments/add', methods=['POST', 'GET'])
def add_appointment():
    if request.method == 'POST':
        customer_name = request.form['name']
        appointment_date = request.form['date']
        appointment_time = request.form['time']
        appointment_status = request.form['status']
        appointment_data = {
            'name': customer_name,
            'date': appointment_date,
            'time': appointment_time,
            'status': appointment_status
        }
        save_appointment(appointment_data)
        return "Cita guardada"
    return render_template('AddAppointment.html')

@app.route('/appointments/edit')
def edit_appointment():
    if request.method == 'POST':
        customer_name = request.form['name']
        appointment_date = request.form['date']
        appointment_time = request.form['time']
        appointment_status = request.form['status']
        appointment_data = {
            'name': customer_name,
            'date': appointment_date,
            'time': appointment_time,
            'status': appointment_status
        }
        save_appointment(appointment_data)
        return "Cita guardada"
    
    return render_template('AddAppointment.html')
    
        