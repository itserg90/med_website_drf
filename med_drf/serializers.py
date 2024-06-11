import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from med_drf.models import Article


# class ArticleModel:
#     def __init__(self, name, article):
#         self.name = name
#         self.article = article


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Article
        # fields = ('name', 'article', 'autor', 'user')
        fields = '__all__'

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.article = validated_data.get('article', instance.article)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.autor_id = validated_data.get('autor_id', instance.autor_id)
        instance.save()
        return instance

# def encode():
#     model = ArticleModel('Serg', 'seee')
#     model_sr = ArticleSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"name":"Serg","article":"seee"}')
#     data = JSONParser().parse(stream)
#     serializer = ArticleSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
#     print(serializer.data)
#     print(serializer.fields)
#     print(serializer.validators)
