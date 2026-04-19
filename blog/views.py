from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import PostForm
from .models import Post

def delete_post_view(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        post.delete()
    return redirect('blog:home')

def home_view(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def add_post_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'blog/add_post.html', context)