
from django.contrib import admin
from django.urls import path, re_path, include

from companies.views import CompanyList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies', CompanyList.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]
