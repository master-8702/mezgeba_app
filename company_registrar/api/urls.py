from django.urls import path
from .views import (company_registrar_list, company_registrar_detail, company_registrar_register, company_registrar_update, company_registrar_delete)



# here we are defining our routes/ paths/ urls for the Indiviual Registrar API

urlpatterns = [
    path('list/', company_registrar_list),                  # an endpoint to query all registered company registrars    
    path('detail/<int:pk>/', company_registrar_detail),     # an endpoint to query a single company registrar
    path('register/', company_registrar_register),          # an endpoint to register a new company registrar
    path('update/<int:pk>/', company_registrar_update),     # an endpoint to update an existing company registrar
    path('delete/<int:pk>/', company_registrar_delete),     # an endponit to delete an existing company registrar


]