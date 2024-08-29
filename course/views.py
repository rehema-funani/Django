
from django.shortcuts import render

# Create your views here.


from .forms import CourseRegistationForm
def register_course(request):
    form=CourseRegistationForm()
    return render(request,"course/register_course.html", {"form":form})
