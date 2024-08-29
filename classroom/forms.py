from django import forms
from .models import Class
class ClassroomRegistationForm(forms.ModelForm):
    class Meta:
        model=Class
        fields="__all__"