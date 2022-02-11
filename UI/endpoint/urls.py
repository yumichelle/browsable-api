# <app>/urls.py
from django.urls import path, re_path

from endpoint.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="api.py API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@ "),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



# endpoints:
urlpatterns = [
    # # path("<endpoint aka route>", views.<name of class>.as_view()),
    path('/studentlist', StudentList.as_view()),
    path('/studentlist/<int:pk>', StudentDetail.as_view(), name='details'),
   #  path('/save_medical', save_medical, name='save_contact'),
   #  path('/get_medical', get_medical, name='get_contact'),

   #  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   #  # ^ A JSON view of your API specification at /swagger.json
   #  # ^ A YAML view of your API specification at /swagger.yaml
   #  path('/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   #  path('/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
   path('/api/schema/', SpectacularAPIView.as_view(), name='schema'),
   # Optional UI:
   path('/api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('/api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


]

