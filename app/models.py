from django.db import models

# Create your models here.
class Student(models.Model):
    Sid=models.IntegerField(primary_key=True)
    Sname=models.CharField(max_length=50)
    Semail=models.EmailField()
    

    def __str__(self):
        return self.Sname
