from django.conf.urls import url

from . import views
from views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_check/$', login_check),
    url(r'^student_details/$', student_details),
    url(r'^get_student_details/$', get_student_details),
    url(r'^get_attendence_names/$', get_attendence_names),
    url(r'^delete_student_details/$', delete_student_details),
    url(r'^attendece_update/$', attendece_update),
    url(r'^get_sm_marks/$', get_sm_marks),
    url(r'^all_attendence/$', all_attendence),
    url(r'^get_unit_marks/$', get_unit_marks),
    url(r'^unit_marks_update/$', unit_marks_update),
    url(r'^update_sem_subjects/$', update_sem_subjects),
    url(r'^get_sem_subjects/$', get_sem_subjects),
    url(r'^delete_sem_subjects/$', delete_sem_subjects),
    url(r'^update_sem_scheme_code/$', update_sem_scheme_code),
    url(r'^get_sem_schemes/$', get_sem_schemes),
    url(r'^delete_sem_scheme_code/$', delete_sem_scheme_code),
    url(r'^get_student_names/$', get_student_names),
    url(r'^update_semester_marks/$', update_semester_marks),
    url(r'^get_semester_marks_update/$', get_semester_marks_update),
    url(r'^get_pm_marks/$', get_pm_marks),
    url(r'^pm_marks_update/$', pm_marks_update),
    url(r'^get_semester_viewtable/$', get_semester_viewtable),
]
