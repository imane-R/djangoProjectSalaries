from django.shortcuts import render
from .models import JobRecord
from django.db.models import Avg, Count
from rest_framework import viewsets
from .models import JobRecord, Contract, Industry, Candidate
from .serializer import JobRecordSerializer, ContractSerializer, IndustrySerializer, CandidateSerializer
from django.core.paginator import Paginator

def dashboard(request):
    total_jobs = JobRecord.objects.count()
    average_salary = JobRecord.objects.aggregate(Avg("salary_in_usd"))["salary_in_usd__avg"]
    countries_covered = JobRecord.objects.values("company_location").distinct().count()

    context = {
        "total_jobs": total_jobs,
        "average_salary": round(average_salary, 2) if average_salary else 0,
        "countries_covered": countries_covered,
    }
    return render(request, "dashboard.html", context)


# Create your views here.

def job_list(request):
    min_rating = request.GET.get("min_rating")
    jobs = JobRecord.objects.annotate(
        feedback_count=Count("feedbacks"),
        average_rating=Avg("feedbacks__rating")
    )
    if min_rating:
        jobs = jobs.filter(average_rating__gte=min_rating)

    return render(request, "job_list.html", {"jobs": jobs})


class JobRecordViewSet(viewsets.ModelViewSet):
    queryset = JobRecord.objects.all()
    serializer_class = JobRecordSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
