from django.db import models
from countries.models import Country

class User(models.Model):
    email = models.CharField(verbose_name="Email", max_length=60, unique=True, null=False)
    name = models.CharField(verbose_name="Name", max_length=30, unique=True, null=False)
    surname = models.CharField(verbose_name="Surname", max_length=40, unique=True, null=False)
    salary = models.PositiveBigIntegerField(default=0)
    phone = models.CharField(max_length=20, null=False)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
