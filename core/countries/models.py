from django.db import models

class Country(models.Model):
    cname = models.CharField(verbose_name="Country Name", max_length=65, unique=True)
    population = models.PositiveBigIntegerField(verbose_name="Population")