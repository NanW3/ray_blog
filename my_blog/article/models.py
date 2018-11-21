from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING)
    read_number = models.IntegerField(default=0)
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.objects.id])

