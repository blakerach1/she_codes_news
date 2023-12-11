from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('news:story', kwargs={"pk": self.pk})
    

# add comments and categories within news app rather than creating separate app