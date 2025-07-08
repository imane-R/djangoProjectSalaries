from django.db import models
from salaries.models import JobRecord

class Feedback(models.Model):
    job = models.ForeignKey(JobRecord, on_delete=models.CASCADE, related_name='feedbacks')
    author_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField()  # valeur entre 1 et 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} - {self.rating}/5"
