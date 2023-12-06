from typing import Any
from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser
from .forms import CustomUserCreationForm, UserUpdateForm


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'


class UserProfilePage(DetailView):
    model = get_user_model()
    template_name = 'users/profile.html'
    context_object_name = 'user_profile'
    slug_field = 'username'
    slug_url_kwarg = 'username'

