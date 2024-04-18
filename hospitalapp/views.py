from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render, redirect
from django.shortcuts import render

from hospitalapp.forms import registrationForm
from hospitalapp.models import Doctors, Department,Booking


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def dep(request):
    s1=Department.objects.all()
    d1={'key':s1}
    return render(request,'department.html',d1)

def doc(request):
    category1=request.GET.get('Department')

    if category1==None:
        photos =  Doctors.objects.all()
    else:
        photos =  Doctors.objects.filter(  dep_name=category1)

    categories= Department.objects.all()

    d2={'keys':categories,'key1':photos}
    return render(request,'doctor.html',d2)

def showmsg(request,pk):
    task=Doctors.objects.get(id=pk)


    d2 = { 'key1': task}

    return render(request,'image.html',d2)


def booking(request):
    s3=registrationForm()
    form = {'register': s3}
    if request.method == 'POST':
        s3=registrationForm(request.POST)
        if s3.is_valid():
            s3.save()
    return render(request, 'booking.html', form)

def contactme(request):
    return render(request,'contact.html')


