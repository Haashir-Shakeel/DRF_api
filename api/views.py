from django.shortcuts import render
from rest_framework import status, viewsets
from api.models import Book
from api.serializers import BookSerializer



# Create your views here.

class BookView(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
