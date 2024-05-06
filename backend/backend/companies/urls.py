from django.urls import path

from .views import *


urlpatterns = [
    path("companies", CompanyList.as_view() , name="company-list"),
]