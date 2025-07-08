# analytics.py

import os
import django

# Initialiser Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProjectSalaries.settings")
django.setup()

from salaries.models import JobRecord
from django.db.models import Avg, Count
from datetime import datetime

# Liste pour stocker les lignes du rapport
report_lines = []

def write_and_print(line):
    """Ajoute une ligne au rapport et l'affiche en console."""
    print(line)
    report_lines.append(line)

# -------------------------------
# 1. Top 5 des jobs les mieux payés
top_jobs = (
    JobRecord.objects
    .values("job_title__name")
    .annotate(avg_salary=Avg("salary_in_usd"))
    .order_by("-avg_salary")[:5]
)

write_and_print("🔝 Top 5 job titles les mieux payés (en USD):")
for job in top_jobs:
    write_and_print(f"- {job['job_title__name']}: {round(job['avg_salary'], 2)} USD")
write_and_print("")

# -------------------------------
# 2. Salaire moyen par niveau d’expérience
salary_by_exp = (
    JobRecord.objects
    .values("experience_level")
    .annotate(avg_salary=Avg("salary_in_usd"))
)

write_and_print("📈 Salaire moyen par niveau d’expérience :")
for entry in salary_by_exp:
    write_and_print(f"- {entry['experience_level']}: {round(entry['avg_salary'], 2)} USD")
write_and_print("")

# -------------------------------
# 3. Nombre de jobs par company_location
jobs_by_country = (
    JobRecord.objects
    .values("company_location")
    .annotate(count=Count("id"))
    .order_by("-count")
)

write_and_print("🌍 Nombre de jobs par pays (company_location):")
for entry in jobs_by_country:
    write_and_print(f"- {entry['company_location']}: {entry['count']} jobs")
write_and_print("")

# -------------------------------
# 4. Ratio de jobs 100% remote
total_jobs = JobRecord.objects.count()
remote_jobs = JobRecord.objects.filter(remote_ratio=100).count()
percentage_remote = (remote_jobs / total_jobs) * 100 if total_jobs > 0 else 0

write_and_print(f"💻 Jobs 100% remote : {remote_jobs} / {total_jobs} ({round(percentage_remote, 2)}%)")

# -------------------------------
# 5. Sauvegarde du rapport
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"report_{timestamp}.txt"

with open(filename, "w") as file:
    file.write("\n".join(report_lines))

write_and_print(f"\n✅ Rapport sauvegardé dans : {filename}")
