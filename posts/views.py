from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Post


def about(request):
    return render(request, 'posts/sobre.html')


def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'post_list': posts})


def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        pub_date_raw = request.POST.get('pub_date', '')

        if pub_date_raw:
            pub_date = timezone.make_aware(datetime.fromisoformat(pub_date_raw))
        else:
            pub_date = timezone.now()

        post = Post(title=title, content=content, pub_date=pub_date)
        post.save()
        return redirect('posts:detail', pk=post.pk)

    return render(request, 'posts/post_form.html')


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title', '')
        post.content = request.POST.get('content', '')
        pub_date_raw = request.POST.get('pub_date', '')
        if pub_date_raw:
            post.pub_date = timezone.make_aware(datetime.fromisoformat(pub_date_raw))
        post.save()
        return redirect('posts:detail', pk=post.pk)

    return render(request, 'posts/post_form.html', {'post': post})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:list')

    return render(request, 'posts/post_confirm_delete.html', {'post': post})
