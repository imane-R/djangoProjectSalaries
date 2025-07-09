from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedbackViewSet
from . import views

router = DefaultRouter()
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('feedback/<int:job_id>/', views.list_feedback, name='list_feedback'),
    path('feedback/<int:job_id>/add/', views.add_feedback, name='add_feedback'),
    path("api/", include(router.urls)),
]
