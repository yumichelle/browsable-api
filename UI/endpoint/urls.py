# <app>/urls.py
from django.urls import path

from endpoint.views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



# endpoints:
urlpatterns = [
   # # path("<endpoint aka route>", views.<name of class>.as_view()),
   path('/studentlist', StudentList.as_view()),
   path('/studentlist/<int:pk>', StudentDetail.as_view(), name='details'),

   path('/api/schema/', SpectacularAPIView.as_view(), name='schema'),
   # Optional UI:
   path('/api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('/api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
