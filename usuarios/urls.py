from django.urls import path
from django.views.generic import TemplateView

from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('success', TemplateView.as_view(template_name='usuarios/success_registration.html'), name='success')
    
]