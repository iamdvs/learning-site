from django.urls import path

from .views import *
from .views import PostListView
from .views import ArticleDetialView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView
#Articlemain

urlpatterns = [
    path('',PostListView.as_view(),name="index"),
    path('series/',Seri.as_view(),name="series"),
    path('series/<int:slug>',seriesDetail,name="series_detail"),
    path('article/',indexA,name="article"),
    path('article/<int:pk>/',ArticleDetialView.as_view(),name="article-detail"),
    path('article/new/',ArticleCreateView.as_view(),name="article-create"),
    path('article/<int:pk>/update/',ArticleUpdateView.as_view(),name="article-update"),
    path('article/<int:pk>/delete/',ArticleDeleteView.as_view(),name="article-delete"),

]
