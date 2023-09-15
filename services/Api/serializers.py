from django.core.validators import FileExtensionValidator
from rest_framework.serializers import Serializer, FileField


# Serializers define the API representation.
class UploadCheckSerializer(Serializer):
    file = FileField(validators=[FileExtensionValidator(['csv'])])

    class Meta:
        fields = ['file']


class ServiceUploadSerializer(Serializer):
    file = FileField(validators=[FileExtensionValidator(['csv'])])

    class Meta:
        fields = ['file']
