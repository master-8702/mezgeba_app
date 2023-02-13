from django.db import models
from django.core.validators import RegexValidator
from accounts.models import User


# In this class we are defining our model for Company  Registrars

class Registrant(models.Model):

    # a choice for geneder field
    GENDER_CHOICE = (('male','Male'), ('female', 'Female'))

     # here we are creating regex (regular expression) validator fro our phone field to accepty numbers only
    # with a maximum of fiften (15) digit
    phone_regex = RegexValidator(regex=r'^[0-9]+$', message="Phone number must be numerics only")

    # here we are setting 'null=True' and 'blank=True' on all fields because we don't know what field(s) the customer 
    # wants to be a required one (all fields are nullable by default)
    # so all the validations will be handled from the frontend, since the APi will accept empty values(null).
    # in short django will just pass NULL to the database for every 'null=True' fields. and
    # django will not make the field required in forms (admin from and other custom forms) for every 'blank=True' fields  

    user =models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    grand_father_name = models.CharField(max_length=50, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)  ## date of birth
    POB = models.CharField(max_length=20, help_text='place of birth', null=True, blank=True)   ## place of birth
    phone_number = models.CharField(unique=True,validators=[phone_regex], max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True,)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=6, null=True, blank=True)
    address_country = models.CharField(max_length=50, null=True, blank=True)
    address_state = models.CharField(max_length=50, null=True, blank=True)
    address_city = models.CharField(max_length=50, null=True, blank=True)    
    id_number = models.CharField(max_length = 25, null=True, blank=True)
    # here for the [attachement] field even though we are gonna be receiving multiple files from the api's, if we try to add registrant 
    # from the django admin panel we can't, because django doesn't support multiple files in a single field. 
    # there is a work around though,to do that: we will create another table for the images with a forign key to registrant table and 
    # use inlineModelAdmin, it will allow us to choose multiple images without leaving the current page while adding registrants.
    # But since we are not gonna be using the django admin as a frontend am not gonna implement that,i will just leave it as it is
    attachement = models.FileField(upload_to='uploadedAttachements', null=True, blank=True,)
    other_notes = models.TextField(max_length=1000, null=True, blank=True)
    additional_fields = models.TextField( null=True, blank=True)


    # here since all the fields could be null, returning those values will raise an error
    # so we are just returning the only not-null value user
    def __str__(self):
        
        return str(self.user)
   

    
    
