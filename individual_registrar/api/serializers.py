from rest_framework import serializers
from individual_registrar.models import IndividualRegistrar

# here in this class we will define our serializer for IndividualRegistrar model(class) 

class IndividualRegistrarSerializer(serializers.ModelSerializer):

    class Meta:
        # here we are telling the serializer to use the IndividualRegistrar model while serializing
        model = IndividualRegistrar
        # and here we are telling the serializer to serialize all field from the model
        # if we want to serialize only some of the fields we can set it like this: ' fields = ['name', 'age', 'phone_number'] ' 
        fields = '__all__'