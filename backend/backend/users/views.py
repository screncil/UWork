from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from django.contrib.auth import authenticate, logout
from django.contrib.auth import get_user_model

from .serializers import UserSerializer


class RegisterUser(APIView):

    def post(self, request):
        lst = []
        required_fields = ['username', 'password', 'email', 'first_name', 'last_name', 'age', 'gender']
        for field in required_fields:
            if field not in request.data:
                lst.append(field)

        if len(lst) > 0:
            return Response({"required": lst}, status=status.HTTP_400_BAD_REQUEST)
        else:
            User = get_user_model()

            if User.objects.filter(username=request.data["username"]).exists():
                return Response({'error': 'user already exists'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.age = request.data['age']
            user.gender = request.data['gender']
            user.img_url = None if "img_url" not in request.data else request.data['img_url']
            user.group = "user"
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



class AllUsersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = get_user_model().objects.filter(group="user")
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class GetUserView(APIView):

    def get(self, request):

        if request.user.is_authenticated:
            if request.user.group == "user":
                serializer = UserSerializer(request.user)
            else:
                return Response({'error': "Not user"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.data)



class LogoutUser(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({'message': 'logged out successfully'}, status=status.HTTP_200_OK)