from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})

def create(request):
    if request.method == "POST":
        form = WriteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = WriteForm()
        return render(request, 'create.html', {"form": form})

def delete(request, article_id):
    post = get_object_or_404(Post, id=article_id)
    post.delete()
    return redirect("index")

def update(request, article_id):
    post = get_object_or_404(Post, id=article_id)
    print(post)
    if request.method == "POST":
        form = WriteForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = WriteForm(instance=post)
        print(form)
        return render(request, 'update.html', {"form": form})