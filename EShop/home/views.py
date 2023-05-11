from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View

from SiteSetting.models import SiteSettings, SliderSetting
from order.models import Order
from product.models import Product, ProductVisit, ProductCategory


def index(request):
    return render(request, 'home/index.html')


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        slider_objects: SliderSetting = SliderSetting.objects.filter(is_active=True)
        context['sliders'] = slider_objects
        context['new_products'] = Product.objects.filter(is_new=True)[:4]
        context['most_view'] = Product.objects.annotate(visit_count=Count('productvisit')).all().order_by(
            '-visit_count')[:4]
        context['categories'] = list(ProductCategory.objects.all()[:4])
        context['popular_product'] = Order.objects.filter(is_paid=True).all()
        print(Order.objects.filter(is_paid=True).all())
        return context


def site_header(request):
    setting = SiteSettings.objects.filter(is_main_setting=True).first()

    return render(request, 'shared/header.html', context={'setting': setting})


def footer(request):
    return render(request, 'shared/footer.html')


class AboutUsView(TemplateView):
    template_name = 'home/aboutus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        data: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
        context['data'] = data
        return context
