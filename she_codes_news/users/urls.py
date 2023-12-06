from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('profile/<slug:username>/', views.UserProfilePage.as_view(), name='userProfile'),
]
