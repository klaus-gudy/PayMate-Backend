from django.db import models
from users.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Property(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    contact = models.CharField(max_length=13)
    emergency_contact = models.CharField(max_length=13)

class RentalContract(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class MaintenanceRequest(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    request_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('InProgress', 'In Progress'), ('Completed', 'Completed')])