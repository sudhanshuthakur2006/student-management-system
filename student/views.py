from django.shortcuts import render,redirect
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

        return redirect ('student')

    return render(request,"student/add_student.html")
def delete_student(request,student_id):
    my_student=Student.objects.get(id=student_id)
    my_student.delete()
    return redirect("student")
def update_student(request,student_id):
    student=Student.objects.get(id=student_id)
    if request.method=="POST":
        student.name=request.POST.get("name")
        student.email=request.POST.get("email")
        student.phone_number=request.POST.get("phone_number")
        
        student.save()
        return redirect("student") 
    parameter={
        "student":student
    }
    return render(request,"student/update_student.html",parameter)