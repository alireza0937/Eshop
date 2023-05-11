from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView
from . import models
from .models import ArticleCategoryModels, Article, Comments


class BlogView(View):
    def get(self, request):
        news: models.Article = models.Article.objects.filter(is_active=True)
        data = {
            'context': news,
        }
        return render(request, 'article/blogs.html', context=data)


class BlogListView(ListView):
    model = models.Article
    template_name = 'article/blogs.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        query = super().get_queryset()
        response = self.kwargs.get('cat')
        if response is not None:
            query = query.filter(selected_categories__url_title__iexact=response, is_active=True)
        return query


class DetailsView(DetailView):
    model = Article
    template_name = 'article/articledetails.html'
    context_object_name = 'key'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article: Article = kwargs.get('object')
        comments = Comments.objects.filter(article_id=article.id, is_span=False, parent=None).prefetch_related(
            'comments_set').order_by('-create_date')
        context['comments'] = comments
        return context


def categories_sort(request):
    categories = ArticleCategoryModels.objects.filter(is_active=True, parent=None)
    data = {
        'key': categories
    }
    return render(request, 'sort/categories.html', context=data)


def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated:
        article_comment = request.GET.get('article_comment')
        article_id = request.GET.get('article_id')
        user_message = Comments(article_id=article_id, user_id=request.user.id, message=article_comment)
        user_message.save()
    return HttpResponse("set!")
