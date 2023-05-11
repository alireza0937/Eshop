from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from UserPanel.forms import EditProfileForm, ChangePasswordForm
from account.models import User
from order.models import OrderDetails, Order
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class EditProfile(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        form = EditProfileForm(instance=current_user)
        return render(request, 'userpanel/edit_profile.html', context={
            'form': form
        })

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        form = EditProfileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'userpanel/edit_profile.html', context={
                'form': form
            })

        return render(request, 'userpanel/edit_profile.html', context={
            'form': form
        })


@method_decorator(login_required, name='dispatch')
class ChangePassword(View):
    def get(self, request):
        form = ChangePasswordForm()
        return render(request, 'userpanel/change_password.html', context={
            'form': form
        })

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('new_password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login-page'))

            else:
                form.add_error('new_password', 'رمز وارد شده اشتباه است.')

        return render(request, 'userpanel/change_password.html', context={
            'form': form
        })


@login_required
def user_dashboard(request):
    return render(request, 'userpanel/user_panel.html')


@login_required
def user_panel_menu_component(request: HttpRequest):
    return render(request, 'userpanel/components/components.html')


@login_required
def user_basket(request: HttpRequest):
    user = Order.objects.filter(user_id=request.user.id,
                                is_paid=False).first()
    if user is not None:
        user_orders = OrderDetails.objects.filter(order_id=user.id)
        sum = 0
        for all_product in user_orders:
            sum += all_product.count * all_product.product.price
        return render(request, 'userpanel/user_cart.html', context={
            'data': user_orders,
            'sum': sum,
        })
    return render(request, 'userpanel/user_cart.html')


@login_required
def remove_product(request: HttpRequest):
    product_ID = request.GET.get('id')
    user_orders = OrderDetails.objects.filter(order__user_id=request.user.id,
                                              product_id=product_ID,
                                              order__is_paid=False)
    user_orders.delete()
    return redirect(reverse('user-cart-page'))


@login_required
def change_amount_of_product(request: HttpRequest):
    Id = request.GET.get('id')
    op = request.GET.get('op')
    product = OrderDetails.objects.filter(product_id=Id, order__user_id=request.user.id, order__is_paid=False).first()
    if op == 'increase':
        product.count += 1
    else:
        if product.count >= 1:
            product.count -= 1
    product.save()
    return redirect(reverse('user-cart-page'))


class ShopHistory(ListView):
    model = Order
    template_name = 'userpanel/shoping_history.html'
    context_object_name = 'history'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_paid=True, user_id=self.request.user.id)
        return query


def show_order_details(request: HttpRequest, pk):
    user_order = Order.objects.prefetch_related('orderdetails_set').filter(id=pk, is_paid=True, user_id=request.user.id).first()
    return render(request, 'userpanel/user_Previous_purchase.html', context={
        'data': user_order
    })

