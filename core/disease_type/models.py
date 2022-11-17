from django.db import models

class DiseaseType(models.Model):
    description = models.CharField(verbose_name="Description", max_length=140)
