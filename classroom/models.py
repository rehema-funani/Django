from django.db import models
from student.models import Student

# Create your models here.
class Class(models.Model):
    class_name = models.CharField(max_length= 20)
    class_trainer = models.CharField(max_length= 20)
    class_size = models.CharField(max_length=20)
    class_motto= models.CharField(max_length= 20)
    class_routine = models.CharField(max_length= 20)
    class_vission = models.CharField(max_length= 20)
    class_goals = models.CharField(max_length= 20)
    class_equipment = models.CharField(max_length= 20)
    class_lessons = models.CharField(max_length= 20)
    class_id = models.PositiveSmallIntegerField(default = 0)
    students = models.ManyToManyField(Student)

    def __str__ (self):
        return f"{self.class_name} {self.class_trainer}"