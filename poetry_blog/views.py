from django.shortcuts import render

from .models import Blog_Post

# Create your views here.

def index(request):
    all_posts = Blog_Post.objects.all()
    return render(request, 'index.html', {'all_posts': all_posts})

def single_post(request, pk):
    all_posts = Blog_Post.objects.get(id=pk)
    return render(request, 'single_post.html', {'all_posts': all_posts})

