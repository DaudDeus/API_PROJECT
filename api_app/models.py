from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    year = models.IntegerField()
    
