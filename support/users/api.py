import json

from django.contrib.auth import get_user_model
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, serializers

from .enums import Role
from .models import User  # noqa

User = get_user_model()  # noqa


@csrf_exempt
def create_user(request: HttpRequest) -> JsonResponse:
    if request.method != "POST":
        raise NotImplementedError("Only POST requests")

    data: dict = json.loads(request.body)
    user = User.objects.create_user(**data)

    results = {
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": user.role,
        "is_active": user.is_active,
    }

    return JsonResponse(results)


class UserSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(required=False)
    junior = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = "__all__"


class UsersAPI(generics.ListCreateAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self, request):
        if request.user.role == Role.SENIOR:
            raise Exception("The role is Senior")
        return super().post(request)


class UsersRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ["get", "put"]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "id"
