from django.db import models
from users.models import User

class Doctor(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=20, null=False)
