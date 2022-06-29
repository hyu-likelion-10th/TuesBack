from pyexpat import model
from rest_framework import serializers
from .models import Post
from django.utils import timezone

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "postDate", "content")
