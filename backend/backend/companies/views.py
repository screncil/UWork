from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from .serializers import CompanySerializer

from countries.models import Countries
from cities.models import Cities



class CompanyList(APIView):

    def get(self, request):
        if "id" in request.query_params:
            try:
                companies = get_user_model().objects.filter(group="company").get(id=request.query_params['id'])
                serializer = CompanySerializer(companies)
                return Response(serializer.data)
            except get_user_model().DoesNotExist:
                return Response({"error": "Company not found"},status=status.HTTP_404_NOT_FOUND)

        companies = get_user_model().objects.filter(group="company")
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RegisterCompany(APIView):

    def post(self, request):
        if "username" not in request.data:
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)

        if "email" not in request.data:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        if "password" not in request.data:
            return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)

        if "country" not in request.data:
            return Response({"error": "Country is required"}, status=status.HTTP_400_BAD_REQUEST)

        if "city" not in request.data:
            return Response({"error": "City is required"}, status=status.HTTP_400_BAD_REQUEST)

        if "phone_number" not in request.data:
            return Response({"error": "Phone is required"}, status=status.HTTP_400_BAD_REQUEST)

        if "address" not in request.data:
            return Response({"error": "Address is required"}, status=status.HTTP_400_BAD_REQUEST)


        User = get_user_model()

        if User.objects.filter(username=request.data["username"]).exists():
            return Response({'error': 'Company already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user("_".join(request.data['username'].split()), request.data['email'], request.data['password'])
        user.img_url = None if "img_url" not in request.data else request.data['img_url']
        user.group = "company"
        user.address = request.data['address']
        user.phone_number = request.data['phone_number']
        user.country = Countries.objects.get(code=request.data['country'])
        user.city = Cities.objects.get(name=request.data['city'])
        user.save()

        return Response({"message": "company created"})


class CompanyDetail(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.group == "company":
                serializer = CompanySerializer(request.user)
            else:
                return Response({"error": "Not company"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.data)