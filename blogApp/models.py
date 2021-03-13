from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_like')
    date_posted = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-date_posted', )

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()    

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

   
