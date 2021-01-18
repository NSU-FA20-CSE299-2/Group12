from django.urls import path, include

from .views import HomePageView, RegistrationView, RegisterSuccessView, ProfileView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('register_success/', RegisterSuccessView.as_view(), name='register_success'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
