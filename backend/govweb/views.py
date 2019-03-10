# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from models import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def student_details(request):
    student = Student.objects.get(id = 1)
    return HttpResponse(student.student_name)
