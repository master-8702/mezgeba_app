from rest_framework import serializers
from registrant.models import Registrant

# here in this class we will be defining our model and fields for the serializer

class RegistrantSerializer(serializers.ModelSerializer):

    class Meta:
        # here we are just saying when serializing/ deserializing use the Registrant model 
        # and serialize/deserialzie all the fields
        # but if want to add all the field with some exception we can do : 'exclude = ('name','age' )'
        # note that we can not use both [fields] and [exclude]  at the same time
        model = Registrant
        fields = '__all__'
        