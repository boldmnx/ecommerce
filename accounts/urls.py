
from django.urls import path
from ecommerce import settings
from django.conf.urls.static import static
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('signout/', views.signout, name='signout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
