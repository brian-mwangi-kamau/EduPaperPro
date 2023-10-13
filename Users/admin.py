from django.contrib import admin
from .models import CustomUser, UserAccount


admin.site.register(CustomUser)
admin.site.register(UserAccount)