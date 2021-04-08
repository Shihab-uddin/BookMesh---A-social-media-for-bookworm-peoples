from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
""" from ckeditor.fields import RichTextField """

# Create your models here.

class Post(models.Model):
    content     = models.CharField(max_length=200)
    image       = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)

