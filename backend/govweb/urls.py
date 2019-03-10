from django.conf.urls import url

from . import views
from views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student_details/$', student_details),
    url(r'^get_student_details/$', get_student_details),


]
