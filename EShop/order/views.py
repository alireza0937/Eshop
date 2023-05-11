from datetime import date
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from order.models import Order, OrderDetails
from product.models import Product
from django.http import HttpResponse
import requests
import json


def add_product_to_orders(request: HttpRequest):
    productId = request.GET.get('product_id')
    count = request.GET.get('count')
    if int(count) < 1:
        count = 1
    chosen_product = Product.objects.filter(is_active=True, is_delete=False, id=productId).first()
    if chosen_product:
        if request.user.is_authenticated:
            have_open_basket = Order.objects.filter(is_paid=False, user_id=request.user.id).first()
            if have_open_basket is None:
                new_basket = Order(user_id=request.user.id, is_paid=False)
                basket_details = OrderDetails(product_id=chosen_product.id, order=new_basket, count=count)
                new_basket.save()
                basket_details.save()
            else:
                had_this_in_basket = OrderDetails.objects.filter(product_id=chosen_product,
                                                                 order_id=have_open_basket.id).first()
                if had_this_in_basket is not None:
                    had_this_in_basket.count += int(count)
                    had_this_in_basket.save()
                else:
                    basket_details = OrderDetails(product_id=chosen_product.id, order=have_open_basket, count=count)
                    basket_details.save()

            return JsonResponse({
                'status': 'successfully',
                'icon': 'success',
                'text': "محصول مورد نظر با موفقیت به سبد خرید اضافه شد.",
                'confirmButtonText': 'ادامه'

            })
        else:
            return JsonResponse({
                'status': 'not authenticated',
                'icon': 'warning',
                'text': "برای ثبت سفارش باید ایتدا وارد شوید.",
                'confirmButtonText': 'ورود به سایت'
            })
    else:
        return JsonResponse({
            'status': 'product not found!',
            'icon': 'error',
            'text': "محصول مورد نظر یافت نشد.",
            'confirmButtonText': 'ادامه'
        })


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = ''  # Optional
mobile = ''  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/orders/verify/'


@login_required
def send_request(request: HttpRequest):
    all_products = Order.objects.filter(user_id=request.user.id, is_paid=False).first()
    amount = all_products.basket_total() * 10
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
        # "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


@login_required
def verify(request: HttpRequest):

    all_products = Order.objects.filter(user_id=request.user.id, is_paid=False).first()
    amount = all_products.basket_total() * 10
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                user_basket = Order.objects.filter(user_id=request.user.id, is_paid=False).first()
                user_basket.is_paid = True
                user_basket.payment_data = date.today()
                for products in user_basket.orderdetails_set.all():
                    products.final_price = products.get_total_price()
                user_basket.save()
                return HttpResponse('Transaction success.\nRefID: ' + str(
                    req.json()['data']['ref_id']
                ))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')


