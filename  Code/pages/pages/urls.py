from .views import HomePageView, AboutPageView, LoginPageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', LoginPageView.as_view(), name='login'),
]
