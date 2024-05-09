from django.urls import path

from .views import JobView, AddJobView



urlpatterns = [
    path('jobs', JobView.as_view(), name='all-jobs'),
    path('jobs/add', AddJobView.as_view(), name='add-job')
]