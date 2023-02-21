from django.shortcuts import render
from main.models import ProductInCart, ProductInOrder, Order
from .forms import UserForm
from django.contrib.auth.models import User


def checkout(request):
    session_key = request.session.session_key
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    form = UserForm(request.POST or None)

    if request.POST:
        print(request.POST)
        if form.is_valid():
            data = request.POST
            name = data["name"]
            phone = data["phone_number"]

            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})
            order = Order.objects.create(customer_name=name, customer_phone=phone)

            for name, value in data.items():
                if name.startswith("product_in_cart_"):
                    product_in_cart_id = name.split("product_in_cart_")[1]
                    product_in_cart_ = ProductInCart.objects.get(id=product_in_cart_id)
                    product_in_cart_.number = value
                    product_in_cart_.save(force_update=True)
                    ProductInOrder.objects.create(product=product_in_cart_.product,
                                                  number=product_in_cart_.number,
                                                  price_per_item=product_in_cart_.price_per_item,
                                                  total_for_product=product_in_cart_.total_price,
                                                  order=order
                                                  )

    return render(request, 'main/checkout.html', locals())
