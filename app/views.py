from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def Inserting_Student(request):
    SO=Student_Details()
    D={'SO':SO}
    if request.method=='POST':
        SD=Student_Details(request.POST)
        if SD.is_valid():
            Sid=SD.cleaned_data['Sid']
            Sname=SD.cleaned_data['Sname']
            Semail=SD.cleaned_data['Semail']

            SDI=Student.objects.get_or_create(Sid=Sid, Sname=Sname, Semail=Semail)[0]
            SDI.save()


            SDR=Student.objects.all()
            D1={'SDR':SDR}
            return render(request, 'two.html',D1 )
    return render(request, 'one.html', D)