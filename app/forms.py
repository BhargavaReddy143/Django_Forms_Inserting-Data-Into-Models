from django import forms


class Student_Details(forms.Form):
    Sid=forms.IntegerField()
    Sname=forms.CharField(max_length=50)
    Semail=forms.EmailField()