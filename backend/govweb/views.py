# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import *
from datetime import datetime
from dateutil.parser import parse
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def student_details(request):
    data_dict = json.loads(request.POST.keys()[0])
    pin = data_dict['pin']
    adding = data_dict.get('adding' ,'')
    if adding:
        del data_dict["adding"]
        student_obj = Student_details.objects.filter(pin = pin)
        if student_obj.exists() :
            return HttpResponse("The Student PIN Already Exists")
        try:
            Student_details.objects.create(**data_dict)
        except Exception as e:
            import traceback
            return HttpResponse(e)
    else:
        data_dict['date_of_birth']=  parse(data_dict['date_of_birth'])
        data_dict['joining_date'] = parse(data_dict['joining_date'])

        try:
            Student_details.objects.update(**data_dict)
        except Exception as e:
            import traceback
            return HttpResponse(e)

    return HttpResponse("Success")
@csrf_exempt
def get_student_details(request):
    pin = json.loads(request.POST.keys()[0])
    student_details = Student_details.objects.filter(pin = pin)
    if student_details.exists():
        student_details = student_details[0]
        data_dict ={}
        data_dict['student_name'] = student_details.student_name
        data_dict['pin'] = student_details.pin
        data_dict['gender'] = student_details.gender
        data_dict['date_of_birth'] = student_details.date_of_birth.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        data_dict['relative_name'] =student_details.relative_name
        data_dict['relation_ship'] =student_details.relation_ship
        data_dict['caste'] = student_details.caste
        data_dict['qualification']  = student_details.qualification
        data_dict['joining_date'] = student_details.joining_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        data_dict['ph'] = student_details.ph
        data_dict['mole_one'] = student_details.mole_one
        data_dict['mole_two'] = student_details.mole_two
        data_dict['tenth_hallticket'] = student_details.tenth_hallticket
        data_dict['tenth_passed_year'] = student_details.tenth_passed_year
        data_dict['scheme_code'] = student_details.scheme_code
        data_dict['year_sem'] = student_details.year_sem
        data_dict['shift'] = student_details.shift
        data_dict['section'] = student_details.section
        data_dict['door_num'] = student_details.door_num
        data_dict['street_name'] = student_details.street_name
        data_dict['city'] = student_details.city
        data_dict['pincode'] = student_details.pincode
        data_dict['district'] = student_details.district
        data_dict['mandal'] = student_details.mandal
        data_dict['phone_number'] = student_details.phone_number
        data_dict['email'] = student_details.email
        return HttpResponse(json.dumps(data_dict))
    else:
        return HttpResponse("Record NOT FOUND")

@csrf_exempt
def get_attendence_names(request):
    student_details = []
    attendence_dict = json.loads(request.POST.keys()[0])
    if attendence_dict['year_sem'] :
        students_obj = Student_details.objects.filter(year_sem = attendence_dict['year_sem'])
        if students_obj.exists():
            for student in students_obj :
                student_dict ={}
                student_dict ['student_name'] = student.student_name
                student_dict['pin'] = student.pin
                student_dict['scheme_code'] = student.scheme_code
                student_dict['year_sem'] = attendence_dict['year_sem']
                student_details.append(student_dict)

    return HttpResponse(json.dumps(student_details))
