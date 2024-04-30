import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://realtimeattendencesystem-a86c8-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    "644464":
        {
            "name": "Subhanker Rajhans",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2022-04-11 00:54:34"
        },
    "852741":
        {
            "name": "Samridhi Saini",
            "major": "Enviromental Science",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-04-11 00:54:34"
        },
    "963852":
        {
            "name": "Prince Raj",
            "major": "Physics",
            "starting_year": 2021,
            "total_attendance":0 ,
            "standing": "F",
            "year": 2,
            "last_attendance_time": "2022-04-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)