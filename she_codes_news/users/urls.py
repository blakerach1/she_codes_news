from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('profile/<slug:username>/', views.UserProfilePage.as_view(), name='userProfile'),
    path('password/', login_required(views.PasswordsChangeView.as_view(), login_url='login'), name="changePassword"),
    path('password_success', views.password_success, name="password_success"),
]
