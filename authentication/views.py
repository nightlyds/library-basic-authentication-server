from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import CustomUserSerializer, AuthenticationLoginSerializer


class AuthenticationListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class AuthenticationLogin(APIView):

    serializer_class = AuthenticationLoginSerializer
    parser_classes = [JSONParser, MultiPartParser]

    def post(self, request, format=None):    
        user = authenticate(username=request.data.get('email'), password=request.data.get('password'))

        if user is not None:
            return Response({'isauthenticated': True, 'user': user.to_dict()})
        
        return Response({'isauthenticated': False})


class AuthenticationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

