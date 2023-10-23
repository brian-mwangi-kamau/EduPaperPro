from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('upload/', views.upload_form, name="form_upload"),
    path('download/<int:form_id>/', views.download_forms, name='download_forms'),
    path('preview_description/<int:form_id>/', views.preview_description, name='preview_description'),
    path('edit-resources/', views.edit_resources, name='edit_resources'),
]

