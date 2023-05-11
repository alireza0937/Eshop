from django.urls import path
from . import views

urlpatterns = [

    path('', views.BlogListView.as_view(), name='blog-page'),
    path('add-article-comment', views.add_article_comment, name='add_article_comment'),
    path('<str:cat>', views.BlogListView.as_view(), name='spec-cat-page'),
    path("<pk>/", views.DetailsView.as_view(), name="article-detail"),

]
