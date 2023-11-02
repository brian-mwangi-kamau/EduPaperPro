from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_page, name='subscription_page'),
    path('payment/1/', views.subscription_initiation_monthly, name='subscription_monthly'),
    path('payment/2/', views.subscription_initiation_yearly, name='subscription_yearly'),
]