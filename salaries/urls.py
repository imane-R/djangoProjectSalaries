from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import dashboard,job_list,JobRecordViewSet, ContractViewSet, IndustryViewSet, CandidateViewSet

router = DefaultRouter()
router.register(r'jobs', JobRecordViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'industries', IndustryViewSet)
router.register(r'candidates', CandidateViewSet)
urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path('jobs/', job_list, name='job_list'),
    path("api/", include(router.urls)),
]
