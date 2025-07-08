from django.db import models

# --------------------------
# Modèle complémentaire : Type de contrat
# --------------------------
class Contract(models.Model):
    # Code du contrat, ex : FT, PT, etc.
    type_code = models.CharField(max_length=10, unique=True)
    # Description plus lisible du type de contrat
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


# --------------------------
# Modèle complémentaire : Poste du candidat
# --------------------------
class JobTitle(models.Model):
    # Intitulé du poste, ex : Data Scientist
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# --------------------------
# Modèle complémentaire : Lieu de résidence
# --------------------------
class Location(models.Model):
    # Code du pays, ex : FR, US
    country_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.country_code

        # --------------------------
        # Modèle complémentaire : Secteur d'activité
        # --------------------------

class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

        # --------------------------
        # Modèle complémentaire : Candidat
        # --------------------------

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # --------------------------
    # Modèle principal : Enregistrement d'un job
    # --------------------------
class JobRecord(models.Model):
    # Relation vers le candidat
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)

    # Titre du poste (ex: Data Scientist, ML Engineer, etc.)
    job_title = models.ForeignKey('JobTitle', on_delete=models.SET_NULL, null=True)

    # Type de contrat (CDI, CDD, freelance...)
    contract = models.ForeignKey('Contract', on_delete=models.SET_NULL, null=True)

    # Secteur d'activité
    industry = models.ForeignKey('Industry', on_delete=models.SET_NULL, null=True)

    # Pays de résidence du salarié
    employee_residence = models.CharField(max_length=100)

    # Pays où se trouve l'entreprise
    company_location = models.CharField(max_length=100)

    # Salaire brut annuel (standardisé en USD)
    salary_in_usd = models.FloatField()

    # Niveau d'expérience (ex: Junior, Mid, Senior)
    experience_level = models.CharField(max_length=50)

    # Nombre d’années (année de collecte, ex: 2020)
    year = models.PositiveIntegerField()

    # Est-ce que le poste est en remote total ?
    remote_ratio = models.IntegerField(help_text="Pourcentage de télétravail (0 à 100)")

    # Pour éviter les doublons : unique constraint sur job_title + year + location
    class Meta:
        unique_together = ('job_title', 'year', 'company_location')

    def __str__(self):
        return f"{self.job_title.name} ({self.year}) - {self.company_location}"



