import csv

from rest_framework import viewsets
from rest_framework.response import Response
from services.Api.serializers import UploadCheckSerializer, ServiceUploadSerializer


class UploadCheckViewSet(viewsets.ViewSet):
    serializer_class = UploadCheckSerializer

    def create(self, request):
        file_uploaded = request.FILES.get('file')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)


class ServiceUploadViewSet(viewsets.ViewSet):
    serializer_class = ServiceUploadSerializer

    def create(self, request):
        file_uploaded = request.FILES.get('file')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)