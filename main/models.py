from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, default=None, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.customer_phone


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()
    is_new = models.BooleanField(default=True)
    discount = models.IntegerField()
    category = models.CharField(max_length=50, default='')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField()
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_for_product = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order.customer_phone

    def save(self, *args, **kwargs):
        number = str(self.number)
        number = int(number)

        price_per_item = self.product.price
        price_per_item = str(price_per_item)
        price_per_item = float(price_per_item)

        total = number * price_per_item
        self.total_for_product = total
        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(instance, **kwargs):
    order = instance.order
    all_products = ProductInOrder.objects.filter(order=order)

    order_total_price = 0
    for item in all_products:
        order_total_price += item.total_for_product

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images', default='')
    is_main = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class ProductInCart(models.Model):
    session_key = models.CharField(max_length=128, default='')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        number = str(self.number)
        number = int(number)

        price_per_item = self.product.price
        price_per_item = str(price_per_item)
        price_per_item = float(price_per_item)
        self.price_per_item = price_per_item

        total = number * price_per_item
        self.total_price = total

        super(ProductInCart, self).save(*args, **kwargs)
