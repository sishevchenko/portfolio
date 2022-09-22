from django.shortcuts import render
from .models import Post


def all_blogs(request):
    posts = Post.objects.order_by("-date")[:10]
    return render(request, 'blog/all_blogs.html', {"posts": posts})
