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
from rest_framework import status
from .serializers import MinimalStudentSerializer
from .serializers import MinimalCourseSerializer
from .serializers import MinimalTeacherSerializer
from .serializers import MinimalClassPeriodSerializer
from .serializers import MinimalClassroomSerializer


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        # first_name = request.query_params.get("first_name")
        # country = request.query_params.get("country")
        # if first_name:
        #     students = students.filter(first_name = first_name)
        # if country:
        #     students = students.filter(country = country)

        serializer = MinimalStudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






        
class StudentDetailView(APIView):
    def enroll_student(self,student,course_id):
        course= Course.objects.get(id = course_id)
        student.courses.add(course)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
    
        if action :"enroll"
        course_id = request.data.get("course")
        self.enroll_student(student, course_id)
        
        return Response(status=status.HTTP_202_ACCEPTED)

    def get(self,request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self,request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class TeacherListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = MinimalTeacherSerializer(teacher, many= True)
        return Response(serializer.data)
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def assign_class(self,teacher,class_id):
        classroom= Class.objects.get(id = class_id)
        teacher.classes.add(classroom)

    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
    
        if action :"assign"
        class_id = request.data.get("classroom")
        self.assign_class(teacher, class_id)
        
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def get(self,request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
   
    def put(self,request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        teacher = Teacher.objects.get(id = id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)       

class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()

       
        serializer = MinimalCourseSerializer(course , many= True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self,request,id):
        student = Course.objects.get(id = id)
        serializer = CourseSerializer(student)
        return Response(serializer.data)
    def put(self,request,id):
        student = Course.objects.get(id = id)
        serializer = CourseSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        course = Course.objects.get(id = id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class ClassroomListView(APIView):
    def get(self, request):
        classroom = Class.objects.all()
        serializer = MinimalClassroomSerializer(classroom, many= True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ClassroomDetailView(APIView):
    def add_student(self,classroom,student_id):
        student= Student.objects.get(id = student_id)
        student.add_student.add(student)

    def post(self, request, id):
        classroom = Class.objects.get(id=id)
        action = request.data.get("action")
    
        if action :"add"
        student_id = request.data.get("student")
        self.add_student(classroom, student_id)
        
        return Response(status=status.HTTP_202_ACCEPTED)

    
    def get(self,request,id):
        classroom = Class.objects.get(id = id)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)
    def put(self,request,id):
        classroom = Class.objects.get(id = id)
        serializer = ClassroomSerializer(classroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        classroom = Class.objects.get(id = id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class ClassperiodListView(APIView):
    def get(self,request):
        classperiod = ClassPeriod.objects.all()
        serializer = MinimalClassPeriodSerializer(classperiod,many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClassperiodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ClassperiodDetailView(APIView):
    def get(self,request,id):
        classperiod = ClassPeriod.objects.get(id = id)
        serializer = ClassperiodSerializer(classperiod)
        return Response(serializer.data)
    def put(self,request,id):
        classperiod = ClassPeriod.objects.get(id = id)
        serializer = ClassperiodSerializer(classperiod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self,request,id):
        classPeriod = ClassPeriod.objects.get(id = id)
        classPeriod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)    


    
