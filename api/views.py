from django.shortcuts import render
from rest_framework import status, viewsets
from api.models import Book
from api.serializers import BookSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class BookView(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes =[IsAuthenticated]
    

class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer
