from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import CommentForm, PostForm
from .models import Comment, Post


class AboutView(TemplateView):
    template_name = 'posts/sobre.html'


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.select_related('author').order_by('-created_at')
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.object.pk})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:list')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/comment_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.post = self.post_obj
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post_obj
        return context

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.post_obj.pk})
