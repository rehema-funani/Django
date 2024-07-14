from django.shortcuts import render
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class StudentListViews(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many = True)
        return Response(serializer.data)