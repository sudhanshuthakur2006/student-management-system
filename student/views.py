from django.shortcuts import render
from .models import Student
# Create your views here.
def student(request):

    student_data=Student.objects.all()

    data={
        "student_data":student_data
    }
    return render(request,"student/student.html",data)
def add_student(request):

    if request.method=="POST":
        student_name=request.POST.get("input_name")
        student_email=request.POST.get("input_email")
        student_phone_number=request.POST.get("input_phone_number")

        Student.objects.create(
            name=student_name,
            email=student_email,
            phone_number=student_phone_number
        )


    return render(request,"student/add_student.html")