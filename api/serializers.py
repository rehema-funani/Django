from rest_framework import serializers
from student.models import Student
from course.models import Course
from teacher.models import Teacher
from classroom.models import Class
from classperiod.models import ClassPeriod



class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"
class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["course_name","course_level"]


class StudentSerializer(serializers.ModelSerializer):
    courses= CourseSerializer(many = True)

    class Meta:
        model = Student
        fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["first_name","last_name"]
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"
class MinimalClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["class_name","class_trainer"]
class Meta:
        model = Class
        fields = ["first_name","last_name"]
class ClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"
class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ["course","classroom"]

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model = Student
        fields = ["id","full_name","email"]




