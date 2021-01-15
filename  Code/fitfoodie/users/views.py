from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy

from .forms import ProfileCreationForm
from .models import Profile

# Create your views here.


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'


class RegistrationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('register_success')
