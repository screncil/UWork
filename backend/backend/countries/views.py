from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import Countries
from .serializers import CountrySerializer


# Create your views here.


class CountryModelView(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer