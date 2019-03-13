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





]
