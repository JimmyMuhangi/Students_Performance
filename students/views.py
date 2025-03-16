from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from .forms import StudentForm

def welcome_view(request):
    return render(request, 'students/welcome.html')

@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    if request.accepted_renderer.format == 'html':
        return render(request, 'students_table.html', {'students': students})
    else:
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

@api_view(["POST"])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def student_form_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def success_page(request):
    return render(request, 'students/success.html')

def student_list(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'students/student_list.html', {'students': students})

