from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views


app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('profile/<slug:username>/', login_required(views.UserProfilePage.as_view(), login_url='login'), name='userProfile'),
]
