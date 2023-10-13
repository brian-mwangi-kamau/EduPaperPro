from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload/', views.upload_form, name="form_upload"),
    path('download/<int:form_id>/', views.download_forms, name='download_forms'),
]

