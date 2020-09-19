from django.db import models
from django.urls import reverse

from user.models import UserAccount
from django.conf import settings


def upload_location(instance, filename):
    file_path = 'media/{user_id}/{filename}'.format(user_id=instance.author.id, filename=filename)
    return file_path

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse('media:homepage',kwargs={'id':self.id})

    class Meta:
        ordering = ['-date_modified']





class Media(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    files = models.ImageField(upload_to=upload_location, blank=True, null=True)