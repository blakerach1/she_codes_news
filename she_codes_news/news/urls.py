from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', login_required(views.AddStoryView.as_view(), login_url='login'), name='newStory'),
    path('author/<username>/', views.AuthorStoryView.as_view(), name='authorStories'),
]
