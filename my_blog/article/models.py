from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.tag_name)

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    read_number = models.IntegerField(default=0)
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s %s %s' % (self.title, self.author, self.created)

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.objects.id])

