from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import MobileHealthStationOrderForm
from . import services


def list_products_view(request):
    """return list of products"""
    model1 = Product.objects.all()
    model2 = Category.objects.all()
    return render(request, 'product/products.html', {"categories": model2, "products": model1})


def categorized(request, cat_name):
    """return list of categorised products"""
    model1 = Product.objects.filter(category__cat_name=cat_name)
    model2 = Category.objects.all()
    return render(request, "product/products.html", {"categories": model2, "products": model1})


def single_product_view(request, pk):
    """return single product and form for order with email notification"""
    form = MobileHealthStationOrderForm()
    model1 = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = MobileHealthStationOrderForm(request.POST)
        if form.is_valid():
            form_data = form.clean()
            services.mobile_station_order_send_mail(**form_data)
            return redirect('home')
        else:
            return render(request, "product/single_product.html", {"product": model1, "form": form})
    else:
        return render(request, "product/single_product.html", {"product": model1, "form": form})

