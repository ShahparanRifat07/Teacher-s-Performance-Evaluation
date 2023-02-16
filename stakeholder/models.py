from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Institution(models.Model):
    institution_name = models.CharField(max_length=128)
    institution_code = models.CharField(max_length=11)
    established_year = models.CharField(max_length=4)
    institution_type = models.PositiveIntegerField()
    institution_head = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    institution_admin = models.OneToOneField(User, on_delete=models.CASCADE)
    apply_date = models.DateField(default=timezone.now)
    approved = models.BooleanField(default=False)

    @property
    def full_name(self):
        return self._full_name

    @property
    def email(self):
        return self._email

    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password


    def __str__(self):
        return self.institution_name


class Student(models.Model):
    pass

class Teacher(models.Model):
    pass

class Parent(models.Model):
    pass


        