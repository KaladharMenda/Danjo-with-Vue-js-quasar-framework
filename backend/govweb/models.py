from __future__ import unicode_literals

from django.db import models
from common import BigAutoField
from datetime import date
# Create your models here.

class Student_details(models.Model):
    id = BigAutoField(primary_key=True)
    student_name = models.CharField(max_length=400)
    pin = models.CharField(max_length=350, default='')
    gender = models.CharField(max_length=32 ,default ='')
    date_of_birth = models.DateTimeField(auto_now_add=True)
    relative_name = models.CharField(max_length=64 ,default ='')
    relation_ship = models.CharField(max_length=64 ,default ='')
    caste = models.CharField(max_length=64 ,default ='')
    qualification  = models.CharField(max_length=64 ,default ='')
    joining_date = models.DateTimeField(auto_now_add=True)
    ph=models.CharField(max_length=64 ,default ='')
    mole_one = models.CharField(max_length=128 ,default ='')
    mole_two = models.CharField(max_length=128 ,default ='')
    tenth_hallticket = models.CharField(max_length=128 ,default ='')
    tenth_passed_year = models.CharField(max_length=128 ,default ='')
    scheme_code = models.CharField(max_length=32 ,default ='')
    year_sem = models.CharField(max_length=32 ,default ='')
    shift = models.CharField(max_length=32 ,default ='')
    section = models.CharField(max_length=32 ,default ='')
    door_num = models.CharField(max_length=64 ,default ='')
    street_name = models.CharField(max_length=64 ,default ='')
    city = models.CharField(max_length=64 ,default ='')
    pincode = models.CharField(max_length=32 ,default ='')
    district = models.CharField(max_length=128 ,default ='')
    mandal = models.CharField(max_length=128 ,default ='')
    phone_number = models.CharField(max_length=32 ,default ='')
    email = models.CharField(max_length=64 ,default ='')
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'STUDENT_DETAILS'

class Attendence_details(models.Model):
     id = BigAutoField(primary_key=True)
     student_details= models.ForeignKey(Student_details, blank=True, null=True)
     year_sem = models.CharField(max_length=32 ,default ='')
     month = models.CharField(max_length=32 ,default ='')
     period = models.CharField(max_length=32 ,default ='')
     working_days = models.CharField(max_length=32 ,default ='')
     attended_days = models.CharField(max_length=32 ,default ='')
     class Meta:
         db_table = 'ATTENDENCE_DETAILS'
