from django.contrib import admin
from services.models import ServiceUser, Service

# Register your models here.
admin.register(Service)
admin.register(ServiceUser)
