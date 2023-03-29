from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.


def product_list(request):
    all_products = Product.objects.all().order_by('price')
    data = {
        'products': all_products,
    }
    return render(request, 'product/product_list.html', context=data)


def product_detail(request, product_slug):
    selected_product = get_object_or_404(Product, slug=product_slug)
    datas = {
        'key': selected_product
    }
    return render(request, 'product/product_detail.html', context=datas)
