from django.db.models import Q
from rest_framework import generics, permissions, serializers
from users.enums import Role

from .enums import Status
from .models import Issue


class IsAdminSeniorUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.user.role == "senior"


class IssueSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(required=False)
    junior = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Issue
        fields = "__all__"

    def validate(self, attrs):
        attrs["status"] = Status.OPENED
        return attrs


class IssuesAPI(generics.ListCreateAPIView):
    http_method_names = ["get", "post"]
    serializer_class = IssueSerializer

    def get_queryset(self):
        if self.request.method == "GET":
            if self.request.user.role == Role.JUNIOR:
                return Issue.objects.filter(junior=self.request.user.id)

            elif self.request.user.role == Role.SENIOR:
                return Issue.objects.filter(
                    Q(senior=self.request.user.id) | Q(senior__isnull=True)
                )

            elif self.request.user.role == Role.ADMIN:
                return Issue.objects.all()

        elif self.request.method == "POST":
            return Issue.objects.all()

    def get(self, request):
        return super().get(request)

    def post(self, request):
        if request.user.role == Role.SENIOR:
            raise Exception("The role is Senior")
        return super().post(request)


class IssuesRetrieveAPI(generics.RetrieveAPIView):
    http_method_names = ["get"]
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    lookup_url_kwarg = "id"


class IssuesUpdateAPI(generics.UpdateAPIView):
    http_method_names = ["put"]
    serializer_class = IssueSerializer
    permission_classes = [IsAdminSeniorUser]
    queryset = Issue.objects.all()
    lookup_url_kwarg = "id"


class IssuesDeleteAPI(generics.DestroyAPIView):
    http_method_names = ["delete"]
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Issue.objects.all()
    lookup_url_kwarg = "id"
