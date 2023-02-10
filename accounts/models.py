from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# and in this class we will manage our custome user class (defined below this class)
# means operation on user model (like createsuperuser) are defined in here
class UserManager(BaseUserManager):

    def create_user(self, name, father_name, grand_father_name,email, password=None,is_active= True, is_staff = False, is_admin = False):
       
       # the fllowing error messages (exception) will not be shown on the form as error messages 
       # they will be shown on the termianl 
        if not name:
            raise ValueError ("Users must have a name")
        if not father_name:
            raise ValueError ("Users must have a father name")
        if not grand_father_name:
            raise ValueError ("Users must have a grand father name")
        if not email:
            raise ValueError ("Users must have an email address")
        if not password:
            raise ValueError ("Users must have a password")

        user = self.model(
            name = name,
            father_name = father_name,
            grand_father_name = grand_father_name,
            email = self.normalize_email(email),

        )

        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using = self._db)
        return user

    def create_staffuser(self, name, father_name, grand_father_name, email, password=None):

        user= self.create_user(
            name,
            father_name,
            grand_father_name,
            email, password=password,
            is_staff=True
        )
        return user

    # this method is gonna be called when we enter the command 'py manage.py createsuperuser'   
    def create_superuser(self, name, father_name, grand_father_name, email, password=None):

        user = self.create_user(
            name,
            father_name, 
            grand_father_name,
            email,
            password=password,
            is_staff=True,
            is_admin=True
            
                )
        return user




# here in this class we are buidling a custome user class by inheriting the django's AbstractBaseUser class
# means if we wan't to add additional fields in addition to what django provides, here the place to do that.
# we will define our user model, required fields in our user model and some basic methods 
class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    grand_father_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    # phone = models.BigIntegerField(unique=True)
    # address = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
   
    # here we are saying use email field as username field
    USERNAME_FIELD = 'email'

    # username (email in our case) and password are required by default,
    # so we do not have to include them here in the [REQUIRED_FIELDS] list
    REQUIRED_FIELDS = ['name', 'father_name', 'grand_father_name'] 


    objects = UserManager()

    # here we will decide what will be dispalyed by default if the user object is called (used)
    # with out using the dot oprator (like user.name)
    def __str__(self):
        return self.email

    # here another getter method for full name
    def get_full_name(self):
        return self.name+self.father_name+self.grand_father_name


    # here we will define other getter methods as well but since we are using @property above them
    # we can call (use) them as a property
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    # here are some methods we should override based on the documentation since we are overriding 
    # the whole django's user model. they are usefull when we are using djano's permission and groups.
    # 
    def has_perm(self, perm, obj = None):

        return True

    def has_module_perms(self, app_label ):

        return True





    

