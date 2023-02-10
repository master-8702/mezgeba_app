from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

# in this class we do everythig related to the admin dashboard (panel) in relation with the 'account' app

# here even though we can use 'account.User' model we choose not to and use the model from django.contrib.auth
# but they are the same since we set it on setting.py file 
User = get_user_model()

# here we are removing Group Model from admin since We're not using it.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['name','father_name', 'grand_father_name','email', 'admin']
    list_filter = ['admin',  'staff', 'active']
    fieldsets = (
        (None, {'fields': ('name','father_name', 'grand_father_name','email', 'password')}),
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','father_name', 'grand_father_name','email', 'password', 'password_2')}
        ),
    )
    # here we are deciding what fields should be available to the user to search in the admin panel
    search_fields = ['name','email']
    # here we are deciding what fields should be available to the user to order the (user)list in the admin panel
    ordering = ['name','email']
    filter_horizontal = ()


# here we are adding (registering) the [User] and [UserAdmin] models to our admin page , 
# so we can access and maange them inside admin panel
admin.site.register(User, UserAdmin)
