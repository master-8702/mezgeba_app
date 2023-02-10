from django.urls import path
from accounts.api.views import (user_registration)


urlpatterns = [
    path('register', user_registration),
]