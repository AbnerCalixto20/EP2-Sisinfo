from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': 'Título',
            'content': 'Conteúdo (HTML)',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Digite o título do post'}),
            'content': forms.Textarea(attrs={'placeholder': 'Digite o conteúdo em HTML'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        labels = {
            'author': 'Autor',
            'text': 'Comentário',
        }
        widgets = {
            'text': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Escreva seu comentário sobre este post...'}
            ),
        }
