from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Countries
from .serializers import CountrySerializer


# Create your views here.


class CountryModelView(viewsets.ViewSet):

    def list(self, request, pk):
        try:
            queryset = Countries.objects.get(pk=pk)
            serializer = CountrySerializer(queryset)
            return Response(serializer.data)
        except Countries.DoesNotExist:
            raise Http404
