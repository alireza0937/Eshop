from django.urls import path
from . import views


urlpatterns = [

    path("",views.days_list, name='days_list'),
    path("<int:day>",views.dynamic_number, name='dynamic_number'),
    path("<str:day>",views.dynamic_function, name='dynamic_function'),
    

]