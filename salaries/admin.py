from django.contrib import admin
from .models import Contract, JobTitle, Industry, Candidate, JobRecord, Category

admin.site.register(Contract)
admin.site.register(JobTitle)
admin.site.register(Industry)
admin.site.register(Candidate)
admin.site.register(Category)
admin.site.register(JobRecord)
