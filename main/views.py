from django.shortcuts import render
from .models import ProductImage, ProductInCart


def main(request):
    product_img = ProductImage.objects.select_related('product').all()

    return render(request, 'main/main.html', {'product_img': product_img})

