from django.db import models
from publicservant.models import PublicServant
from countries.models import Country
from disease.models import Disease

class Record(models.Model):
    email = models.ForeignKey(PublicServant, on_delete=models.CASCADE)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    total_deaths = models.PositiveBigIntegerField(default=0)
    total_patients = models.PositiveBigIntegerField(default=0)
