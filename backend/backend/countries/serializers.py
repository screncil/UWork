from rest_framework import serializers

from .models import Countries


class CountryForCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['name', 'image']


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = '__all__'