from django.urls import path, include

from .views import HomePageView, RegistrationView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('register_success/', RegistrationView.as_view(), name='register_success'),
]
