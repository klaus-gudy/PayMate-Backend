from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Property(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)