from rest_framework import serializers

from django.contrib.auth import get_user_model



class CompanySerializer(serializers.ModelSerializer):

    country = serializers.StringRelatedField(read_only=True)
    city = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'phone_number', 'email', 'country', 'city', 'address', 'img_url']