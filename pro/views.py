from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import date
from datetime import timedelta

class OwnerListCreate(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class PropertyListCreate(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class TenantListCreate(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

def get_total_tenants(request):
    total_tenants = Tenant.objects.all().count()
    return total_tenants

def get_total_properties(request):
    total_properties = Property.objects.all().count()
    return total_properties

def get_total_tenants_with_contracts(request):
    today = date.today()
    total_rental_contracts = RentalContract.objects.filter(end_date__gte=today).count()
    return total_rental_contracts

def get_tenants_with_near_end_date(request):
    today = date.today()
    end_date = today + timedelta(days=30)
    tenants = RentalContract.objects.filter(end_date__gte=today, end_date__lte=end_date)
    return tenants

class RentalContractListCreate(generics.ListCreateAPIView):
    queryset = RentalContract.objects.all()
    serializer_class = RentalContractSerializer

class RentalContractRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = RentalContract.objects.all()
    serializer_class = RentalContractSerializer

