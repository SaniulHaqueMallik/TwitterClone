from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        # IF THE FORM IS VALID
        if form.is_valid():
            #yes, save
            form.save()

            # redirect to home
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())
    # get all post upto 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # show
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    # find user
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
