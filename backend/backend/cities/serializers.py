from rest_framework import serializers

from .models import Cities



class CompanyCitySerializer(serializers.Serializer):

   name = serializers.CharField(max_length=255)


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Cities
        fields = ['id', 'name']