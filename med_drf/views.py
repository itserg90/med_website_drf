from rest_framework import generics

from med_drf.models import Article
from med_drf.serializers import ArticleSerializer


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
