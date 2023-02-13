from .serializers import RegistrantSerializer
from registrant.models import Registrant
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# In this class we will decalre a bunch of function based views that are gonna handle 
# the different API endpoints regarding Registrants
# in short they are just methods that will just accept a [request] and parameters and return accordingly

@api_view(['GET'])          
def registrant_list(request):
    
    # here we are feching and return all the registered registrants under a certain individal_registrar or company_registrar
    # (in short we will return all results related with the current user , and we will get the current user from the request (request.user))

    registrant = Registrant.objects.filter(user__id= request.user.id)
    # then we will serialize what we get from the query, in order to return them as a json
    # and we will set the 'many' parameter to True, because the serializer might (almost always in this case)
    # be handling a list of objects from the query result (not a single object) 
    # if we set that to false (the default) and the query returns a list then an exception will raise
    # because the serializer by default is expecting a single object  
    serializer  = RegistrantSerializer(registrant, many =True)

    # then we will return the serialized lists in a json format and HTTP status code as well
    return Response(data={'count': registrant.count(),'Registrant List': serializer.data}, status=status.HTTP_200_OK)




# here in this function based view we will return a specific object or a single registrant
# based on the passed argument pk (the function requires us to pass the id(pk) alongside the request) and
# the current user's authorization to access (view) that registrant's detail
@api_view(['GET'])
def registrant_detail(request, pk):

    # here in the try block we will check if that specific object (registrant) exists
    # if it exists and the requester (user) is the owner (has authorization) we will serialize it and return it as a json 
    # but if it does not exist we will raise [CompanyRegistrar.DoesNotExist] exception, and if the user has no 
    # authorization we will return error

    try:
        # querying the object
        registrant = Registrant.objects.get(id=pk)
        # raising an eception (if the object doesn't exist)
    except Registrant.DoesNotExist:
        # returning an error including the exception(s)
        return Response(data= {'Error': 'Unknown Id'},status=status.HTTP_404_NOT_FOUND)

    # checking if the user is the owner of the registrant (or has access to view the registarnt)
    if registrant.user.id == request.user.id:
        
        # the user has permission so serialzie the object and return it        
        serializer = RegistrantSerializer(registrant, many = False) 
        return Response(data = {'Registrant':serializer.data},  status=status.HTTP_200_OK) 
    else:
        # the user has no permission so return an error       
        return Response (data = {'Error': "Sorry, You Have No Authorization To Access This File"}, status=status.HTTP_401_UNAUTHORIZED)


# here in the following function based view we will accept the sent data (from the request object : request.data)
# it is just the body of the http request, it might be as a json(body) or it might be as a form data.
# after receiving the data, we will validate it and if evrything is well we will create a new Registrant based on
# the passes data & the current user, and return what has been created as a response.
# but if validation fails we will just return an error response with the raised exceptions   
@api_view(['POST'])
def registrant_register(request):
    # here we will override the 'user' field from the coming data with the current user, to relate it with the registrant
    # when the request.data comes there might (might not) be the 'user' field, we don't care we will just ovveride it
    # when the request came.
    # we do that because, we need to make sure every registrar is able to create registrant under his/her name only!
    request.data['user'] = request.user.id
   
    
    # serialize the incoming data (including the modeified field - 'user' field )
    serializer = RegistrantSerializer(data=request.data)
    # validate the serialized data, if true save the object, if false return an error
    if serializer.is_valid():
        serializer.save()
    
        return Response(data = {'You Have Successfully Registered The Following Registrant':serializer.data}, status = status.HTTP_201_CREATED)
    return Response(data = {'Error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def registrant_update(request, pk):
    # here we will update the registrant that already exists in the system and return HTTP status code 202 to tell the update 
    # operation is successfull
    # but before doing that we need to check the incoming data is valid by using 'is_valid' method from 'rest_framework' on the data(serializer)
    # then we will update the data by calling the save method on the data (serializer)
   

    # here first we will get that object(the one that needs update) first, because we don't want to create new object 
    # we just wanna update the existing one. 
    # if it dosn't exist or the current user is not the owner of the registrant we will raise an eception 
    # otherwise we will save it(update it)

    # check if the object exists
    try:
        registrant = Registrant.objects.get(id=pk)
    # raise an exception if it does not exist
    except Registrant.DoesNotExist:
        return Response(data= {'Error': 'Unknown Id'},status=status.HTTP_404_NOT_FOUND)
    
    # check if the current user is the owner(creater) of the object
    if registrant.user.id == request.user.id:
        # if he/she is , then serialize it, validate it and save it
        serializer = RegistrantSerializer(instance=registrant,data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response(data = {'You Have Successfully Updated The Folowing Registrant': serializer.data}, status = status.HTTP_202_ACCEPTED)
        # if the validation fails return an error 
        return Response(data = {'Error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    else:
        # if he/se is not return an error
        return Response (data = {'Error': "Sorry, You Have No Authorization To Modify This File"}, status=status.HTTP_401_UNAUTHORIZED)






@api_view(['DELETE'])
def registrant_delete(request, pk):
    # here we will delete the registrant that already exists in the system (if it exists and the current user is the owner)
    #  and return HTTP status code 200 to tell the delete operation is successfull
    # otherwise we will raise an eception and return it as a response
   
    # checking if the object exists
    try:

        registrant = Registrant.objects.get(id=pk)

    # raise an error if it doesn't exist
    except Registrant.DoesNotExist:

        return Response(data = {'Error': 'Unknown Id'},status=status.HTTP_404_NOT_FOUND)
    
    # check if the current user has permission to delete this registrant (if the registrant is created under his/her name)
    if registrant.user.id == request.user.id:
        
        # if it is delete the object
        registrant.delete()
        return Response(data = {'Registrant Successfully Deleted'}, status = status.HTTP_200_OK)
    else:
        # if it is not return no authorization error
        return Response (data = {'Error': "Sorry, You Have No Authorization To Delete This File"}, status=status.HTTP_401_UNAUTHORIZED)