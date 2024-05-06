
from django.contrib import admin
from django.urls import path, re_path, include

from companies.views import CompanyList

from users.views import RegisterUser, LoginUser, AllUsersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies', CompanyList.as_view()),
    path("api/", include("users.urls")), # user urls
    path("api/", include("companies.urls")) # companies urls
]
