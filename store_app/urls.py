from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('order-complete/', views.order_complete, name="order_complete"),
    path('register/', views.register, name="register"),
    path('search/', views.search_result, name="search_result"),



    path('<slug:cat_slug>/<slug:product_slug>/',
         views.product_detail, name="product_detail"),
    path('store/<slug:cat_slug>/', views.store, name="products_by_category"),
    path('store/', views.store, name="store"),



    path('signin/', views.signin, name="signin"),
    path('lab3/', views.lab3, name="lab3"),
]
