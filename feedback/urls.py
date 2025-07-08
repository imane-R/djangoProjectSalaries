from django.urls import path
from . import views

urlpatterns = [
    path('feedback/<int:job_id>/', views.list_feedback, name='list_feedback'),
    path('feedback/<int:job_id>/add/', views.add_feedback, name='add_feedback'),

]
