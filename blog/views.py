#blog/views.py 
from django.shortcuts import render
from .models import Post

# Create your views here.

def blog_index(request):
    posts = Post.objects.filter(status='published').order_by('-pubished_date')
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog_index.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "blog/blog_detail.html", context)
