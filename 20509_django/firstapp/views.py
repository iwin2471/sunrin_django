from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(req):
    posts = Post.objects.all()
    return render(req, 'firstapp\post_list.html', {'posts':posts})

def second(req):
    return render(req, 'firstapp\second.html')

def intro(req):
    return render(req, 'firstapp\introduce.html')

def study(req):
    return render(req, 'firstapp\study.html')

def google(req):
    return render(req, 'firstapp\google.html')

def post_new(req):
    if req.method == "POST":
        form = PostForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = req.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(req, 'firstapp/post_edit.html', {'form': form})

def post_detail(req):
    return render(req, 'firstapp\detail.html')

def post_edit(req, pk):
    post = get_object_or_404(Post, pk=pk)
    if req.method == "POST":
        form = PostForm(req.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = req.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'firstapp/post_edit.html', {'form': form})

# Create your views here.
