from django.contrib import admin
from .models import *


admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductInOrder)
admin.site.register(ProductInCart)

