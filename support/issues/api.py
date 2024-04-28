import json

from django.shortcuts import get_object_or_404
from issues.models import Issue
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"


@api_view()
def get_issues(request) -> Response:
    issues = Issue.objects.all()
    results = [IssueSerializer(issue).data for issue in issues]

    return Response(data={"results": results})


@api_view()
def retrieve_issue(request, issue_id: int) -> Response:
    instance = get_object_or_404(Issue, id=issue_id)

    return Response(data={"results": IssueSerializer(instance).data})


@api_view(["POST"])
def create_issue(request) -> Response:
    try:
        payload: dict = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        raise Exception("Request Body is invalid")

    serializer = IssueSerializer(data=payload)
    serializer.is_valid(raise_exception=True)

    issue = Issue.objects.create(**serializer.validated_data)

    return Response(data=IssueSerializer(issue).data)
