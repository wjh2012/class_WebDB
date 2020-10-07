from django.shortcuts import render
from django.views.generic import ListView, DetailView
from student.models import Student

# Create your views here.
class StudentLV(ListView):
    model = Student

class StudentDV(DetailView):
    model = Student