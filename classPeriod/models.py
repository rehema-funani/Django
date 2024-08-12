from django.db import models
import json

# Create your models here.


class ClassPeriodd(models.Model):
    def __init__(self, teacher, course, time):
        self.teacher = teacher
        self.course = course
        self.time = time
        

weekly_timetable = {
    "Monday": [
        {"teacher": "Mr. Smith", "course": "Mathematics", "time": "09:00 - 10:30"},
        {"teacher": "Mrs. Johnson", "course": "Science", "time": "14:00 - 15:30"}
    ],
    "Tuesday": [
        {"teacher": "Dr. Brown", "course": "History", "time": "09:00 - 10:30"},
        {"teacher": "Ms. Davis", "course": "English", "time": "14:00 - 15:30"}
    ],
}

timetable_json = json.dumps(weekly_timetable, indent=4)

print(timetable_json)
