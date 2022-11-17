from django.db import models
from users.models import User

class PublicServant(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=20, null=False)