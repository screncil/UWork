from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from jobs.models import Job
from jobs.serializers import AddJobSerializer, JobSerializer


# Create your views here.


class JobView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class AddJobView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request):
        if request.user.group == "company":
            serializer = AddJobSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Job added"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "user cannot add job"}, status=status.HTTP_400_BAD_REQUEST)