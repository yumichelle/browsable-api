# <app>/urls.py
from django.urls import path

from endpoint.views import *

urlpatterns = [
    # # path("<endpoint aka route>", views.<name of class>.as_view()),
    path('/studentlist', StudentList.as_view()),
    path('/<int:pk>', StudentDetail.as_view()),
    path('/save_medical', save_medical, name='save_contact'),
    path('/get_medical', get_medical, name='get_contact'),
]