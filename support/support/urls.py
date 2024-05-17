from django.contrib import admin
from django.urls import path
from issues.api import (IssuesAPI, IssuesDeleteAPI, IssuesRetrieveAPI,  # noqa
                        IssuesUpdateAPI)
from rest_framework_simplejwt.views import TokenObtainPairView  # noqa
from rest_framework_simplejwt.views import token_obtain_pair  # noqa
from users.api import UserListCreateAPI, UsersDeleteAPI, UsersRetrieveUpdateAPI

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", UserListCreateAPI.as_view()),
    path("issues/", IssuesAPI.as_view()),
    path("issues/get/<int:id>", IssuesRetrieveAPI.as_view()),
    path("issues/update/<int:id>", IssuesUpdateAPI.as_view()),
    path("issues/delete/<int:id>", IssuesDeleteAPI.as_view()),
    path("users/<int:id>", UsersRetrieveUpdateAPI.as_view()),
    path("users/delete/<int:id>", UsersDeleteAPI.as_view()),
    # Authentification
    # path("auth/token/", token_obtain_pair),
    path("auth/token/", TokenObtainPairView.as_view()),
]
