from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import NewsStory
from users.models import CustomUser
from .forms import StoryForm, EditStoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class UpdateStoryView(UpdateView):
    model = NewsStory
    form_class = EditStoryForm
    template_name = 'news/update_story.html'
    
    
class AuthorStoryView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_stories'

    def get_queryset(self):
        self.username = get_object_or_404(CustomUser, username=self.kwargs['username'])
        return NewsStory.objects.filter(author=self.username)


    