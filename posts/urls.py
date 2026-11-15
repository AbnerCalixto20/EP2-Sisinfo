from django.urls import path

from .views import (
    AboutView,
    CategoryDetailView,
    CategoryListView,
    CommentCreateView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('sobre/', AboutView.as_view(), name='about'),
    path('posts/create/', PostCreateView.as_view(), name='create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('posts/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]
