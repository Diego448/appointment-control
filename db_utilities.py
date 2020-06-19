from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.appointment_control_dev
appointments = db.appointments

def save_appointment(appointment_data):
    appointment_id = appointments.insert_one(appointment_data).inserted_id
    return appointment_id

def get_all_appointemnts():
    return appointments.find()

def get_appointment(id):
    object_id = ObjectId(id)
    return appointments.find_one({'id': object_id})