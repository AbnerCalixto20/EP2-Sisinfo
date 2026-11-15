from django import forms

from .models import Post


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
