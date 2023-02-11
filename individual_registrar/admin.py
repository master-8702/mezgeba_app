from django.contrib import admin
from individual_registrar.models import IndividualRegistrar

# here we are adding the model to our admin dashboard (panel)
admin.site.register(IndividualRegistrar)