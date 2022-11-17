from django.db import models
from countries.models import Country
from disease_type.models import DiseaseType

class Discover(models.Model):
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    first_enc_date_year = models.PositiveIntegerField(default=2022)
    first_enc_date_month = models.PositiveIntegerField(default=10)
    first_enc_date_day = models.PositiveIntegerField(default=5)