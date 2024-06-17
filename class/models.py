from django.db import models

# Create your models here.
class Class(models.Model):
     class_name = models.CharField(max_length = 20)
     class_teacher = models.CharField(max_length = 20)
     class_size = models.PositiveIntegerField()
     class_rep = models.CharField(max_length = 20)
     enrollment = models.PositiveSmallIntegerField()
     class_goal = models.CharField(max_length = 30)
     class_vision = models.TextField(max_length = 30)
     class_id = models.CharField(max_length = 15)
     class_capacity = models.PositiveSmallIntegerField()
     class_meetings = models.CharField(max_length = 10)



     def __str__(self):
        return f"{self.class_name} {self.class_goal}"
