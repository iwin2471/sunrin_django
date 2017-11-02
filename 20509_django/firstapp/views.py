from django.shortcuts import render
from .models import Post
def post_list(req):
    posts = Post.objects.all()
    return render(req, 'firstapp\home.html', {'posts':posts})

# Create your views here.
