from django.contrib import admin
from services.models import ServiceUser, Service

# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceUser)
