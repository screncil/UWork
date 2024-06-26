

from django.urls import path

from .views import *

urlpatterns = [
    path("user/register", RegisterUser.as_view(), name="register-user"),
    path("user/login", LoginUser.as_view(), name="login-user"),
    path("users", AllUsersView.as_view(), name="user-list"),
    path("user", GetUserView.as_view(), name="user-detail"),
    path("user/logout", LogoutUser.as_view(), name="logout-user"),
    path("user/update_photo", UpdatePhotoUserView.as_view(), name="update-user-photo")
]