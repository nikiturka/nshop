from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('product/', include('products.urls')),
    path('categories/', include('categories.urls')),
    path('checkout/', include('checkout.urls')),
    path('__debug__/', include('debug_toolbar.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

