from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('filter_items/', views.filter_items, name='filter_items'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload_form, name="form_upload"),
    path('download/<int:form_id>/', views.download_forms, name='download_forms'),
    path('preview_description/<int:form_id>/', views.preview_description, name='preview_description'),
    path('admin-resources/', views.admin_resources, name='admin_resources'),
    path('delete/<int:form_id>', views.delete_resource, name='delete-resource'),
    path('update/<int:form_id>', views.update_resource, name='update-resource'),
]

