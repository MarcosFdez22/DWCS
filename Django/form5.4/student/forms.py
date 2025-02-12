from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "name":"Name",
            "degree":"Degree"
        }
        error_messages = {
            "name": {
                "required":"Your name must not be empty!",
            }
        }