from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from django.http import Http404
from rest_framework.views import APIView

from articles.serializers import ArticleSerializer
from articles.models import Article

from drf_yasg.utils import swagger_auto_schema

# @api_view(['GET', 'POST'])
# def articleAPI(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 위에 함수형 뷰에서 아래 클래스뷰로 바꿔줌.

class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def articleDetail(request, article_id):
#     if request.method == 'GET':
#         article = get_object_or_404(Article, id=article_id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         article = get_object_or_404(Article, id=article_id)
#         serializer = ArticleSerializer(article, data = request.data) # 뒤에 받은 데이터를 앞에 데이터로 바꿔줌.
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#     elif request.method == 'DELETE':
#         article = get_object_or_404(Article, id=article_id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# 위에 함수형 뷰에서 아래 클래스뷰로 바꿔줌.

class ArticleDetail(APIView):

    def get(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    
    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data = request.data) # 뒤에 받은 데이터를 앞에 데이터로 바꿔줌.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
