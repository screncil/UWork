from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Company
from .serializers import CompanySerializer



class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
