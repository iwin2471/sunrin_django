from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
# Create your views here.



def post_list(request):
        posts=Post.objects.all()
        return render(request,'firstapp/index.html',{'posts':posts})

def second(request):
        return render(request,'firstapp/second.html')

def thrid(request):
        return render(request,'firstapp/third.html')

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
