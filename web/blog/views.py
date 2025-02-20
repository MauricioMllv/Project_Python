from django.shortcuts import render
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})