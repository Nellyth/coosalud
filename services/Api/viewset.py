from rest_framework import viewsets
from rest_framework.response import Response
from services.Api.serializers import UploadCheckSerializer, ServiceUploadSerializer
from services.Api.utils import read_csv_of_request
from services.models import Service


class UploadCheckViewSet(viewsets.ViewSet):
    serializer_class = UploadCheckSerializer

    def create(self, request):
        file_uploaded = request.FILES.get('file')
        csv_list = read_csv_of_request(file_uploaded)
        print(csv_list)
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)


class ServiceUploadViewSet(viewsets.ViewSet):
    serializer_class = ServiceUploadSerializer
    HEADER = ["Codigo", "Nombre", "Cobertura"]

    def create(self, request):
        file_uploaded = request.FILES.get('file')
        csv_list = read_csv_of_request(file_uploaded)
        self.save_data_model(csv_list)
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)

    def save_data_model(self, csv_list):
        for instance in csv_list:
            if self.HEADER[0] not in instance and self.HEADER[1] not in instance and self.HEADER[2] not in instance:
                if instance[0].isnumeric():
                    Service.objects.get_or_create(service_code=instance[0], description_services=instance[1])
