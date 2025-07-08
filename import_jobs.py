# import_jobs.py

import csv
import os
import django

# Configuration pour accéder au projet Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProjectSalaries.settings")
django.setup()

# Importer les modèles
from salaries.models import JobRecord, JobTitle, Industry, Contract, Candidate

# Lecture du fichier CSV
with open('salaries.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0

    for row in reader:
        # Vérifier ou créer les objets liés
        job_title, _ = JobTitle.objects.get_or_create(name=row["job_title"])
        # On attribue "Tech" comme valeur par défaut pour le champ 'industry'
        industry_name = row.get("industry", "Tech")
        industry, _ = Industry.objects.get_or_create(name=industry_name)
        # On récupère le code de type d'emploi depuis 'employment_type', ou 'FT' par défaut
        type_code = row.get("employment_type", "FT")
        contract, _ = Contract.objects.get_or_create(
            type_code=type_code,
            defaults={"description": ""}
        )
        candidate, _ = Candidate.objects.get_or_create(
            email=row.get("employee_email", ""),
            defaults={
                "name": row.get("employee_name", "Unknown"),
                "company_location": row["company_location"]
            }
        )

        # Vérifie si la ligne existe déjà pour éviter les doublons
        if JobRecord.objects.filter(job_title=job_title, year=row["work_year"], company_location=row["company_location"]).exists():
            continue

        # Création du JobRecord
        JobRecord.objects.create(
            job_title=job_title,
            candidate=candidate,
            industry=industry,
            contract=contract,
            year=row["work_year"],
            company_location=row["company_location"],
            salary_in_usd=row["salary_in_usd"],
            remote_ratio=row["remote_ratio"]
        )

        count += 1

print(f"{count} enregistrements ajoutés avec succès.")
