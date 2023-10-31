import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendancerealtime-4c124-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "321652":
        {
            "name": "Soham Kadam",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance":6,
            "standing":"G",
            "year":3,
            "last_attendance_time": "2023-10-11 00:54:34"

        },
    "678954":
        {
            "name": "Shriya Hundekari",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance":7,
            "standing":"B",
            "year":3,
            "last_attendance_time": "2023-10-11 00:56:34"

        },
    "789569":
        {
            "name": "Shivendra Ghatge",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance":69,
            "standing":"G",
            "year":3,
            "last_attendance_time": "2023-10-11 00:57:34"

        },
    "852744":
        {
            "name": "Neeta Kole",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance":9,
            "standing":"G",
            "year":3,
            "last_attendance_time": "2023-10-11 00:57:34"

        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance":0,
            "standing":"B",
            "year":3,
            "last_attendance_time": "2023-10-11 00:25:34"

        },
    "698545":
        {
            "name": "Chetana More",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance":5,
            "standing":"G",
            "year":3,
            "last_attendance_time": "2023-10-11 00:25:34"

        },
    "798970":
        {
            "name": "Chaitanaya Chougle",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 5,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2023-10-11 00:25:34"

        },
    "457896":
        {
            "name": "Sakshi Patil",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 5,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2023-10-11 00:25:34"

        },



}

for key, value in data.items():
    ref.child(key).set(value)