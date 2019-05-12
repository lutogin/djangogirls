from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post


def post_list(req):
    return render(req, 'blog/post_list.twig', context={
        'posts': Post.objects.all().order_by('published_date'), 'title': 'Blog - главная.'
    })
