from django.urls import path
from .views import *

urlpatterns = [
    path('owners/', OwnerListCreate.as_view()),
    path('owner/<int:pk>/', OwnerRetrieveUpdateDestroy.as_view()),

    path('properties/', PropertyListCreate.as_view()),
    path('property/<int:pk>/', PropertyRetrieveUpdateDestroy.as_view()),

    path('tenants/', TenantListCreate.as_view()),
    path('tenant/<int:pk>/', TenantRetrieveUpdateDestroy.as_view()),

    path('rental-contracts/', RentalContractListCreate.as_view()),
    path('rental-contract/<int:pk>/', RentalContractRetrieveUpdateDestroy.as_view()),
]