from django.urls import path
from . import views

urlpatterns = [
    path('owners/', views.OwnerListCreate.as_view()),
    path('owner/<int:pk>/', views.OwnerRetrieveUpdateDestroy.as_view()),

    path('properties/', views.PropertyListCreate.as_view()),
    path('property/<int:pk>/', views.PropertyRetrieveUpdateDestroy.as_view()),

    path('tenants/', views.TenantListCreate.as_view()),
    path('tenant/<int:pk>/', views.TenantRetrieveUpdateDestroy.as_view()),

    path('rental-contracts/', views.RentalContractListCreate.as_view()),
    path('rental-contract/<int:pk>/', views.RentalContractRetrieveUpdateDestroy.as_view()),

    path('total-tenants/', views.get_total_tenants, name='total-tenants'),
]