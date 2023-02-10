from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    # here since we do not have password_2 (confirm password field) in our model ,
    # we are creating one here and add it to the serializer
    password_2 = serializers.CharField(style= {'input_type': 'password'}, write_only = True)
    
    class Meta:
        model = User
        fields = ['name', 'father_name', 'grand_father_name', 'email', 'password', 'password_2']
       
        # here we are just making sure the frist password is not visible to anyone
        extra_kwargs = {
            'password': {'write_only':True}
        }

    # here we are overriding the save method  because we have to check if the two passwordsa are a match 

    def save(self):
        user  = User(
            name =self.validated_data['name'],
            father_name =self.validated_data['father_name'],
            grand_father_name =self.validated_data['grand_father_name'],
            email =self.validated_data['email'],

        )
        password =self.validated_data['password']
        password_2 =self.validated_data['password_2']

        if password != password_2:
            raise serializers.ValidationError({'error message':'the two passwords do not match'})

        user.set_password(password)

        # and if everything is set we just call the main save method that is gonna save our model
        user.save()
        return user

    