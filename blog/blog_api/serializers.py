from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'summary','video_embed', 'content',
                  'published', 'author', 'image_source']
