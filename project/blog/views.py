from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponseRedirect, Http404
from django.urls import reverse


# Create your views here.


database = {
    "saturday" : "this is saturday in dictionry.",
    "sunday" : "this is sunday in dictionry.",
    "monday" : "this is monday in dictionry.",
    "tuesday" : "this is tuesday in dictionry.",
    "wednesday" : "this is wednesday in dictionry.",
    "thursday" : "this is thursday in dictionry.",
    "friday" : "this is friday in dictionry.",
}


def dynamic_number(request,day) :
    days_list = list(database.keys())
    if day < 6 :
        redirect_day = days_list[day - 1]
        redirect_url = reverse("dynamic_number", args=[redirect_day])
        return HttpResponseRedirect(redirect_url)
    
    return HttpResponseNotFound("days not found..") 
    


def dynamic_function(request,day) :
    response = database.get(day)
    convert_data = {
        "key": response,
        "name": day
    }

    if response is None :
        raise Http404()
    
    return render(request, "blog/blog.html", context=convert_data)
    
  



def days_list(request) :
    days_list = list(database.keys())
    context = {
        "key": days_list,
    }
    return render(request, "blog/index.html", context)