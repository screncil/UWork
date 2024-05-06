from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from .serializers import UserSerializer


class RegisterUser(APIView):

    def post(self, request):
        if "username" not in request.data:
            return Response({'error': 'username required'}, status=status.HTTP_400_BAD_REQUEST)

        if "password" not in request.data:
            return Response({'error': 'password required'}, status=status.HTTP_400_BAD_REQUEST)

        if "email" not in request.data:
            return Response({'error': 'email required'}, status=status.HTTP_400_BAD_REQUEST)

        if "first_name" not in request.data:
            return Response({'error': 'first name required'}, status=status.HTTP_400_BAD_REQUEST)

        if "last_name" not in request.data:
            return Response({'error': 'last name required'}, status=status.HTTP_400_BAD_REQUEST)

        if "age" not in request.data:
            return Response({'error': 'age required'}, status=status.HTTP_400_BAD_REQUEST)

        if "gender" not in request.data:
            return Response({'error': 'gender required'}, status=status.HTTP_400_BAD_REQUEST)


        User = get_user_model()

        if User.objects.filter(username=request.data["username"]).exists():
            return Response({'error': 'user already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.age = request.data['age']
        user.gender = request.data['gender']
        user.img_url = None if "img_url" not in request.data else request.data['img_url']
        user.save()

        return Response({'message': 'user created'})


class LoginUser(APIView):

    def post(self, request):

        if "username" not in request.data:
            return Response({'error': 'username required'}, status=status.HTTP_400_BAD_REQUEST)

        if "password" not in request.data:
            return Response({'error': 'password required'}, status=status.HTTP_400_BAD_REQUEST)


        user = authenticate(username=request.data['username'], password=request.data['password'])

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class AllUsersView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class GetUserView(APIView):

    def get(self, request):

        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
        else:
            return Response({'error': 'not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'user': serializer.data})