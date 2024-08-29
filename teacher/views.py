from django.shortcuts import render


from .forms import TeacherRegistationForm
# Create your views here.
def register_teacher(request):
    form=TeacherRegistationForm()
    return render(request,"teacher/register_teacher.html", {"form":form})
