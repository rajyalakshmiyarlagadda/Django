from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


# Create your models here.
class UserImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(UserImage, self).save(*args, **kwargs)  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.image.path)    

# @receiver(post_save, sender=User)
# def create_userimage(*args, **kwargs):
#     print("I am in models signalas    ***********************",args,kwargs)
    
#     # if created:
#     #     UserImage.objects.create(user=instance)
#     #     print('USer image created')

# # post_save.connect(create_userimage, sender=User)

         

