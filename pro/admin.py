from django.contrib import admin
from .models import *

admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(RentalContract)
admin.site.register(MaintenanceRequest)
