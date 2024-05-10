from rest_framework import serializers

from .models import Job

from companies.serializers import CompanySerializer


class AddJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'category', 'requirements', 'offer', 'salary', 'country', 'city', 'owner']


class JobSerializer(serializers.ModelSerializer):

    owner = CompanySerializer(read_only=True)
    country = serializers.StringRelatedField(read_only=True)
    city = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'category', 'requirements', 'offer', 'salary', 'country', 'city', 'owner']

