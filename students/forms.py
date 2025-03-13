from django import forms
from .models import Student  # Assuming you have a Student model

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'index_number', 'mid_term', 'end_term']

