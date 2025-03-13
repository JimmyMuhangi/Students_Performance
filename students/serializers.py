from rest_framework import serializers  # Third-party first
from .models import Student  # Local import second

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

           
