from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from article.models import ArticlePost, Tag
from django.core.paginator import Paginator
import markdown




# Create your views here.


def article_list(request):
    page = request.GET.get('page' , 1)
    articles = ArticlePost.objects.all()
    paginator = Paginator(articles, 10)
    articles = paginator.get_page(page)
    context = {}
    tags = Tag.objects.all()
    context['articles'] = articles
    context['tags'] = tags
    return render(request, 'article/list.html', context)

def article_detail(request, id):
    context = {}
    article = get_object_or_404(ArticlePost, pk=id)
    article.read_number += 1
    article.save()
    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
    ])
    context['article'] = article
    return render(request, 'article/detail.html', context)

def articles_with_tag(request, tag_pk):
    context = {}
    tag = get_object_or_404(Tag, pk=tag_pk)
    articles = ArticlePost.objects.filter(tag=tag)
    context['articles'] = articles
    context['tag'] = tag
    context['tags'] = Tag.objects.all()
    return render(request, 'article/tag_list.html', context)
