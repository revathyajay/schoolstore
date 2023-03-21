import django
from django.db import models
from django.utils import timezone


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Purpose(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Details(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(default=django.utils.timezone.now)
    phno = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.name


# Create your models here.
