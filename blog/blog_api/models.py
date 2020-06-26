from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, default='')
    content = models.TextField()
    summary = models.CharField(max_length=200, default='')
    published = models.DateTimeField(auto_now_add=True)
    video_embed = models.CharField(max_length=400, default='')
    author = models.CharField(max_length=100, default='Conor Bailey')
    image_source = models.CharField(max_length=400, default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published']
