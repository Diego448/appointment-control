from pymongo import MongoClient

client = MongoClient()
db = client.appointment_control_dev
appointments = db.appointments

def save_appointment(appointment_data):
    appointment_id = appointments.insert_one(appointment_data).inserted_id
    return appointment_id

def get_all_appointments():
    return appointments.find()

def get_appointment(id):
    return appointments.find_one({'id': id})