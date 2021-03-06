from django.db import models

class Student(models.Model):
	fname=models.CharField(max_length=20)
	lname=models.CharField(max_length=20)
	email=models.EmailField()
	city=models.CharField(max_length=20)