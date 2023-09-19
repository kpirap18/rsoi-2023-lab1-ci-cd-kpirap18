from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/v1/persons$', views.person_service_api),
    re_path(r'^api/v1/persons/([0-9]+)$', views.person_service_api),
]