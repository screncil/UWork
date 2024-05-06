from django.urls import path

from .views import *


urlpatterns = [
    path("companies", CompanyList.as_view() , name="company-list"),
    path("company/register", RegisterCompany.as_view(), name="register-company"),
    path("company", CompanyDetail.as_view(), name="company-detail")
]