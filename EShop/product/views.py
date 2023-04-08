from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        all_data = super().get_queryset()
        data = all_data.filter(is_active=True)
        return data


# class ProductListView(TemplateView):
#     template_name = 'product/product_list.html'
#
#     def get_context_data(self, **kwargs):
#         all_product = Product.objects.all()
#         content = super().get_context_data()
#         content['products'] = all_product
#         return content


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'key'


# class ProductDetailView(TemplateView):
#     template_name = 'product/product_detail.html'
#
#     def get_context_data(self, **kwargs):
#         content = super().get_context_data()
#         product_slug = kwargs['slug']
#         selected_product = get_object_or_404(Product, slug=product_slug)
#         content['key'] = selected_product
#         return content
class Test(View):


    def post(self, request):

        output = request.POST["product_id"]
        response = Product.objects.get(pk=output)
        request.session['product_favorite'] = response.id

        return redirect(response.get_absolute_url())






