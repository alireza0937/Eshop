from django.shortcuts import render, redirect
from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs
from django.views import View

# Create your views here.

class ContactUsView(View):
    
    def post(self, request):
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("index-page")


    def get(self, request):
        contact_form = ContactUsModelForm()
        return render(request, 'contact/contact.html', {
            'form': contact_form
        })

















def contact(request):
    if request.method == 'POST':
        # contact_form = ContactUsForm(request.POST)
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("index-page")
                

    else:       
        # contact_form = ContactUsForm()
        contact_form = ContactUsModelForm()
    return render(request, 'contact/contact.html', {
            'form': contact_form
        })


