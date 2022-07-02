from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=256)
    email=models.CharField(max_length=256)
    location=models.CharField(max_length=256)
    def __str__(self):
        return self.name