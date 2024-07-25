from django.shortcuts import render
from django.db.models import Count,Sum,Avg,Max,F
from app.models import Product, Category, Order

from app.models import Product,Order


# Create your views here.

def report(request):
    product_revenue = Product.objects.annotate(total_product_revenue=Sum(F('order__quantity') * F('price')))
    order_quantity = Order.objects.annotate(Sum('quantity'))
    context = {'product_revenue': product_revenue,
               'order_quantity': order_quantity}
    return render(request,'daily_report.html',context)



