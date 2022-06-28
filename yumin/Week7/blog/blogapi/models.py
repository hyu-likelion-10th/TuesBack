from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    postDate = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.title)
