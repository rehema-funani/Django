from django.shortcuts import render

# Create your views here.


from .forms import ClassroomRegistationForm
def register_classroom(request):
    form=ClassroomRegistationForm()
    return render(request,"classroom/register_classroom.html", {"form":form})
