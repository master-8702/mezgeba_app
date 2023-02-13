from django.urls import path
from .views import (registrant_list, registrant_detail, registrant_register, registrant_update, registrant_delete)



# here we are defining our routes/ paths/ urls for the  Registrant API

urlpatterns = [
    path('list/', registrant_list),                  # an endpoint to query all registered registrants    
    path('detail/<int:pk>/', registrant_detail),     # an endpoint to query a single registrant
    path('register/', registrant_register),          # an endpoint to register a new registrant
    path('update/<int:pk>/', registrant_update),     # an endpoint to update an existing registrant
    path('delete/<int:pk>/', registrant_delete),     # an endponit to delete an existing registrant


]