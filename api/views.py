from  rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from teacher.models import Teacher
from course.models import Course
from .serializers import  CourseSerializer
from .serializers import  TeacherSerializer
from classroom.models import Class
from .serializers import ClassroomSerializer
from .serializers import ClassperiodSerializer
from classperiod.models import ClassPeriod


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
class TeacherListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many= True)
        return Response(serializer.data)

class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course , many= True)
        return Response(serializer.data)
    
class ClassroomListView(APIView):
    def get(self, request):
        classroom = Class.objects.all()
        serializer = ClassroomSerializer(classroom, many= True)
        return Response(serializer.data)
class ClassperiodListView(APIView):
    def get(self,request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassperiodSerializer(classperiod,many = True)
        return Response(serializer.data)
