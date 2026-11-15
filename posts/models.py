from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('Título', max_length=200)
    content = models.TextField('Conteúdo (HTML)')
    pub_date = models.DateTimeField('Data de postagem', default=timezone.now)
    categories = models.ManyToManyField(
        Category,
        related_name='posts',
        blank=True,
        verbose_name='Categorias',
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Post',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Autor',
    )
    text = models.TextField('Texto')
    created_at = models.DateTimeField('Data de postagem', default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return f'Comentário de {self.author} em {self.post}'
