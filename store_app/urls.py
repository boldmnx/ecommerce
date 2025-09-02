from django.urls import path
from .views import baraa_burtgel

urlpatterns = [
    path('', baraa_burtgel, name='baraa_burtgel')
]
