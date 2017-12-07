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
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(req):
    return render(req, 'firstapp\detail.html')

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# Create your views here.
