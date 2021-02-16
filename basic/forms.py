from django import forms
from basic.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=("first_name", "last_name", "school",)