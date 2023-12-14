from typing import Any
from django.db import models
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from news.models import NewsStory

from .models import CustomUser
from .forms import CustomUserCreationForm, UserUpdateForm

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:password_success')
    template_name= 'registration/change-password.html'


def password_success(request):
     return render(request, 'registration/password_success.html', {})


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
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
