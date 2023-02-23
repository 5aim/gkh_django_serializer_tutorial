from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name="article_list"), # 슬래시 넣으면 못불러옴.
    path('<int:article_id>/', views.ArticleDetail.as_view(), name="article_detail_view"),
]
