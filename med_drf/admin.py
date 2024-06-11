from django.contrib import admin

from med_drf.models import Article, Autor


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'is_published', 'autor', 'id', 'user')


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
