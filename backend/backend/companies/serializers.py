from rest_framework import serializers

from countries.serializers import CountryForCompanySerializer
from .models import Company



class CompanySerializer(serializers.ModelSerializer):

    country = serializers.StringRelatedField(read_only=True)
    city = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'phone', 'email', 'country', 'city']