from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
from .forms.forms import PostForm


def post_list(req):
    return render(req, 'blog/post_list.twig', context={
        'posts': Post.objects.all().order_by('published_date'),
        'title': 'Blog - главная.'
    })


def add_post(req):
    if req.method == 'GET':
        return render(req, 'blog/add-post.twig', {
            'form': PostForm()
        })
    else:
        form = PostForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = req.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
        else:
            return redirect('add_post')
