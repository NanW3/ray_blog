from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .models import Comment

def update_comment(request):
    referer = request.META.get('HTTP_REFERER', '/')

    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message': 'User need to login', 'redirect_to': referer})
    text = request.POST.get('text', '').strip()
    if text == '':
        return render(request, 'error.html', {'message': 'Empty comment', 'redirect_to': referer})
    try:
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(id=object_id)
    except Exception as e:
        print (e)
        return render(request, 'error.html', {'message': 'Comment object not exist', 'redirect_to': referer})

    comment = Comment()
    comment.user = request.user
    comment.text = text
    comment.content_object = model_obj
    comment.save()
    return redirect(referer)