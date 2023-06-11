from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def show1(request):
    return render(request,'testapp/student.html')
def show2(request):
    return render(request,'testapp/one.html')
def show3(request):
    return render(request,'testapp/faculty.html')
def show4(request):
    return render(request,'testapp/event.html')
def about(request):
    return render(request,'testapp/about.html')
def base(request):
    return render(request,'testapp/base.html')
def random(request):
    return render(request,'testapp/about.html')
