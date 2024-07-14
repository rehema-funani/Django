from rest_framework import serializers
from student.models import Student
from rest_framework.views import APIView

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

