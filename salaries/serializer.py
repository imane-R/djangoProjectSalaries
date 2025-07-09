from rest_framework import serializers
from .models import (
    Contract,
    Industry,
    Candidate,
    JobTitle,
    Category,
    JobRecord
)

# Serializer pour Contract
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

# Serializer pour Industry
class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'

# Serializer pour Candidate
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

# Serializer pour JobTitle
class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = '__all__'

# Serializer pour Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Serializer principal pour JobRecord
class JobRecordSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only=True)
    industry = IndustrySerializer(read_only=True)
    candidate = CandidateSerializer(read_only=True)

    class Meta:
        model = JobRecord
        fields = [
            "id",
            "year", "experience_level",
            "contract",
            "job_title", "job_title",
            "industry",
            "salary_in_usd", "salary_in_usd",
            "employee_residence", "remote_ratio",
            "company_location",
            "candidate"
        ]
