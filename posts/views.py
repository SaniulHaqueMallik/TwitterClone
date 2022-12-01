from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def like(request):
    cd = Post.objects.all()
    return render(request,('posts.html'),{'cd':cd})