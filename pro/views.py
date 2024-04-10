from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

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

class RentalContractListCreate(generics.ListCreateAPIView):
    queryset = RentalContract.objects.all()
    serializer_class = RentalContractSerializer

class RentalContractRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = RentalContract.objects.all()
    serializer_class = RentalContractSerializer

