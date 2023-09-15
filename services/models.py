from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    service_code = models.PositiveIntegerField()
    description_services = models.CharField(max_length=200)


class ServiceUser(models.Model):
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    assignation_date = models.DateTimeField(auto_now_add=True)
