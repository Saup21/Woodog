from django.utils import regex_helper
from .views import EmailValidationView, LoginView, LogoutView, RegistrationView, UsernameValidationView, VerificationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/<str:type_of>',RegistrationView.as_view(), name='register'),
    path('login',LoginView.as_view(), name='login'),
    path('logout',LogoutView.as_view(), name='logout'),
    path("validate-username", csrf_exempt(UsernameValidationView.as_view()), 
    name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), 
    name="validate-email"),
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name='activate'),
]
