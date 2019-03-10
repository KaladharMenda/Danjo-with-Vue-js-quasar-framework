# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import *
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def student_details(request):
    import pdb; pdb.set_trace()
    data_dict = json.loads(request.POST.keys()[0])
    try:
        Student_details.objects.create(**data_dict)
    except Exception as e:
        import traceback




    return HttpResponse("Success")
