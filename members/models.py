from django.db import models


# Create your models here.

class student(models.Model):
    firstname=models.CharField(max_length=100,default="")
    lastname=models.CharField(max_length=100,default="")
    age=models.IntegerField(default=0)
    email=models.CharField(max_length=100,default="")
    phone=models.BigIntegerField(default=0)
    image=models.ImageField(upload_to="")

class subject(models.Model):
    student_id=models.ForeignKey(to=student,on_delete=models.CASCADE)
    subjectname=models.CharField(max_length=100)
    chapter=models.IntegerField()
    description=models.TextField()