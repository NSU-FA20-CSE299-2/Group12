from django.shortcuts import render
from django.views.generic import DetailView, CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy

from .forms import ProfileCreationForm
from .models import Profile

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'


class RegistrationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('register_success')


class RegisterSuccessView(TemplateView):
    template_name = 'register_success.html'


class EditView(UpdateView):
    model = Profile
    fields = ('age', 'weight', 'height')
    template_name = 'edit_view.html'
    success_url = reverse_lazy('home')
