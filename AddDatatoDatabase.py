import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cryptography.exceptions
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-b3e83-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')
data={
    "1892":
        {
         "name":"Kshitij Singh",
         "major":"CSAI",
         "starting_year":"2022",
         "total_attendance":13,
         "standing":"G",
         "year":"3",
         "last_attendance_time":"2025-2-24 00:54:34"
        },
"1901":
        {
         "name":"Sanir",
         "major":"CSAI",
         "starting_year":"2022",
         "total_attendance":13,
         "standing":"G",
         "year":"3",
         "last_attendance_time":"2025-2-24 00:54:34"
        },
"1907":
        {
         "name":"Gopal Kumar",
         "major":"CSAI",
         "starting_year":"2022",
         "total_attendance":13,
         "standing":"G",
         "year":"3",
         "last_attendance_time":"2025-2-24 00:54:34"
        },
"1951":
        {
         "name":"Aryan Raj Singh",
         "major":"CSAI",
         "starting_year":"2022",
         "total_attendance":13,
         "standing":"G",
         "year":"3",
         "last_attendance_time":"2025-2-24 00:54:34"
        }
}
for key,value in data.items():
    ref.child(key).set(value)

