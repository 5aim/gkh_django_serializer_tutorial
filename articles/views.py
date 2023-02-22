from rest_framework.decorators import api_view
from rest_framework.response import Response

from articles.serializers import ArticleSerializer
from articles.models import Article


@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)