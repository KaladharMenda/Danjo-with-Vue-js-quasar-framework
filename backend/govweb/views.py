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
    data_dict ={}
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
            student_obj = Student_details.objects.filter(pin = pin)
            student_obj.update(**data_dict)
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
        existing_pin = []
        attendence_obj = Attendence_details.objects.filter(year_sem = attendence_dict['year_sem'],period =attendence_dict['period'] ,month = attendence_dict['month'])
        if attendence_obj.exists() :
            for student in attendence_obj:
                student_dict ={}
                student_dict ['student_name'] = student.student_details.student_name
                student_dict['pin'] = student.student_details.pin
                student_dict['scheme_code'] = student.student_details.scheme_code
                student_dict['year_sem'] = attendence_dict['year_sem']
                student_dict['attended_days'] = student.attended_days
                student_details.append(student_dict)
                existing_pin.append(student_dict['pin'])
        students_obj = Student_details.objects.filter(year_sem = attendence_dict['year_sem'])
        if students_obj.exists():
            for student in students_obj :
                if student.pin not in existing_pin :
                    student_dict ={}
                    student_dict ['student_name'] = student.student_name
                    student_dict['pin'] = student.pin
                    student_dict['scheme_code'] = student.scheme_code
                    student_dict['year_sem'] = attendence_dict['year_sem']
                    student_details.append(student_dict)

    return HttpResponse(json.dumps(student_details))

@csrf_exempt
def delete_student_details(request):
    pin = json.loads(request.POST.keys()[0])
    student_details = Student_details.objects.filter(pin = pin)
    if student_details.exists():
        student_details = student_details[0]
        student_details.status = False
        student_details.save()
    return HttpResponse("Success")

@csrf_exempt
def attendece_update(request):
    attendence_dict ={}
    attendence_dict = json.loads(request.POST.keys()[0])
    try:
        for record in attendence_dict :
            attendence_dict = {}
            pin = record.get('pin','')
            attendence_dict['year_sem'] = record.get('year_sem','')
            attendence_dict['month'] = record.get('month','')
            attendence_dict['period'] = record.get('period','')
            attendence_dict['working_days'] = record.get('working_days','')
            student_obj = Student_details.objects.filter(pin = pin)
            if student_obj.exists():
                attendence_dict['student_details'] = student_obj[0]
            else:
                return HttpResponse("Pin Does not exists")
            existing_obj = Attendence_details.objects.filter(**attendence_dict)
            if existing_obj.exists():
                existing_obj = existing_obj[0]
                existing_obj.attended_days = record.get('no_of_days_attend','')
                existing_obj.save()
            else:
                attendence_dict['attended_days'] = record.get('no_of_days_attend','')
                Attendence_details.objects.create(**attendence_dict)
        return HttpResponse("Success")
    except Exception as e:
        import traceback
        return HttpResponse("Some thing went wrong")
@csrf_exempt
def all_attendence(request):
    attendence_dict ={}
    student_details = []
    attendence_dict = json.loads(request.POST.keys()[0])
    try:
        if attendence_dict['period'] == 'complete':
            attendence_obj = Attendence_details.objects.filter(year_sem = attendence_dict['year_sem'],month = attendence_dict['month']).order_by('-student_details')
        else:
            attendence_obj = Attendence_details.objects.filter(year_sem = attendence_dict['year_sem'],period =attendence_dict['period'] ,month = attendence_dict['month'])
        if attendence_obj.exists() :
            for attendence in attendence_obj:
                student_dict ={}
                student_dict ['student_name'] = attendence.student_details.student_name
                student_dict['pin'] = attendence.student_details.pin
                student_dict['scheme_code'] = attendence.student_details.scheme_code
                student_dict['year_sem'] = attendence_dict['year_sem']
                student_dict['attended_days'] = attendence.attended_days
                student_dict['working_days'] = attendence.working_days
                if attendence.period == 'second_period' :
                    student_dict ['period'] = '16 to Month End'
                else:
                    student_dict ['period'] = '1 to 15 days'

                student_details.append(student_dict)

        return HttpResponse(json.dumps(student_details))
    except Exception as e:
        import traceback
        return HttpResponse("Some thing went wrong")




@csrf_exempt
def get_sm_marks(request):
    student_details =[]
    sm_marks_dict = json.loads(request.POST.keys()[0])
    subject = sm_marks_dict['subject']
    year_sem = sm_marks_dict['year_sem']
    schemecode = sm_marks_dict['scheme_code']
    students_obj = Student_details.objects.filter(year_sem = sm_marks_dict['year_sem'],scheme_code =sm_marks_dict['scheme_code'])
    if students_obj.exists():
        for student in students_obj :
            student_dict ={}
            student_dict ['student_name'] = student.student_name
            student_dict['pin'] = student.pin
            student_dict['scheme_code'] = student.scheme_code
            student_dict['year_sem'] = sm_marks_dict['year_sem']
            student_details.append(student_dict)
    return HttpResponse(json.dumps(student_details))

