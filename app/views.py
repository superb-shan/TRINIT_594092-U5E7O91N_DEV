from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class FeedView(ListView):
    model = Post
    template_name = 'feeds/feed.html'
    context_object_name = 'posts'

