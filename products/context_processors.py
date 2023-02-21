from main.models import ProductInCart


def cart_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    product_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    product_in_cart_number = product_in_cart.count()

    return locals()

