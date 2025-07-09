from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            "id",
            "job",
            "author_name",
            "comment",
            "rating",
            "created_at"
        ]
        read_only_fields = ["created_at"]  # auto-généré
