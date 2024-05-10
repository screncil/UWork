from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from categories.views import CategoryList
from companies.views import CompanyList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies', CompanyList.as_view()),
    path("api/", include("users.urls")), # user urls
    path("api/", include("companies.urls")), # companies urls
    path("api/categories", CategoryList.as_view()),
    path("api/", include("jobs.urls"))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
