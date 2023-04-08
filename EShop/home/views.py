from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View


def index(request):
    return render(request, 'home/index.html')


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


def site_header(request):
    return render(request, 'shared/header.html')


def footer(request):
    return render(request, 'shared/footer.html')
