from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Category
from django.core.paginator import Paginator


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
    return render(request, "search-result.html")


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
        p = Paginator(products, 3)
        page = request.GET.get('page')
        page_products = p.get_page(page)
        count = products.count()
        garchig = categories
    else:
        products = Product.objects.all().filter(is_available=True)
        p = Paginator(products, 3)
        page = request.GET.get('page')
        page_products = p.get_page(page)
        count = products.count()

    return render(request, "store.html", {'products': page_products, 'count': count, 'garchig': categories})


def lab3(request):
    products = Product.objects.all()
    return render(request, "lab3.html", {'products': products})
