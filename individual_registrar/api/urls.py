from django.urls import path
from .views import (individual_registrar_list, individual_registrar_register, 
individual_registrar_detail, 
individual_registrar_update,
individual_registrar_delete)

# here we are defining our routes/ paths/ urls for the Indiviual Registrar API

urlpatterns = [
    path('list/', individual_registrar_list),                # an endpoint to query all registraras
    path('detail/<int:pk>/', individual_registrar_detail),  # an endpoint to query a single registrar
    path('register/', individual_registrar_register),        # an endpoint to register a new registrar
    path('update/<int:pk>/', individual_registrar_update),   # an endpoint to update an existing registrar
    path('delete/<int:pk>/', individual_registrar_delete),  # an endponit to delete an existing registrar

]