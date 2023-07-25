from django.shortcuts import render
from main.models import Product, ProductImage


def products(request):
    image = ProductImage.objects.filter(is_main=True).select_related('product')
    return render(request, 'main/all.html', {'image': image})
