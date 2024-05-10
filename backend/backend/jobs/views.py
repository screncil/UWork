from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from jobs.models import Job
from jobs.serializers import JobSerializer

from countries.models import Countries
from cities.models import Cities
from categories.models import Category

from django.contrib.auth import get_user_model

from .models import Job



# Create your views here.


class JobView(APIView):

    def get(self, request):
        if "id" in request.query_params:
            try:
                companies = Job.objects.get(id=request.query_params['id'])
                serializer = JobSerializer(companies)
                return Response(serializer.data)
            except Job.DoesNotExist:
                return Response({"error": "Job not found"},status=status.HTTP_404_NOT_FOUND)

        companies = Job.objects.all()
        serializer = JobSerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddJobView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.group == "company":
            lst = []
            required_fields = ['title', 'description', 'category', 'requirements', 'offer', 'salary', 'country', 'city']
            for field in required_fields:
                if field not in request.data:
                    lst.append(field)
            if len(lst) > 0:
                return Response({"required": lst}, status=status.HTTP_400_BAD_REQUEST)
            else:
                job = Job.objects.create(
                    title=request.data['title'],
                    description=request.data['description'],
                    category=Category.objects.get(code=request.data['category']),
                    requirements=request.data['requirements'],
                    offer=request.data['offer'],
                    salary=request.data['salary'],
                    country=Countries.objects.get(code=request.data['country']),
                    city=Cities.objects.get(name=request.data['city']),
                    owner=get_user_model().objects.get(id=request.user.id)
                )

                job.save()

                return Response({"message": "job created"}, status=status.HTTP_201_CREATED)

        else:
            return Response({"error": "not company"})