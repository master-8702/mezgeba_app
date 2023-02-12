from rest_framework import serializers
from company_registrar.models import CompanyRegistrar

# here we will declare our class and fields for the serializer 
class CompanyRegistrarSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyRegistrar        # use the [CompanyRegistrar] model when serializing and Deserializing
        fields = '__all__'              # serialize all the fields in the model