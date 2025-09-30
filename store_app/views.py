from django.shortcuts import get_object_or_404, render
from .models import Product, Category


def index(request):
    return render(request, "index.html")


def cart(request):
    return render(request, "cart.html")


def dashboard(request):
    return render(request, "dashboard.html")


def order_complete(request):
    return render(request, "order_complete.html")


def product_detail(request, id):
    return render(request, "product-detail.html", {'id': id})


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
        count = products.count()
        garchig = slug
    else:
        products = Product.objects.all().filter(is_available=True)
        count = products.count()
    return render(request, "store.html", {'products': products, 'count': count, 'garchig': categories})


def lab3(request):
    products = Product.objects.all()
    return render(request, "lab3.html", {'products': products})
