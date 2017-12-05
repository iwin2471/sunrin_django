from django.shortcuts import render
from .models import Post
def post_list(req):
    posts = Post.objects.all()
    return render(req, 'firstapp\main.html', {'posts':posts})

def second(req):
    return render(req, 'firstapp\second.html')

def intro(req):
    return render(req, 'firstapp\introduce.html')

def study(req):
    return render(req, 'firstapp\study.html')

# Create your views here.
