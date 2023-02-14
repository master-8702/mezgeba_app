from .serializers import CompanyRegistrarSerializer
from company_registrar.models import CompanyRegistrar
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# In this class we will decalre a bunch of function based views that are gonna handle 
# the different API endpoints regarding Company Registrars
# in short they are just methods that will just accept a [request] and parameters and return accordingly

@api_view(['GET'])          
def company_registrar_list(request):

    # since list of all company_registrars should only be accessed by admin, here we will check if the user is admin 
    if request.user.is_admin:
        # here we are feching and return all the registered Company registrars (like select * from company_registrar)
        companyRegistrars = CompanyRegistrar.objects.all()
        # then we will serialize what we get from the query, in order to return them as a json
        # and we will set the 'many' parameter to True, because the serializer might (almost always in this case)
        # be handling a list of objects from the query result (not a single object) 
        # if we set that to false (the default) and the query returns a list then an exception will raise
        # because the serializer by default is expecting a single object  
        serializer  = CompanyRegistrarSerializer(companyRegistrars, many =True)

        # then we will return the serialized lists in a json format and HTTP status code as well
        return Response(data={'Company Registrars': serializer.data}, status=status.HTTP_200_OK)
    else:
         # if the user is not admin we will return authorization error
        return Response (data = {'Error': "Sorry, You Have No Authorization To Access This File"}, status=status.HTTP_401_UNAUTHORIZED)




# here in this function based view we will return a specific object or a single company registrar
# based on the passed argument pk (the function requires us to pass the id(pk) alongside the request) 
@api_view(['GET'])
def company_registrar_detail(request, pk):

    # here in the try block we will check if that specific object (company registrar) exists
    # if it exists and user is the owner of the object or user is an admin then we will serialize it and return it as a json 
    # but if it does not exist we will raise [CompanyRegistrar.DoesNotExist] exception
    # or if the user is not the owner of the object, we will return no authorization error

    try:
        # querying the object
        companyRegistrar = CompanyRegistrar.objects.get(id=pk)
        # raising an eception (if the object doesn't exist)
    except CompanyRegistrar.DoesNotExist:
        # returning an error including the exception(s)
        return Response(data= {'Error': 'Unknown Id'},status=status.HTTP_404_NOT_FOUND)

    # here we will check if the current user is related with the queried company_registrar  or is an admin      #Security
    if (request.user.id ==  companyRegistrar.user.id) or request.user.is_admin:
        # serialzie the object if it exists and return it        
        serializer = CompanyRegistrarSerializer(companyRegistrar, many = False) 
        return Response(data = {'Company Registrar':serializer.data},  status=status.HTTP_200_OK) 
    else:
         # if the user is not related to the queried company_registrar or is not an admin
        return Response (data = {'Error': "Sorry, You Have No Authorization To Access This File"}, status=status.HTTP_401_UNAUTHORIZED)



# here in the following function based view we will accept the sent data (from the request object : request.data)
# it is just the body of the http request, it might be as a json(body) or it might be as a form data.
# after receiving the data, we will validate it. if evrything is well and the user is active then we will create a new 
# Company Registrar based on the passes data, and return what has been created as a response.
# but if validation fails or user has no permission we will just return an error response with the raised exceptions   
@api_view(['POST'])
def company_registrar_register(request):

     # here we will check if the current user is active         #Security
    if request.user.is_active:
        
        # here we are overriding the user field from the request, incase it was modified while on transit #Security
        # but if the user is admin, since he/she may create company_registrar on behalf of others , we won't override it
        # we will just accept whatever comes
        if not request.user.is_admin:
            request.data['user'] = request.user.id       
        # serialize the coming data
        serializer = CompanyRegistrarSerializer(data=request.data)
        # validate the serialized data, if true save the object, if false return error
        if serializer.is_valid():
            serializer.save()
        
            return Response(data = {'You Have Successfully Registered The Following Company Registrar':serializer.data}, status = status.HTTP_201_CREATED)
        return Response(data = {'Error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    else:
         # if the user is not active
        return Response (data = {'Error': "Sorry, Your Account Must be Active In order To Access This Feature"}, status=status.HTTP_401_UNAUTHORIZED)




@api_view(['PUT'])
def company_registrar_update(request, pk):
    # here we will update the company registrar that already exists in the system and return HTTP status code 202 to tell the update 
    # operation is successfull
    # but before doing that we need to check the incoming data is valid by using 'is_valid' method from 'rest_framework' on the data(serializer)
    # then we will update the data by calling the save method on the data (serializer)
   

    # here first we will get that object(the one that needs update) first, because we don't want to create new object 
    # we just wanna update the existing one, if it dosn't exist we will raise an eception otherwise we will save it(update it)

    try:
        companyRegistrar = CompanyRegistrar.objects.get(id=pk)

    except CompanyRegistrar.DoesNotExist:
        return Response(data= {'Error': 'Unknown Id'},status=status.HTTP_404_NOT_FOUND)
    
     # here we will check if the current user is related with the queried company_registrar  or is an admin     #Security
    if (request.user.id ==  companyRegistrar.user.id) or request.user.is_admin:
        serializer = CompanyRegistrarSerializer(instance=companyRegistrar,data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response(data = {'You Have Successfully Updated The Folowing Company Registrar': serializer.data}, status = status.HTTP_202_ACCEPTED)
        return Response(data = {'Error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    else:
        # if the user is not related to the queried company_registrar or is not an admin
        return Response (data = {'Error': "Sorry, You Have No Authorization To Modify This File"}, status=status.HTTP_401_UNAUTHORIZED)







@api_view(['DELETE'])
def company_registrar_delete(request, pk):
    # here we will delete the company registrar that already exists in the system (if it exists) and has permission then we will
    # return HTTP status code 200 to tell the delete operation is successfull
    # otherwise we will raise an exception and return it as a response
    try:

        companyRegistrar = CompanyRegistrar.objects.get(id=pk)

    except CompanyRegistrar.DoesNotExist:

        return Response(data = {'Error': 'Unknown Id'},status=status.HTTP_404_NOT_FOUND)
    
    # here we will check if the current user is related with the queried company_registrar  or is an admin      #Security
    if (request.user.id ==  companyRegistrar.user.id) or request.user.is_admin:
        companyRegistrar.delete()
            
        return Response(data = {'Company Registrar Successfully Deleted'}, status = status.HTTP_200_OK)  
    else:
        # if the user is not related to the queried company_registrar or is not an admin
        return Response (data = {'Error': "Sorry, You Have No Authorization To Delete This File"}, status=status.HTTP_401_UNAUTHORIZED)
