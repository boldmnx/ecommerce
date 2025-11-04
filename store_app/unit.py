import sqlite3 as sql
from store_app.models import Category
from carts.models import Cart, CartItem
from carts.views import _cart_id


def category_data(request):
    categories = Category.objects.all()
    return {'categories': categories}


# def menu_links(request):
#     links = Category.objects.all()
#     return dict(links=links)

def counter(request):
    cart_count = 0
    # if 'admin' in request.path:
    #     return {}
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            cart_count += item.quantity
    except Cart.DoesNotExist:
        cart_count = 0
    return dict(cart_count=cart_count)

# cart 0 doosh hasagdaj bolohgui bas baraanii uldegdel 5 baival 5aas deesh yvj bolohgui
