from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    postDate = models.DateTimeField(default=timezone.now)
    content = models.TextField()

