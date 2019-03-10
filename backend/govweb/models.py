# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common import BigAutoField
from datetime import date
# Create your models here.

class Student(models.Model):
    id = BigAutoField(primary_key=True)
    student_name = models.CharField(max_length=400)

    class Meta:
        db_table = 'STUDENT'
