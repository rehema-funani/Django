from django.db import models

# Create your models here.
class ClassPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    course = models.CharField(max_length= 40)
    classroom = models.CharField(max_length= 40)
    day_of_the_week = models.CharField(max_length= 40)
    def  __self__(self):
        return f"{self.course}"