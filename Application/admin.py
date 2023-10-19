from django.contrib import admin
from .models import Resource, DownloadRecord


admin.site.register(Resource)
admin.site.register(DownloadRecord)