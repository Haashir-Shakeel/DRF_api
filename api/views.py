from django.shortcuts import render
from rest_framework import status, viewsets
from api.models import Book
from api.serializers import BookSerializer, UserSerializer
from django.contrib.auth.models import User


# Create your views here.

class BookView(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class = BookSerializer

class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer
