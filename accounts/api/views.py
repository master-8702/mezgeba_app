from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.api.serializers import UserSerializer

from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def user_registration(request):

    # here we will serialize the coming data from the post request
    serializer = UserSerializer(data=request.data)
    # this map called [data] is gonna be used to return some info about the new user when a certain user registers succcessfully
    # until we make sure the coming data is valid we will just initialize it to empty map(list)
    data = {}

    # here checking 'is_valid', beside checking if the sent data is valid it will give us access to [validated_data] 
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
        # here we are generating 'access' and 'refresh' tokens to send it as a response when creating a new user
        token  = RefreshToken.for_user(user)
        data['refresh'] = str(token)
        data['access'] = str(token.access_token)
    else:
        data = serializer.errors

    return Response(data)

