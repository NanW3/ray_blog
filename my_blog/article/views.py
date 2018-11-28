from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.db.models import Count
from article.models import ArticlePost, Tag, ReadNum
from comments.models import Comment
from comments.forms import CommentForm
import markdown




# Create your views here.


def article_list(request):
    page = request.GET.get('page' , 1)
    articles = ArticlePost.objects.all()
    paginator = Paginator(articles, 10)
    articles = paginator.get_page(page)
    cur_num = articles.number
    page_range = list(range(max(cur_num - 2, 1), min(cur_num + 2, articles.paginator.num_pages) + 1))

    if cur_num - 2 > 2:
        page_range.insert(0, '...')
        page_range.insert(0, 1)
    elif cur_num - 2 == 2:
        page_range.insert(0, 1)

    if cur_num + 2 < paginator.num_pages - 1:
        page_range.append('...')
        page_range.append(paginator.num_pages)
    elif cur_num + 2 == paginator.num_pages - 1:
        page_range.append(paginator.num_pages)
    context = {}
    context['articles'] = articles
    context['tags'] = Tag.objects.annotate(article_count=Count('articlepost'))
    context['page_range'] = page_range
    return render(request, 'article/list.html', context)

def article_detail(request, id):
    context = {}
    article = get_object_or_404(ArticlePost, pk=id)
    if not request.COOKIES.get("read_%s" % id):
        if ReadNum.objects.filter(articlepost=article).count():
            readnum = ReadNum.objects.get(articlepost=article)
        else:
            readnum = ReadNum(articlepost=article)
        readnum.read_num += 1
        readnum.save()
    article.save()
    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
    ])
    article_content_type = ContentType.objects.get_for_model(article)
    comments = Comment.objects.filter(content_type=article_content_type, object_id=id)
    context['next_article'] = ArticlePost.objects.filter(created__gt=article.created).last()
    context['previous_article'] = ArticlePost.objects.filter(created__lt=article.created).first()
    context['article'] = article
    context['read'] = article.read_number
    context['comments'] = comments
    context['comment_form'] = CommentForm(initial={'content_type':article_content_type.model, 'object_id': article.id})
    response = render(request, "article/detail.html", context)
    response.set_cookie("read_%s" % article.id, "true")
    return response

def articles_with_tag(request, tag_pk):
    tag = get_object_or_404(Tag, pk=tag_pk)
    page = request.GET.get('page', 1)
    articles = ArticlePost.objects.filter(tag=tag)
    paginator = Paginator(articles, 10)
    articles = paginator.get_page(page)
    cur_num = articles.number
    page_range = list(range(max(cur_num - 2, 1), min(cur_num + 2, articles.paginator.num_pages) + 1))

    if cur_num - 2 > 2:
        page_range.insert(0, '...')
        page_range.insert(0, 1)
    elif cur_num - 2 == 2:
        page_range.insert(0, 1)

    if cur_num + 2 < paginator.num_pages - 1:
        page_range.append('...')
        page_range.append(paginator.num_pages)
    elif cur_num + 2 == paginator.num_pages - 1:
        page_range.append(paginator.num_pages)
    context = {}
    context['tag'] = tag
    context['articles'] = articles
    context['tags'] = Tag.objects.annotate(article_count=Count('articlepost'))
    context['page_range'] = page_range
    return render(request, 'article/tag_list.html', context)
