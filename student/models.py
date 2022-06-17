from django.db import models

# Create your models here.

class Student(models.Model):
    dep=(
        ('CS','CS'),
        ('EC','EC'),
        ('MECH','MECH')
    )
    stu_id=models.CharField(max_length=10,unique=True,null=False)
    branch=models.CharField(max_length=5,choices=dep)
    name=models.CharField(max_length=20)
    number=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    address=models.TextField(max_length=50)
    photo=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

class Mark(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    sub1=models.FloatField(default=0)
    sub2=models.FloatField(default=0)
    sub3=models.FloatField(default=0)

    def __str__(self):
        return self.student.name