from django import forms
from .models import Teacher
class TeacherRegistationForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields="__all__"