from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
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
        return reverse('post_detail', kwargs={'the_slug': self.slug})

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug: 
        instance.slug = slugify(instance.title, allow_unicode=True)

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comments = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

   
