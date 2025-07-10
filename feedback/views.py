from django.shortcuts import render, get_object_or_404, redirect
from .models import Feedback
from salaries.models import JobRecord
from django.utils import timezone
from rest_framework import viewsets
from .serializers import FeedbackSerializer
from rest_framework.permissions import IsAuthenticated

def list_feedback(request, job_id):
    job = get_object_or_404(JobRecord, id=job_id)
    feedbacks = Feedback.objects.filter(job=job)
    return render(request, 'list_feedback.html', {
        'job': job,
        'feedbacks': feedbacks
    })

def add_feedback(request, job_id):
    job = JobRecord.objects.get(id=job_id)

    if request.method == "POST":
        author_name = request.POST.get("author_name", "").strip()
        comment = request.POST.get("comment", "").strip()
        rating = int(request.POST.get("rating", 0))

        if author_name and 1 <= rating <= 5:
            Feedback.objects.create(
                job=job,
                author_name=author_name,
                comment=comment,
                rating=rating,
                created_at=timezone.now()
            )
            return redirect('list_feedback', job_id=job.id)

    return render(request, 'add_feedback.html', {"job": job})



class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]  # Pas de lecture publique ici

