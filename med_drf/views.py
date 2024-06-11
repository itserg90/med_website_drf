from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from med_drf.models import Article, Autor
from med_drf.serializers import ArticleSerializer
from med_drf.permissions import IsAdminOrReadOnly, IsUserOrReadOnly


# class ArticleViewSet(viewsets.ModelViewSet):
#     # queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Article.objects.all()[:3]
#
#         return Article.objects.filter(pk=pk)
#
#     @action(methods=['GET'], detail=True)
#     def autor(self, request, pk=None):
#         autor = Autor.objects.get(pk=pk)
#         return Response({'autor': autor.name})

class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ArticleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


# class ArticleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


class ArticleAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly, )
