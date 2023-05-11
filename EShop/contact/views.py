from django.shortcuts import render, redirect
from .forms import  ContactUsModelForm, ProfileImagesForm
from .models import ContactUs, ProfileM
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic import ListView
from SiteSetting.models import SiteSettings

class ContactUsView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactUsModelForm
    success_url = '/'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        settings: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
        context['setting'] = settings
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProfileImage(View):
    def get(self, request):
        form = ProfileImagesForm()

        return render(request, 'contact/profileimage.html', {
            'form': form,
        })
    def post(self, request):
        submit_data = ProfileImagesForm(request.POST, request.FILES)
        if submit_data.is_valid():
            profile = ProfileM(image=request.FILES['user_image'])
            profile.save()
            # saveimage(request.FILES['image'])
            return render(request, 'contact/profileimage.html')

        return render(request, 'contact/profileimage.html', {
            'form': submit_data,
        })


class ProfileImagesList(ListView) :
    template_name = 'contact/imagelist.html'
    context_object_name = 'proimages'
    model = ProfileM

