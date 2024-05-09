from django.contrib import admin
from django.urls import path
from issues.api import IssuesAPI, IssuesRetrieveUpdateDeleteAPI
from rest_framework_simplejwt.views import TokenObtainPairView  # noqa
from rest_framework_simplejwt.views import token_obtain_pair  # noqa
from users.api import UsersRetrieveUpdateDeleteAPI, create_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", create_user),
    path("issues/", IssuesAPI.as_view()),
    path("issues/<int:id>", IssuesRetrieveUpdateDeleteAPI.as_view()),
    path("users/<int:id>", UsersRetrieveUpdateDeleteAPI.as_view()),
    # Authentification
    # path("auth/token/", token_obtain_pair),
    path("auth/token/", TokenObtainPairView.as_view()),
]
