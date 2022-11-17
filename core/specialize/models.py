from django.db import models
from doctor.models import Doctor
from disease_type.models import DiseaseType

class Specialize(models.Model):
    did = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    email = models.ForeignKey(Doctor, on_delete=models.CASCADE)
