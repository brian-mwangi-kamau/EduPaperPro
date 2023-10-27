from django.urls import path
from . import views

urlpatterns = [
    path('sub/', views.subscription_initiation, name="subscription"),
]