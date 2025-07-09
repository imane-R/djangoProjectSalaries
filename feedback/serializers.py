from rest_framework import serializers
from .models import Feedback
from salaries.serializer import JobRecordSerializer

class FeedbackSerializer(serializers.ModelSerializer):
    job = JobRecordSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = [
            "id",
            "job",
            "author_name",
            "comment",
            "created_at"
        ]
