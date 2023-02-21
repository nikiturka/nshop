from django.shortcuts import render
from .models import ProductImage


def main(request):
    product_img = ProductImage.objects.all()

    return render(request, 'main/main.html', {'product_img': product_img})

