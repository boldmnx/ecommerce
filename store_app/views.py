from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Category
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    productAll = Product.objects.all()
    return render(request, "index.html", {'productAll': productAll})


def dashboard(request):
    return render(request, "dashboard.html")


def order_complete(request):
    return render(request, "order_complete.html")


def product_detail(request, product_slug=None, cat_slug=None):
    product = None
    if product_slug != None:
        product = Product.objects.get(
            slug=product_slug, category__slug=cat_slug)
        return render(request, "product-detail.html", {'product': product})
    else:
        return redirect()


def register(request):
    return render(request, "register.html")


def search_result(request):
    keyword = request.GET.get('keyword', '').strip()
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')
    cat_slug = request.GET.get('category', '')
    products = Product.objects.all()

    # if cat_slug and min_price and max_price:
    #     categories = get_object_or_404(Category, slug=cat_slug)
    #     products = Product.objects.filter(
    #         category=categories, price__gte=min_price, price__lte=max_price)

    #     products = Product.objects.filter(Q(category=categories) & Q(
    #         price__gte=min_price) & Q(price__lte=max_price))

    # Хайлтын keyword
    if keyword:
        products = products.filter(
            Q(product_name__icontains=keyword) |
            Q(description__icontains=keyword)
        )

    if cat_slug:
        categories = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)

    # Үнийн шүүлтүүр
    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    context = {
        "products": products,
        "keyword": keyword,
        "min_price": min_price,
        "count": len(products),
        "keyword": keyword,
        "max_price": max_price
    }
    return render(request, "store.html", context)


def signin(request):
    return render(request, "signin.html")


def store(request):
    products = Product.objects.all()
    return render(request, "store.html", {'products': products})


def store(request, slug=None):
    categories = None
    products = None
    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=categories)
        p = Paginator(products, 6)
        page = request.GET.get('page')
        page_products = p.get_page(page)
        count = products.count()
        garchig = categories
    else:
        products = Product.objects.all().filter(is_available=True)
        p = Paginator(products, 6)
        page = request.GET.get('page')
        page_products = p.get_page(page)
        count = products.count()

    return render(request, "store.html", {'products': page_products, 'count': count, 'garchig': categories})


def lab3(request):
    products = Product.objects.all()
    return render(request, "lab3.html", {'products': products})
