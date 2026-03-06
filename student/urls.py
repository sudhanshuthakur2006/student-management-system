from django.urls import path
from . import views
urlpatterns = [
    path("",views.student),
    path("add_student/",views.add_student)
]