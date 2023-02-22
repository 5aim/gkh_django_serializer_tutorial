from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from articles.serializers import ArticleSerializer
from articles.models import Article


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_view(reqeust, article_id):
    if reqeust.method == 'GET':
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
    return Response(serializer.data)