from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar      = models.ImageField(default='avatar.png', upload_to='avatars/')
    friends     = models.ManyToManyField(User, blank=True, related_name='friends')
    updated     = models.DateTimeField(auto_now=True)
    created     = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} profile'
