from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.api.serializers import UserSerializer

@api_view(['POST'])
def user_registration(request):

    serializer = UserSerializer(data=request.data)
    data = {}

    # here checking 'is_valid', beside checing if the sent data is valid it will give us access to [validated_data] 
    # inside the serializer (serializer.py file) or inside forms (forms.py file) 
    if serializer.is_valid():
        # here the save method is not the main save method, it is the one we override inside the serializer class
        # that is gonna check if the two given passwords are a match, save the user and return user(the user object ) to us
        user  = serializer.save()
        data ['response'] = "You have successfully registered a new user." 
        data ['name'] = user.name 
        data ['father_name'] = user.father_name
        data ['grand_father_name'] = user.grand_father_name
        data ['email'] = user.email
    else:
        data = serializer.errors

    return Response(data)

