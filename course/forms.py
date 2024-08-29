from django import forms
from .models import Course
class CourseRegistationForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"