@csrf_exempt
def get_unit_marks(request):
    student_details =[]
    unit_dict = json.loads(request.POST.keys()[0])
    existing_pin = []
    unit_obj = Unit_marks.objects.filter(year_sem = unit_dict['year_sem'],subject =unit_dict['subject'],unit_exam = unit_dict['unit_exam'])
    if unit_obj.exists() :
        for unit in unit_obj:
            student_dict ={}
            student_dict ['student_name'] = unit.student_details.student_name
            student_dict['pin'] = unit.student_details.pin
            student_dict['marks'] = unit.marks
            student_dict['total_marks'] = unit.total_marks
            student_details.append(student_dict)
            existing_pin.append(student_dict['pin'])
    if not unit_dict.get('view','') :
        students_obj = Student_details.objects.filter(year_sem = unit_dict['year_sem'])
        if students_obj.exists():
            for student in students_obj :
                if student.pin not in existing_pin :
                    student_dict ={}
                    student_dict ['student_name'] = student.student_name
                    student_dict['pin'] = student.pin
                    student_dict['marks'] = ''
                    student_dict['year_sem'] = unit_dict['year_sem']
                    student_details.append(student_dict)
    return HttpResponse(json.dumps(student_details))


@csrf_exempt
def unit_marks_update(request):
    unit_marks_dict = json.loads(request.POST.keys()[0])
    unit_exam = unit_marks_dict[0].get('unit_exam','')
    if not unit_exam :
        return HttpResponse("Unit Exam Does not Exists")
    subject = unit_marks_dict[0].get('subject','')
    if not subject:
        return HttpResponse("Subject is Empty")
    total_marks =unit_marks_dict[0].get('total_marks','')
    if not total_marks :
        return HttpResponse("Total Marks is Empty")
    try:
        for record in unit_marks_dict :
            unit_dict = {}
            pin = record.get('pin','')
            unit_dict['year_sem'] = record.get('year_sem','')
            student_obj = Student_details.objects.filter(pin = pin)
            unit_dict['unit_exam'] = unit_exam
            unit_dict['subject'] = subject
            if student_obj.exists():
                unit_dict['student_details'] = student_obj[0]
            else:
                return HttpResponse("Pin Does not exists")
            existing_obj = Unit_marks.objects.filter(**unit_dict)
            unit_dict['total_marks'] = total_marks
            if existing_obj.exists():
                existing_obj = existing_obj[0]
                existing_obj.marks = record.get('marks','')
                existing_obj.total_marks = total_marks
                existing_obj.save()
            else:
                unit_dict['marks'] = record.get('marks','')
                Unit_marks.objects.create(**unit_dict)
        return HttpResponse("Success")
    except Exception as e:
        import traceback
        return HttpResponse("Some thing went wrong")

@csrf_exempt
def get_pm_marks(request):
    student_details =[]
    pm_dict = json.loads(request.POST.keys()[0])
    existing_pin = []
    view = False
    if pm_dict.get('view','') :
        view = True
        pm_obj = Project_marks.objects.filter(year_sem = pm_dict['year_sem'],scheme_code =pm_dict['scheme_code'])
    else:
        pm_obj = Project_marks.objects.filter(year_sem = pm_dict['year_sem'],scheme_code =pm_dict['scheme_code'],project_title = pm_dict['project_title'])
    if pm_obj.exists() :
        for pm in pm_obj:
            student_dict ={}
            student_dict ['student_name'] = pm.student_details.student_name
            student_dict['pin'] = pm.student_details.pin
            student_dict['project_name'] = pm.project_title
            student_dict['marks'] = pm.marks
            student_dict['total_marks'] = pm.total_marks
            student_details.append(student_dict)
            existing_pin.append(student_dict['pin'])
    if not view :
        students_obj = Student_details.objects.filter(year_sem = pm_dict['year_sem'] ,scheme_code = pm_dict['scheme_code'])
        if students_obj.exists():
            for student in students_obj :
                if student.pin not in existing_pin :
                    student_dict ={}
                    student_dict ['student_name'] = student.student_name
                    student_dict['pin'] = student.pin
                    student_dict['marks'] = ''
                    student_dict['year_sem'] = pm_dict['year_sem']
                    student_details.append(student_dict)
    return HttpResponse(json.dumps(student_details))

@csrf_exempt
def pm_marks_update(request):
    pm_marks_dict = json.loads(request.POST.keys()[0])
    scheme_code = pm_marks_dict[0].get('scheme_code','')
    if not scheme_code :
        return HttpResponse("Scheme Code  Does not Exists")
    project_title = pm_marks_dict[0].get('project_title','')
    if not project_title:
        return HttpResponse("Project Title is Empty")
    total_marks =pm_marks_dict[0].get('total_marks','')
    if not total_marks :
        return HttpResponse("Total Marks is Empty")
    try:
        for record in pm_marks_dict :
            pm_dict = {}
            pin = record.get('pin','')
            pm_dict['year_sem'] = record.get('year_sem','')
            student_obj = Student_details.objects.filter(pin = pin)
            pm_dict['project_title'] = project_title
            pm_dict['scheme_code'] = scheme_code
            if student_obj.exists():
                pm_dict['student_details'] = student_obj[0]
            else:
                return HttpResponse("Pin Does not exists")
            existing_obj = Project_marks.objects.filter(**pm_dict)
            pm_dict['total_marks'] = total_marks
            if existing_obj.exists():
                existing_obj = existing_obj[0]
                existing_obj.marks = record.get('marks','')
                existing_obj.total_marks = total_marks
                existing_obj.save()
            else:
                pm_dict['marks'] = record.get('marks','')
                Project_marks.objects.create(**pm_dict)
        return HttpResponse("Success")
    except Exception as e:
        import traceback
        return HttpResponse("Some thing went wrong")
