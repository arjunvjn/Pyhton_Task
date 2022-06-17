from django import forms
from .models import *

class CreateStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('stu_id')

