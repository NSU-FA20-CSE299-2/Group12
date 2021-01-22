from django.shortcuts import render
from django.views.generic import DetailView, CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProfileCreationForm
from .models import Profile

# Create your views here.


class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

    template_name = 'home.html'


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')

    model = Profile
    template_name = 'profile.html'


class RegistrationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('register_success')


class RegisterSuccessView(TemplateView):
    template_name = 'register_success.html'


class EditView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')

    model = Profile
    fields = ('age', 'weight', 'height')
    template_name = 'edit_view.html'
    success_url = reverse_lazy('home')
