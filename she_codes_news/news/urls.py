from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
<<<<<<< Updated upstream
    path('author/<author>/', views.AuthorStoryView.as_view(), name='authorStory'),
=======
    path('author/<slug:username>/', views.AuthorStoryView.as_view(), name='authorStories'),
>>>>>>> Stashed changes
]
