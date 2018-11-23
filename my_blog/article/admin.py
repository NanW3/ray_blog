from django.contrib import admin

# Register your models here.
from .models import ArticlePost
from .models import Tag
from .models import ReadNum

admin.site.register(Tag)
admin.site.register(ReadNum)
@admin.register(ArticlePost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'author', 'created')