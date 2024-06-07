from django.db import models


class Autor(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя автора')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    article = models.TextField(blank=True, verbose_name='Статья')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.name}: {self.article[:10]}...'
