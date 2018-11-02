from django.contrib import admin

# Register your models here.
from .models import ArticlePost
from .models import Tag

admin.site.register(Tag)
@admin.register(ArticlePost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')