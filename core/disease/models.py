from django.db import models
from disease_type.models import DiseaseType

class Disease(models.Model):
    disease_code = models.CharField(verbose_name="Desease Code", max_length=50, unique=True)
    pathogen = models.CharField(verbose_name="Pathogen", max_length=20)
    description = models.CharField(verbose_name="Description", max_length=140)
    tid = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    