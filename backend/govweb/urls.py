from django.conf.urls import url

from . import views
from views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student_details/$', student_details),
    url(r'^get_student_details/$', get_student_details),
    url(r'^get_attendence_names/$', get_attendence_names),
    url(r'^delete_student_details/$', delete_student_details),
    url(r'^attendece_update/$', attendece_update),
    url(r'^get_sm_marks/$', get_sm_marks),
    url(r'^all_attendence/$', all_attendence),
    url(r'^get_unit_marks/$', get_unit_marks),
    url(r'^unit_marks_update/$', unit_marks_update),



]
