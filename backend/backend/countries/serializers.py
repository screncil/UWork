from rest_framework import serializers

from .models import Countries



class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = '__all__'