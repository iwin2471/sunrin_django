from django.shortcuts import render
from .models import Post
def post_list(req):
    posts = Post.objects.all()
    return render(req, 'firstapp\home.html', {'posts':posts})

def second(req):
    return render(req, 'firstapp\second.html')

# Create your views here.
