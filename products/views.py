from django.shortcuts import render
from main.models import Product, ProductImage, ProductInCart
from django.http import JsonResponse


def product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    product_img = ProductImage.objects.filter(product=product_id)

    return render(request, 'main/product.html', {'product': product, 'product_img': product_img})


def cart_add(request):
    return_dict = dict()
    session_key = request.session.session_key

    data = request.POST
    product_id = data.get("id")
    quantity = data.get("quantity")

    if data['is_delete'] == 'delete':
        product_to_delete = ProductInCart.objects.get(product_id=product_id, session_key=session_key)
        product_to_delete.delete()

    else:
        product_in_cart, created = ProductInCart.objects.get_or_create(session_key=session_key,
                                                                       product_id=product_id,
                                                                       is_active=True,
                                                                       defaults={'number': quantity})
        if not created:
            product_in_cart.number += int(quantity)
            product_in_cart.save(force_update=True)

    product_in_cart_for_dict = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    product_in_cart_number = product_in_cart_for_dict.count()

    return_dict['product_in_cart_number'] = product_in_cart_number
    return_dict["products"] = list()

    for item in product_in_cart_for_dict:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["id"] = item.id
        product_dict["price"] = item.price_per_item
        product_dict["number"] = item.number
        product_dict["is_active"] = item.is_active

        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)
