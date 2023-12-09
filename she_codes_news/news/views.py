from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import NewsStory
from users.models import CustomUser
from .forms import StoryForm


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
    

class AuthorStoryView(generic.DetailView):
<<<<<<< Updated upstream
    model = NewsStory
    template_name = 'news/index.html'
    context_object_name = 'latest_stories'

    def get_queryset(self):
        return super().get_queryset()

=======
    model = CustomUser
    template_name = 'news/index.html'
    context_object_name = 'latest_stories'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_queryset(self):
        # Get the username from the URL parameter
        username = self.kwargs.get('username', None)

        # use the username to filter CustomUser and get the primary key
        author = CustomUser.objects.get(username=username)
        author_id = author.pk

        # Use the author_id to filter NewsStory objected related to the author
        queryset = NewsStory.objects.filter(author_id=author_id)              
        return queryset
>>>>>>> Stashed changes
  