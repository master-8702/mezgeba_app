from django.db import models
from accounts.models import User
from django.core.validators import RegexValidator



class CompanyRegistrar(models.Model):

    # we will use this coustome validator to [company_phone] field, it will allow numbers ony
    phone_regex = RegexValidator(regex=r'^[0-9]+$', message="Phone number must be numerics only")

    user =models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_field = models.CharField(max_length=255)
    company_address_country = models.CharField(max_length=255)
    company_address_state = models.CharField(max_length=255)
    company_address_city = models.CharField(max_length=255)
    company_phone = models.CharField(unique=True,validators=[phone_regex], max_length=15) # validators should be a list
    contact_person_phone = models.CharField(unique=True,validators=[phone_regex], max_length=15)
    contact_person_address_country = models.CharField(max_length=255)
    contact_person_address_state = models.CharField(max_length=255)
    contact_person_address_city = models.CharField(max_length=255)
    number_of_employees = models.CharField(max_length=255)

