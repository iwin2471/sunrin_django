from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(req):
    posts = Post.objects.all()
    return render(req, 'firstapp\main.html', {'posts':posts})

def second(req):
    return render(req, 'firstapp\second.html')

def intro(req):
    return render(req, 'firstapp\introduce.html')

def study(req):
    return render(req, 'firstapp\study.html')

def google(req):
    return render(req, 'firstapp\google.html')

def post_new(request):
    form = PostForm()
    return render(request, 'firstapp\post_edit.html', {'form': form})

def post_detail(req):
    return render(req, 'firstapp\detail.html')
def post(req):
    if req.method == "POST ":
        form = PostForm(req.POST)
        if form.is_vaild():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('firstapp.views.post_detail', post_id=poost.pk)
    else:
        form = PostForm()
    return render(req, 'firstapp\form.html', {'form': form})

# Create your views here.
