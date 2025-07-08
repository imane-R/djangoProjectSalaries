from django.shortcuts import render
from .models import JobRecord
from django.db.models import Avg, Count

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
from django.shortcuts import render

# Create your views here.
