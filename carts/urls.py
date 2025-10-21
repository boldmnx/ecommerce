
from django.contrib import admin
from django.urls import path
from ecommerce import settings
from django.conf.urls.static import static
from store_app.views import (
    index, register, dashboard, order_complete,
    product_detail, search_result, store, signin
)
from carts.views import (
    cart, add_cart, remove_cart_item, reduce_cart_item
)

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<int:product_id>/', add_cart, name='add_cart'),
    path('remove/<int:product_id>/', remove_cart_item, name='remove_cart_item'),
    path('reduce/<int:product_id>/', reduce_cart_item, name='reduce_cart_item'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
