from django.db.models import Count, Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from SiteSetting.models import AdvModel
from .models import Product, ProductCategory, ProductBrand, ProductVisit, ProductGallery
from utils.http_request import get_client_ip


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        all_data = super().get_queryset()
        min_price = self.request.GET.get('minprice')
        max_price = self.request.GET.get('maxprice')
        cat = self.kwargs.get('cat')
        brand = self.kwargs.get('brand')
        if cat is not None:
            all_data = all_data.filter(category__url_title__iexact=cat)

        if brand is not None:
            all_data = all_data.filter(brand__url_title__iexact=brand)

        if min_price is not None:
            all_data = all_data.filter(price__gte=min_price)

        if max_price is not None:
            all_data = all_data.filter(price__lte=max_price)
        return all_data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['adv'] = AdvModel.objects.filter(is_active=True,
                                                 position__iexact=AdvModel.BannerPosition.product_list).first()

        return context


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'key'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        loaded_product: Product = self.object
        loaded_product_id = loaded_product.brand.id
        context['related_products'] = Product.objects.filter(brand_id=loaded_product_id).exclude(
            title=loaded_product.title)[:3]
        context['imgs'] = list(ProductGallery.objects.filter(product_id=loaded_product.id).all())
        context['by_categories'] = list(Product.objects.filter().all())
        ip = get_client_ip(self.request)
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user.id
        visit = ProductVisit(ip=ip, user_id=user, product=loaded_product)
        visit.save()
        return context


def product_categories(request):
    cat = ProductCategory.objects.filter(is_active=True)
    return render(request, 'product/components/product_cat.html', context={
        'key': cat
    })


def product_brands(request):
    all_brands = ProductBrand.objects.annotate(products_count=Count("product")).filter(is_active=True)
    return render(request, 'product/components/product_brand.html', context={
        'all_brands': all_brands
    })
