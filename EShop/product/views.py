from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        all_data = super().get_queryset()
        data = all_data.filter(is_active=True)
        return data


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'key'


class Test(View):

    def post(self, request):
        output = request.POST["product_id"]
        response = Product.objects.get(pk=output)
        request.session['product_favorite'] = response.id

        return redirect(response.get_absolute_url())
