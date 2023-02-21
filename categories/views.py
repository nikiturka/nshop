from django.shortcuts import render
from main.models import Product, ProductImage


def products(request):
    all_products = Product.objects.all()
    image = ProductImage.objects.filter(is_main=True)
    return render(request, 'main/all.html', {'all_products': all_products, 'image': image})
