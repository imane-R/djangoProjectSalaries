from django.urls import path
from .views import dashboard, job_list

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path('jobs/', job_list, name='job_list'),
]
