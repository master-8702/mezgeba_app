from django.db import models
from accounts.models import User
from django.core.validators import RegexValidator


# In this class we are defining our model for Individual Registrars

class IndividualRegistrar(models.Model):

    GENDER_CHOICE = (('male','Male'), ('female', 'Female'))
    # here we are creating regex (regular expression) validator fro our phone field to accepty numbers only
    # with a maximum of fiften (15) digit
    phone_regex = RegexValidator(regex=r'^[0-9]+$', message="Phone number must be numerics only")

    user =models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(unique=True,validators=[phone_regex], max_length=15) # validators should be a list
    gender = models.CharField(choices=GENDER_CHOICE, max_length=6)
    address_country = models.CharField(max_length=255)
    address_state = models.CharField(max_length=255)
    address_city = models.CharField(max_length=255)


    def __str__(self):
        return str(self.user.name) + ' > ' + self.phone_number + ' > ' + self.user.email

